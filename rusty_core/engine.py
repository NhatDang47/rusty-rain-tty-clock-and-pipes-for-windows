
import ctypes
import random
from ctypes import Structure, Union, c_short, c_ushort, c_wchar, byref

from rusty_core.config import PALETTES, RUNES, TAIL_LEN

class COORD(Structure): _fields_ = [("X", c_short), ("Y", c_short)]
class SMALL_RECT(Structure): _fields_ = [("Left", c_short), ("Top", c_short), ("Right", c_short), ("Bottom", c_short)]
class CHAR_UNION(Union): _fields_ = [("UnicodeChar", c_wchar), ("AsciiChar", ctypes.c_char)]
class CHAR_INFO(Structure): _fields_ = [("Char", CHAR_UNION), ("Attributes", c_ushort)]
class CSBI(Structure): 
    _fields_ = [("dwSize", COORD), ("dwCursorPosition", COORD), ("wAttributes", c_ushort), ("srWindow", SMALL_RECT), ("dwMaximumWindowSize", COORD)]

kernel32 = ctypes.windll.kernel32
h_out = kernel32.GetStdHandle(-11)

class Win32Matrix:
    def __init__(self):
        self.palette_idx = 0
        self.w, self.h = 0, 0
        self.setup()

    def setup(self):
        csbi = CSBI()
        kernel32.GetConsoleScreenBufferInfo(h_out, byref(csbi))
        self.w = csbi.srWindow.Right - csbi.srWindow.Left + 1
        self.h = csbi.srWindow.Bottom - csbi.srWindow.Top + 1
        
        self.drops = [float(random.randint(-self.h, 0)) for _ in range(self.w)]
        self.speeds = [random.uniform(0.2, 0.6) for _ in range(self.w)]
        self.buffer = (CHAR_INFO * (self.w * self.h))()
        ctypes.memset(byref(self.buffer), 0, ctypes.sizeof(self.buffer))
        
        self.rect = SMALL_RECT(0, 0, self.w - 1, self.h - 1)
        self.buf_size = COORD(self.w, self.h)
        self.coord_00 = COORD(0, 0)

    def change_palette(self, direction):
        self.palette_idx = (self.palette_idx + direction) % len(PALETTES)

    def update(self):
        _, head_col, neon_col, deep_col = PALETTES[self.palette_idx]
        
        for x in range(self.w):
            self.drops[x] += self.speeds[x]
            if self.drops[x] - TAIL_LEN > self.h:
                self.drops[x] = random.randint(-5, 0)
            
            hy = int(self.drops[x])
            if 0 <= hy < self.h:
                idx = hy * self.w + x
                self.buffer[idx].Char.UnicodeChar = random.choice(RUNES)
                self.buffer[idx].Attributes = head_col
            if 0 <= hy - 1 < self.h:
                self.buffer[(hy - 1) * self.w + x].Attributes = neon_col
            if 0 <= hy - 4 < self.h:
                self.buffer[(hy - 4) * self.w + x].Attributes = deep_col
            ty = hy - TAIL_LEN
            if 0 <= ty < self.h:
                idx = ty * self.w + x
                self.buffer[idx].Char.UnicodeChar = ' '
                self.buffer[idx].Attributes = 0

    def render(self):
        kernel32.WriteConsoleOutputW(h_out, byref(self.buffer), self.buf_size, self.coord_00, byref(self.rect))