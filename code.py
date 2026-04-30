import board
from rainbowio import colorwheel
import neopixel
import pulseio
import time

pixel_pin = board.GP5
num_pixels = 108

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.4, auto_write=False)
pulse = pulseio.PulseIn(board.GP22)


def color_chase(color, j):
    end_count = (j - 25) % (num_pixels - 1)
    print(end_count)
    print(j)
    pixels[:j] = [color] * j
    pixels[:end_count] = [((0, 0, 0))] * end_count
    pixels[j:] = [((0, 0, 0))] * (num_pixels - j)
    pixels.show()


def rainbow_cycle(j):
    for i in range(num_pixels):
        rc_index = (i * 256 // num_pixels) + (j * 20)
        pixels[i] = colorwheel(rc_index & 255)
    pixels.show()


def color_flash(color, j):
    if j % 60 == 0:
        pixels.fill(color)
        pixels.show()
    elif j % 60 == 30:
        pixels.fill((0, 0, 0))
        pixels.show()


RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)

count = 0
last_chase = 0
last_modified = 0

while True:
    if len(pulse) == 0:
        continue
    # Round length incase it is not perfect
    display = round(pulse[-1] / 20)
    if display == 1:
        pixles.fill(BLUE)
    elif display == 2:
        color_flash(BLUE, count % num_pixels)
    elif display == 3:
        pixels.fill(RED)
    elif display == 4:
        color_flash(RED, count % num_pixels)
    elif display == 5:
        pixles.fill(YELLOW)
    elif display == 6:
        color_flash(YELLOW, count % num_pixels)
    elif display == 7:
        pixles.fill(WHITE)
    elif display == 8:
        color_flash(WHITE, count)
    elif display == 9:
        rainbow_cycle(count)
    pixels.show()

    count += 1
