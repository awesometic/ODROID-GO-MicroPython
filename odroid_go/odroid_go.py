from machine import Pin, SPI, ADC
from .utils import *


class ODROID_GO:
    """
    Class for helping to code with ODROID-GO.
    """

    def __init__(self):
        self._init_lcd()
        self._init_buttons()
        self._init_speaker()
        self._init_battery()

    def _init_lcd(self):
        self.lcd = Lcd(width=TFT_WIDTH, height=TFT_HEIGHT,
                       miso=TFT_MISO_PIN, mosi=TFT_MOSI_PIN, clk=TFT_SCLK_PIN,
                       cs=TFT_CS_PIN, dc=TFT_DC_PIN, speed=TFT_SPI_SPEED)
        self.lcd = self.lcd.get_tft_object()
        Pin(TFT_LED_PIN, Pin.OUT).value(1)

    def _init_buttons(self):
        self.btn_joy_x = Button(BUTTON_JOY_X_PIN, True, BUTTON_DEBOUNCE_MS)
        self.btn_joy_y = Button(BUTTON_JOY_Y_PIN, True, BUTTON_DEBOUNCE_MS)
        self.btn_menu = Button(BUTTON_MENU_PIN, True, BUTTON_DEBOUNCE_MS)
        self.btn_volume = Button(BUTTON_VOLUME_PIN, True, BUTTON_DEBOUNCE_MS)
        self.btn_select = Button(BUTTON_SELECT_PIN, True, BUTTON_DEBOUNCE_MS)
        self.btn_start = Button(BUTTON_START_PIN, True, BUTTON_DEBOUNCE_MS)
        self.btn_a = Button(BUTTON_A_PIN, True, BUTTON_DEBOUNCE_MS)
        self.btn_b = Button(BUTTON_B_PIN, True, BUTTON_DEBOUNCE_MS)

    def _init_speaker(self):
        self.speaker = Speaker(SPEAKER_PIN, SPEAKER_DAC_PIN)

    def _init_battery(self):
        self.battery = Battery(BATTERY_PIN, BATTERY_RESISTANCE_NUM,
                               BATTERY_SAMPLES, BATTERY_VMAX, BATTERY_VMIN,
                               ADC.WIDTH_12BIT, ADC.ATTN_11DB)

    def begin(self):
        self.speaker.set_volume(0.1)
        self.speaker.set_beep(262, 1)

    def update(self):
        self.btn_joy_x.read_axis()
        self.btn_joy_y.read_axis()
        self.btn_menu.read()
        self.btn_volume.read()
        self.btn_select.read()
        self.btn_start.read()
        self.btn_a.read()
        self.btn_b.read()


GO = ODROID_GO()
GO.begin()
