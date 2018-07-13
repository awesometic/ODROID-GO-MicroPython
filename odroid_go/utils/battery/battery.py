"""
A simple battery module for Micropython, only for ODROID-GO (ESP32).

Created on: 2018. 7. 13
Author: Joshua Yang (joshua.yang@hardkernel.com)
"""

from machine import Pin, ADC


class Battery:
    """
    TODO: Have to calibrate the results voltage using Vref on efuse.
    But the necessary functions seem not to be implemented to MicroPython yet.
      * esp_adc_cal_characterize()
      * esp_adc_cal_raw_to_voltage()

    This module calculate current battery voltage roughly for now.
    """

    _adc1_pin = object()
    _battery_resistance_num = 0

    def __init__(self, pin, resistance_num, width, atten):
        self._adc1_pin = ADC(Pin(pin))
        self._adc1_pin.width(width)
        self._adc1_pin.atten(atten)

        self._battery_resistance_num = resistance_num

    def get_voltage(self):
        return self._adc1_pin.read() * self._battery_resistance_num
