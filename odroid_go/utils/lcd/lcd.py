'''
Initilization code refereces from:
https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo/wiki/display
'''

import machine, display, time
from micropython import const


# Define ILI9341 command constants
_RDDSDR = const(0x0f) # Read Display Self-Diagnostic Result
_SLPOUT = const(0x11) # Sleep Out
_GAMSET = const(0x26) # Gamma Set
_DISPOFF = const(0x28) # Display Off
_DISPON = const(0x29) # Display On
_CASET = const(0x2a) # Column Address Set
_PASET = const(0x2b) # Page Address Set
_RAMWR = const(0x2c) # Memory Write
_RAMRD = const(0x2e) # Memory Read
_MADCTL = const(0x36) # Memory Access Control
_VSCRSADD = const(0x37) # Vertical Scrolling Start Address
_PIXSET = const(0x3a) # Pixel Format Set
_PWCTRLA = const(0xcb) # Power Control A
_PWCRTLB = const(0xcf) # Power Control B
_DTCTRLA = const(0xe8) # Driver Timing Control A
_DTCTRLB = const(0xea) # Driver Timing Control B
_PWRONCTRL = const(0xed) # Power on Sequence Control
_PRCTRL = const(0xf7) # Pump Ratio Control
_PWCTRL1 = const(0xc0) # Power Control 1
_PWCTRL2 = const(0xc1) # Power Control 2
_VMCTRL1 = const(0xc5) # VCOM Control 1
_VMCTRL2 = const(0xc7) # VCOM Control 2
_FRMCTR1 = const(0xb1) # Frame Rate Control 1
_DISCTRL = const(0xb6) # Display Function Control
_INTFACE = const(0xf6) # Interface
_ENA3G = const(0xf2) # Enable 3G
_PGAMCTRL = const(0xe0) # Positive Gamma Control
_NGAMCTRL = const(0xe1) # Negative Gamma Control


class Lcd:
    _tft = object()

    def __init__(self, width, height, miso, mosi,
                 clk, cs, dc, speed):
        self._tft = display.TFT()
        self._tft.init(type=self._tft.ILI9341,
                       width=width, height=height,
                       miso=miso, mosi=mosi, clk=clk, cs=cs, dc=dc,
                       speed=speed,
                       color_bits=self._tft.COLOR_BITS16,
                       rot=self._tft.LANDSCAPE_FLIP)

        # Send initialization commands
        for command, data in (
            (_RDDSDR, b"\x03\x80\x02"),
            (_PWCRTLB, b"\x00\xcf\x30"),
            (_PWRONCTRL, b"\x64\x03\x12\x81"),
            (_DTCTRLA, b"\x85\x00\x78"),
            (_PWCTRLA, b"\x39\x2c\x00\x34\x02"),
            (_PRCTRL, b"\x20"),
            (_DTCTRLB, b"\x00\x00"),
            (_PWCTRL1, b"\x1b"),
            (_PWCTRL2, b"\x12"),
            (_VMCTRL1, b"\x3e\x3c"),
            (_VMCTRL2, b"\x91"),
            (_MADCTL, b"\xa8"),
            #(_MADCTL, b"\x08"),
            (_PIXSET, b"\x55"),
            (_FRMCTR1, b"\x00\x1b"),
            (_DISCTRL, b"\x0a\xa2\x27"),
            (_INTFACE, b"\x01\x30"),
            (_ENA3G, b"\x00"),
            (_GAMSET, b"\x01"),
            (_PGAMCTRL, b"\x0f\x31\x2b\x0c\x0e\x08\x4e\xf1\x37\x07\x10\x03\x0e\x09\x00"),
            (_NGAMCTRL, b"\x00\x0e\x14\x03\x11\x07\x31\xc1\x48\x08\x0f\x0c\x31\x36\x0f")):
            self._tft.tft_writecmddata(command, data)

    def get_tft_object(self):
        return self._tft
