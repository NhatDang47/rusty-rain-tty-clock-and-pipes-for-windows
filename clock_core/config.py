import ctypes

FG_BLUE      = 0x0001
FG_GREEN     = 0x0002
FG_RED       = 0x0004
FG_INTENSITY = 0x0008
WHITE        = FG_RED | FG_GREEN | FG_BLUE | FG_INTENSITY
GRAY         = FG_INTENSITY

PALETTES = [
    ("Deep Sea",    WHITE, FG_BLUE | FG_INTENSITY),
    ("Classic",     WHITE, FG_GREEN | FG_INTENSITY),
    ("Cyber Hell",  WHITE, FG_RED | FG_INTENSITY),
    ("Synthwave",   WHITE, (FG_RED | FG_BLUE) | FG_INTENSITY),
    ("Fallout",     WHITE, (FG_RED | FG_GREEN) | FG_INTENSITY)
]

DIGITS = {
    '0': ["█████", "██ ██", "██ ██", "██ ██", "█████"],
    '1': ["  ██ ", "  ██ ", "  ██ ", "  ██ ", "  ██ "],
    '2': ["█████", "   ██", "█████", "██   ", "█████"],
    '3': ["█████", "   ██", "█████", "   ██", "█████"],
    '4': ["██ ██", "██ ██", "█████", "   ██", "   ██"],
    '5': ["█████", "██   ", "█████", "   ██", "█████"],
    '6': ["█████", "██   ", "█████", "██ ██", "█████"],
    '7': ["█████", "   ██", "   ██", "   ██", "   ██"],
    '8': ["█████", "██ ██", "█████", "██ ██", "█████"],
    '9': ["█████", "██ ██", "█████", "   ██", "█████"],
    ':': ["     ", "  ██ ", "     ", "  ██ ", "     "]
}