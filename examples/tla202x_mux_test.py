# SPDX-FileCopyrightText: 2020 Bryan Siepert, written for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense
# pylint:disable=no-member
import board
import busio
from adafruit_tla202x import TLA2024, Mux

i2c = busio.I2C(board.SCL, board.SDA)
tla = TLA2024(i2c)

for i in range(4):
    channel = i
    tla.input_channel = channel
    print("Channel", channel, ":", tla.voltage)
# Mux.MUX_AIN0_AIN1
# Mux.MUX_AIN0_AIN3
# Mux.MUX_AIN1_AIN3
# Mux.MUX_AIN2_AIN3
# Mux.MUX_AIN0_GND
# Mux.MUX_AIN1_GND
# Mux.MUX_AIN2_GND
# Mux.MUX_AIN3_GND
tla.mux = Mux.MUX_AIN0_GND
