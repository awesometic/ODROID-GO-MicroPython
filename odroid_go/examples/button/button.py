from odroid_go import GO
import time

GO.lcd.font(GO.lcd.FONT_Default)


def display_buttons():
    GO.lcd.clear()

    GO.lcd.text(0, 0, "/* Direction Pad */")
    GO.lcd.text(0, GO.lcd.LASTY + 16, "Joy-Y-Up: " + ("Pressed" if GO.btn_joy_y.is_axis_pressed() == 2 else ""))
    GO.lcd.text(0, GO.lcd.LASTY + 16, "Joy-Y-Down: " + ("Pressed" if GO.btn_joy_y.is_axis_pressed() == 1 else ""))
    GO.lcd.text(0, GO.lcd.LASTY + 16, "Joy-X-Left: " + ("Pressed" if GO.btn_joy_x.is_axis_pressed() == 2 else ""))
    GO.lcd.text(0, GO.lcd.LASTY + 16, "Joy-X-Right: " + ("Pressed" if GO.btn_joy_x.is_axis_pressed() == 1 else ""))
    GO.lcd.text(0, GO.lcd.LASTY + 16, "")
    GO.lcd.text(0, GO.lcd.LASTY + 16, "/* Function Key */")
    GO.lcd.text(0, GO.lcd.LASTY + 16, "Menu: " + ("Pressed" if GO.btn_menu.is_pressed() == 1 else ""))
    GO.lcd.text(0, GO.lcd.LASTY + 16, "Volume: " + ("Pressed" if GO.btn_volume.is_pressed() == 1 else ""))
    GO.lcd.text(0, GO.lcd.LASTY + 16, "Select: " + ("Pressed" if GO.btn_select.is_pressed() == 1 else ""))
    GO.lcd.text(0, GO.lcd.LASTY + 16, "Start: " + ("Pressed" if GO.btn_start.is_pressed() == 1 else ""))
    GO.lcd.text(0, GO.lcd.LASTY + 16, "")
    GO.lcd.text(0, GO.lcd.LASTY + 16, "/* Actions */")
    GO.lcd.text(0, GO.lcd.LASTY + 16, "B: " + ("Pressed" if GO.btn_b.is_pressed() == 1 else ""))
    GO.lcd.text(0, GO.lcd.LASTY + 16, "A: " + ("Pressed" if GO.btn_a.is_pressed() == 1 else ""))


while True:
    GO.update()
    display_buttons()

    time.sleep(1)
