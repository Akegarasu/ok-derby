# -*- coding=UTF-8 -*-
# pyright: strict

from . import mathtools
from . import template
import time
from typing import Callable, Iterable, Iterator, Text, Tuple, Union

from . import clients
from models.controller import missionController


def resize_proxy() -> mathtools.ResizeProxy:
    """Resize proxy to current client width."""
    return mathtools.ResizeProxy(clients.current().width)


def tap(point: Tuple[int, int]):
    clients.current().tap(point)
    template.invalidate_screeshot()


def count_image(*tmpl: Union[Text, template.Specification]) -> int:
    ret = 0
    for _ in template.match(template.screenshot(), *tmpl):
        ret += 1
    return ret


def match_image_until_disappear(
    *tmpl: Union[Text, template.Specification],
    sort: Callable[
        [Iterator[Tuple[template.Specification, Tuple[int, int]]]],
        Iterable[Tuple[template.Specification, Tuple[int, int]]],
    ] = lambda x: x,
) -> Iterator[Tuple[template.Specification, Tuple[int, int]]]:
    while True:
        count = 0
        for i in sort(template.match(template.screenshot(max_age=0), *tmpl)):
            count += 1
            yield i
            break  # actions will make screenshot outdate
        if count == 0:
            break


def wait_image(
    *tmpl: Union[Text, template.Specification]
) -> Tuple[template.Specification, Tuple[int, int]]:
    while True and missionController.FLAG:
        try:
            return next(template.match(template.screenshot(max_age=0), *tmpl))
        except StopIteration:
            time.sleep(0.01)
    return (template.Specification(""), (0, 0))



def wait_image_stable(
    *tmpl: Union[Text, template.Specification],
    duration: float = 1.0,
) -> Tuple[template.Specification, Tuple[int, int]]:
    t, last_pos = wait_image(*tmpl)
    start_time = time.time()
    while True:
        time.sleep(0.01)
        _, pos = wait_image(t)
        if pos != last_pos:
            start_time = time.time()
        if time.time() - start_time > duration:
            break
        last_pos = pos
    return t, last_pos


def wait_image_disappear(*tmpl: Union[Text, template.Specification]) -> None:
    while True and missionController.FLAG:
        try:
            next(template.match(template.screenshot(max_age=0), *tmpl))
            time.sleep(0.5)
        except StopIteration:
            break


def tap_image(
    name: Union[Text, template.Specification], *, x: int = 0, y: int = 0
) -> bool:
    try:
        name, pos = next(template.match(template.screenshot(), name))
        tap((pos[0] + x, pos[1] + y))
        return True
    except StopIteration:
        return False


def wait_tap_image(
    name: Union[Text, template.Specification], *, x: int = 0, y: int = 0
) -> None:
    _, last_pos = wait_image(name)
    while True:
        _, pos = wait_image(name)
        if pos == last_pos:
            break
        last_pos = pos
    tap((pos[0] + x, pos[1] + y))


def swipe(point: Tuple[int, int], *, dx: int = 0, dy: int = 0, duration: float = 0.1):
    clients.current().swipe(point, dx=dx, dy=dy, duration=duration)
    template.invalidate_screeshot()


def reset_client_size() -> None:
    client = clients.current()
    if isinstance(client, clients.DMMClient):
        client.setup()
