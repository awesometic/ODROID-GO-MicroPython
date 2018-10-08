"""
This file is executed on every boot (including wake-boot from deepsleep)

An example boot.py for ODROID-GO module
"""

from odroid_go import GO
import sys

# Code from Loboris MicroPython default boot.py
sys.path[1] = '/flash/lib'

print("\033[1;32mGO: ODROID-GO module loaded\033[1;m")
print("\033[1;32mGO: Enter \"hello()\" to see a message on the screen.\033[1;m")


def hello():
    GO.lcd.clear()
    GO.lcd.font(GO.lcd.FONT_DejaVu24, color=GO.lcd.GREEN)
    GO.lcd.text(GO.lcd.CENTER, GO.lcd.CENTER, "Hello, ODROID-GO!")
