import board
from rainbowio import colorwheel
import neopixel
import pulseio
import time

pixel_pin = board.GP5
num_pixels = 108

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.4, auto_write=False)
pulse = pulseio.PulseIn(board.GP22, 5)

def color_chase(color, wait):
    for i in range(num_pixels):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
    time.sleep(0.5)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = colorwheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)

def color_flash(color, wait):
    pixels.fill(color)
    pixels.show()
    time.sleep(wait)
    pixels.fill((0, 0, 0))
    pixels.show()
    time.sleep(wait)

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)

while True:
    if len(pulse) == 0:
        continue
    # Round length incase it is not perfect
    display = round(pulse[-1]/20)
    print(display)
    if display == 1:
        pixels.fill(RED)
    elif display == 2:
        pixels.fill(YELLOW)
    elif display == 3:
        pixels.fill(GREEN)
    elif display == 4:
        pixels.fill(CYAN)
    elif display == 5:
        pixels.fill(BLUE)
    elif display == 6:
        pixels.fill(PURPLE)
    pixels.show()