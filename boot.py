"""
An example boot.py for ODROID-GO module
"""

from odroid_go import GO

print("\033[1;32mGO: ODROID-GO module loaded\033[1;m")
print("\033[1;32mGO: Enter \"hello()\" to see a message on the screen.\033[1;m")


def hello():
    GO.lcd.fill(color=GO.lcd.colors.BLACK)
    GO.lcd.set_font(GO.lcd.fonts.TT32)
    GO.lcd.set_color(fg=GO.lcd.colors.GREEN, bg=GO.lcd.colors.BLACK)
    GO.lcd.print("Hello, ODROID-GO!")
