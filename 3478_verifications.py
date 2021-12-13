#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 17:31:43 2021

@author: robby
"""
import logging
from time import sleep
from pymeasure.instruments.hp import HP3478A
from pymeasure.log import console_log

log = logging.getLogger()
console_log(log)
log.info("Creating connection to 3478A")
meter = HP3478A("GPIB0::23")

meter.display_text = "TEST"
sleep(1)
meter.display_reset()

meter.display_text_no_symbol = "0123.456,789abc"
sleep(1)
meter.display_reset()

meter.display_text = "DCV"
for r in range(3, 6):
    meter.resolution = r
    for i in range(0, 4):
        print(meter.measure_DCV)
    print(meter.mode)
    print(meter.range)
    print(meter.resolution)
    print(meter.active_connectors)
    print(meter.auto_zero_enabled)
    print(meter.trigger)
    print(meter.SRQ_mask)

meter.display_text = "DCI"
for r in range(3, 6):
    meter.resolution = r
    for i in range(0, 4):
        print(meter.measure_DCI)
    print(meter.mode)
    print(meter.range)
    print(meter.resolution)
    print(meter.active_connectors)
    print(meter.auto_zero_enabled)
    print(meter.trigger)
    print(meter.SRQ_mask)


meter.display_text = "ACI"
for r in range(3, 6):
    meter.resolution = r
    for i in range(0, 4):
        print(meter.measure_ACI)
    print(meter.mode)
    print(meter.range)
    print(meter.resolution)
    print(meter.active_connectors)
    print(meter.auto_zero_enabled)
    print(meter.trigger)
    print(meter.SRQ_mask)


meter.display_text = "ACV"
for r in range(3, 6):
    meter.resolution = r
    for i in range(0, 4):
        print(meter.measure_ACV)
    print(meter.mode)
    print(meter.range)
    print(meter.resolution)
    print(meter.active_connectors)
    print(meter.auto_zero_enabled)
    print(meter.trigger)
    print(meter.SRQ_mask)

meter.display_text = "R2W"
for r in range(3, 6):
    meter.resolution = r
    for i in range(0, 4):
        print(meter.measure_R2W)
    print(meter.mode)
    print(meter.range)
    print(meter.resolution)
    print(meter.active_connectors)
    print(meter.auto_zero_enabled)
    print(meter.trigger)
    print(meter.SRQ_mask)

meter.display_text = "DONE"
sleep(30)
meter.shutdown()
