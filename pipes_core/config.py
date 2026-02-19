import ctypes

FG_BLUE      = 0x0001
FG_GREEN     = 0x0002
FG_RED       = 0x0004
FG_INTENSITY = 0x0008
WHITE        = FG_RED | FG_GREEN | FG_BLUE | FG_INTENSITY

ICE_COLORS  = [0x0001 | 0x0008, 0x0001 | 0x0002, 0x0001 | 0x0002 | 0x0008, WHITE]
FIRE_COLORS = [0x0004 | 0x0008, 0x0004 | 0x0001 | 0x0008, 0x0004 | 0x0002 | 0x0008, 0x0004 | 0x0001]

PALETTES = [
    ("Elemental (Default)", [ICE_COLORS, FIRE_COLORS]), 
    ("Classic Matrix",      [[0x0002 | 0x0008, 0x0002, WHITE]]),
    ("Cyber Hell",          [[0x0004 | 0x0008, 0x0004, 0x0004 | 0x0001 | 0x0008]]),
    ("Synthwave",           [[0x0001 | 0x0004 | 0x0008, 0x0001 | 0x0008, WHITE]]),
    ("Fallout",             [[0x0002 | 0x0004 | 0x0008, 0x0002 | 0x0004]])
]

STYLE_THIN = {
    ('u','u'): '│', ('d','d'): '│', ('l','l'): '─', ('r','r'): '─',
    ('r','d'): '┐', ('r','u'): '┘', ('l','d'): '┌', ('l','u'): '└',
    ('u','r'): '┌', ('u','l'): '┐', ('d','r'): '└', ('d','l'): '┘',
    'cross': '┼'
}

SPEED = 0.04
NUM_PAIRS = 6
TURN_CHANCE = 0.06
COLOR_SPEED = 2
MIN_FRAMES = 100
MAX_FRAMES = 300