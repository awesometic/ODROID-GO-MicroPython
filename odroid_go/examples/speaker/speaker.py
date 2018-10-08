from odroid_go import GO

GO.lcd.clear()
GO.lcd.font(GO.lcd.FONT_DejaVu24)
GO.lcd.text(0, 0, "ODROID-GO speaker test")
GO.lcd.text(0, GO.lcd.CENTER, "was_pressed: ")

GO.speaker.set_volume(30)

while True:
    GO.update()
    GO.lcd.rect(210, 110, 30, 30, color=GO.lcd.BLACK, fillcolor=GO.lcd.BLACK)

    if GO.btn_a.was_pressed():
        GO.lcd.text(210, 115, "A")
        GO.speaker.beep()

    if GO.btn_b.was_pressed():
        GO.lcd.text(210, 115, "B")
        GO.speaker.tone(3000, 2)
