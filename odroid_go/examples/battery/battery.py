from odroid_go import GO
import time

GO.lcd.font(GO.lcd.FONT_DejaVu18)


def show_battery_status():
    GO.lcd.clear()
    GO.lcd.text(0, GO.lcd.CENTER, "Current Voltage: " + str(GO.battery.get_voltage()))
    GO.lcd.text(0, GO.lcd.LASTY + 18, "Current Percentage: " + str(round(GO.battery.get_percentage())))


while True:
    show_battery_status()

    time.sleep(1)
