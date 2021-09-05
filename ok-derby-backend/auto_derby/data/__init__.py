# -*- coding=UTF-8 -*-
# pyright: strict

from __future__ import annotations


from typing import Text
import os
import sys

__dirname__ = os.path.join(os.path.dirname(sys.executable), "data") \
                if hasattr(sys, "frozen") else os.path.dirname(os.path.abspath(__file__))


def path(*paths: Text) -> Text:
    return os.path.join(__dirname__, *paths)
