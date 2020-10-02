# SPDX-FileCopyrightText: Copyright (c) 2020 Bryan Siepert for Adafruit Industries
#
# SPDX-License-Identifier: MIT
"""A TLA202x subclass to represent the TLA2024"""
from . import TLA2024 as TLA202x

A0 = 0
A1 = 1
A2 = 2
A3 = 3


class TTLA202x:
    """New slaaa"""

    @staticmethod
    def foozer2():
        """gooooo"""
        print("foo? zern")


class TLA2024(TLA202x):
    """Dock String"""

    @staticmethod
    def foozer2():
        """gooooo"""
        print("foo2? zern2")
