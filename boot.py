"""
An example boot.py for ODROID-GO module
"""

from odroid_go import GO

print("ODROID-GO module loaded.")


def hello():
    GO.lcd.fill(color=GO.lcd.colors.BLACK)
    GO.lcd.print("Hello, ODROID-GO!")
