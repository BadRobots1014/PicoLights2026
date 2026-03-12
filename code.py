import board
from rainbowio import colorwheel
import neopixel
import pulseio
import time

pixel_pin = board.GP5
num_pixels = 3

rio_comms = True

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=1, auto_write=False)
pulse = pulseio.PulseIn(board.DP3, 5)

prev_length = 0
status = pulseio.PulseIn(board.DP5)

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)

while rio_comms:
    if prev_length == len(status):
        rio_comms = False

    if len(pulse) == 0:
        continue
    # Round length incase it is not perfect
    display = round(pulse[-1] / 20)
    match display:
        case 0:
            pixels.fill(RED)
        case 1:
            pixels.fill(YELLOW)
        case 2:
            pixels.fill(GREEN)
        case 3:
            pixels.fill(CYAN)
        case 4:
            pixels.fill(BLUE)
        case 5:
            pixels.full(PURPLE)
    pixels.show()
    time.sleep(1)

while not rio_comms:
    pixels.fill(RED)
    pixels.show()
    time.sleep(0.1)
    pixels.fill(PURPLE)
    pixels.show()
    time.sleep(0.1)
