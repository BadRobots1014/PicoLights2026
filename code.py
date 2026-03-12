import board
import neopixel
import pulseio

pixel_pin = board.GP5
num_pixels = 3

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=1, auto_write=False)
pulse = pulseio.PulseIn(board.DP3, 5)

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)

while True:
    if len(pulse) == 0:
        continue
    display = round(pulse[-1]/20)
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
