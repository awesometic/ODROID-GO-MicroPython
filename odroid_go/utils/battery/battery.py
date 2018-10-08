"""
A simple battery module for Micropython, only for ODROID-GO (ESP32).

Created on: 2018. 7. 13
Author: Joshua Yang (joshua.yang@hardkernel.com)
"""

from machine import Pin, ADC

class Battery:
    _adc1_pin = object()
    _battery_resistance_num = 0
    _samples = 0
    _battery_vmax = 0
    _battery_vmin = 0

    def __init__(self, pin, resistance_num, samples, vmax, vmin, width, atten):
        self._adc1_pin = ADC(Pin(pin))
        self._adc1_pin.width(width)
        self._adc1_pin.atten(atten)

        self._battery_resistance_num = resistance_num
        self._samples = samples
        self._battery_vmax = vmax
        self._battery_vmin = vmin

    def get_voltage(self):
        reading = 0
        for _ in range(0, self._samples):
            reading += self._adc1_pin.read()

        reading /= self._samples

        return reading * self._battery_resistance_num / 1000

    def get_percentage(self):
        res = 101 - (101 / pow(1 + pow(1.33 * (self.get_voltage() * 100 - self._battery_vmin) / (self._battery_vmax - self._battery_vmin), 4.5), 3))

        if res >= 100:
            res = 100
        
        return res
