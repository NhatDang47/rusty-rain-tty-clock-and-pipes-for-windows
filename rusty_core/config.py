import ctypes

FG_BLUE      = 0x0001
FG_GREEN     = 0x0002
FG_RED       = 0x0004
FG_INTENSITY = 0x0008
WHITE        = FG_RED | FG_GREEN | FG_BLUE | FG_INTENSITY

PALETTES = [
    ("Deep Sea",    WHITE, FG_BLUE | FG_INTENSITY, FG_BLUE),
    ("Classic",     WHITE, FG_GREEN | FG_INTENSITY, FG_GREEN),
    ("Cyber Hell",  WHITE, FG_RED | FG_INTENSITY, FG_RED),
    ("Synthwave",   WHITE, (FG_RED | FG_BLUE) | FG_INTENSITY, (FG_RED | FG_BLUE)),
    ("Fallout",     WHITE, (FG_RED | FG_GREEN) | FG_INTENSITY, (FG_RED | FG_GREEN))
]

SPEED = 0.04
TAIL_LEN = 15
GLITCH_RATE = 0.005

RUNES = ["0", "1", "·", "▫", ":", "."]