#Jacob Sexton 7/8/25

from adafruit_circuitplayground import cp

NOTES = {
    "C4": 262,
    "D4": 294,
    "E4": 330,
    "G4": 392
}

COLORS = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0)
}

def fill_pixels(color_tuple):
    cp.pixels.fill(color_tuple)
    cp.pixels.show()

while True:
    if cp.touch_A1:
        cp.start_tone(NOTES["C4"])
        fill_pixels(COLORS["red"])
    elif cp.touch_A3:
        cp.start_tone(NOTES["D4"])
        fill_pixels(COLORS["green"])
    elif cp.touch_A4:
        cp.start_tone(NOTES["E4"])
        fill_pixels(COLORS["blue"])
    elif cp.touch_A6:
        cp.start_tone(NOTES["G4"])
        fill_pixels(COLORS["yellow"])
    else:
        cp.stop_tone()
        cp.pixels.fill((0, 0, 0))
        cp.pixels.show()
