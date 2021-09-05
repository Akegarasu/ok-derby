# -*- coding=UTF-8 -*-
# pyright: strict

from __future__ import annotations


from typing import Text
import os
import sys

__dirname__ = os.path.dirname(os.path.abspath(__file__)) if hasattr(sys, 'frozen') else os.path.dirname(sys.executable)


def path(*paths: Text) -> Text:
    return os.path.join(__dirname__, *paths)
