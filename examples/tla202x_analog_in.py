# SPDX-FileCopyrightText: Copyright (c) 2020 Bryan Siepert for Adafruit Industries
# SPDX-License-Identifier: MIT
import time
import board

import adafruit_tla202x.tla2024 as TLA
from adafruit_tla202x.analog_in import AnalogIn

################ AnalogIn Example #####################
#
# This example shows how to use the AnalogIn class provided
# by the library by creating an AnalogIn instance and using
# it to measure the voltage at the first ADC channel input
#
# Wiring:
# Connect a voltage source to the first ADC channel, in addition to the
# normal power and I2C connections. The voltage level should be between 0V/GND and VCC
#
########################################

i2c = board.I2C()
tla = TLA.TLA2024(i2c)

tla_in_0 = AnalogIn(tla, TLA.A0)
while True:
    raw_value = tla_in_0.value
    scaled_value = (raw_value / 65535) * tla_in_0.reference_voltage

    voltage = tla_in_0.voltage

    print("Pin 0 Scaled Voltage: %0.2fV" % (scaled_value))
    print("Pin 0 Direct Voltage: %0.2fV" % (voltage))
    print("")
    time.sleep(1)
