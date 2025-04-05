from luma.core.interface.serial import i2c
from luma.oled.device import sh1106
from PIL import ImageFont


serial = i2c(port=1, address=0x3C)
device = sh1106(serial)
oled_font = ImageFont.truetype('FreeSans.ttf', 14)

