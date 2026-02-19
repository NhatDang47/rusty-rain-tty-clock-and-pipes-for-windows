import ctypes
import time
from ctypes import Structure, Union, c_short, c_ushort, c_wchar, byref
from .config import PALETTES, DIGITS, GRAY

class COORD(Structure): _fields_ = [("X", c_short), ("Y", c_short)]
class SMALL_RECT(Structure): _fields_ = [("Left", c_short), ("Top", c_short), ("Right", c_short), ("Bottom", c_short)]
class CHAR_UNION(Union): _fields_ = [("UnicodeChar", c_wchar), ("AsciiChar", ctypes.c_char)]
class CHAR_INFO(Structure): _fields_ = [("Char", CHAR_UNION), ("Attributes", c_ushort)]
class CSBI(Structure): 
    _fields_ = [("dwSize", COORD), ("dwCursorPosition", COORD), ("wAttributes", c_ushort), ("srWindow", SMALL_RECT), ("dwMaximumWindowSize", COORD)]

kernel32 = ctypes.windll.kernel32
h_out = kernel32.GetStdHandle(-11)

class Win32Clock:
    def __init__(self):
        self.palette_idx = 0
        self.w, self.h = 0, 0
        self.setup()

    def setup(self):
        csbi = CSBI()
        kernel32.GetConsoleScreenBufferInfo(h_out, byref(csbi))
        self.w = csbi.srWindow.Right - csbi.srWindow.Left + 1
        self.h = csbi.srWindow.Bottom - csbi.srWindow.Top + 1
        self.buffer = (CHAR_INFO * (self.w * self.h))()
        self.rect = SMALL_RECT(0, 0, self.w - 1, self.h - 1)
        self.buf_size = COORD(self.w, self.h)
        self.coord_00 = COORD(0, 0)

    def write_str(self, x, y, string, attr):
        for i, char in enumerate(string):
            if 0 <= y < self.h and 0 <= x + i < self.w:
                idx = y * self.w + (x + i)
                self.buffer[idx].Char.UnicodeChar = char
                self.buffer[idx].Attributes = attr

    def change_palette(self, direction):
        self.palette_idx = (self.palette_idx + direction) % len(PALETTES)

    def draw(self):
        csbi = CSBI()
        kernel32.GetConsoleScreenBufferInfo(h_out, byref(csbi))
        nw = csbi.srWindow.Right - csbi.srWindow.Left + 1
        nh = csbi.srWindow.Bottom - csbi.srWindow.Top + 1
        if nw != self.w or nh != self.h:
            self.setup()

        ctypes.memset(byref(self.buffer), 0, ctypes.sizeof(self.buffer))
        _, head_attr, accent_attr = PALETTES[self.palette_idx]
        
        now = time.localtime()
        time_str = time.strftime("%H:%M:%S", now)
        date_str = time.strftime(">> %Y.%m.%d [%A] <<", now).upper()
    
        clock_w = len(time_str) * 6 - 1
        start_x = (self.w - clock_w) // 2
        start_y = (self.h - 5) // 2

        curr_x = start_x
        for char in time_str:
            glyph = DIGITS[char]
            for r_idx, r_str in enumerate(glyph):
                self.write_str(curr_x, start_y + r_idx, r_str, accent_attr)
            curr_x += 6

        date_x = (self.w - len(date_str)) // 2
        self.write_str(date_x, start_y + 8, date_str, GRAY)

    def render(self):
        kernel32.WriteConsoleOutputW(h_out, byref(self.buffer), self.buf_size, self.coord_00, byref(self.rect))