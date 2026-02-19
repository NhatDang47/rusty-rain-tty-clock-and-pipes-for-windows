import ctypes
import random
from ctypes import Structure, Union, c_short, c_ushort, c_wchar, byref
from .config import *

class COORD(Structure): _fields_ = [("X", c_short), ("Y", c_short)]
class SMALL_RECT(Structure): _fields_ = [("Left", c_short), ("Top", c_short), ("Right", c_short), ("Bottom", c_short)]
class CHAR_UNION(Union): _fields_ = [("UnicodeChar", c_wchar), ("AsciiChar", ctypes.c_char)]
class CHAR_INFO(Structure): _fields_ = [("Char", CHAR_UNION), ("Attributes", c_ushort)]
class CSBI(Structure): 
    _fields_ = [("dwSize", COORD), ("dwCursorPosition", COORD), ("wAttributes", c_ushort), ("srWindow", SMALL_RECT), ("dwMaximumWindowSize", COORD)]

kernel32 = ctypes.windll.kernel32
h_out = kernel32.GetStdHandle(-11)

class Weaver:
    def __init__(self, engine):
        self.engine = engine
        self.reset()

    def reset(self, master=None):
        self.active = True
        self.master = master
        if self.master:
            self.dir = self.master.dir
            self.x, self.y = self.master.x, self.master.y
            if self.dir in ['u', 'd']: self.x += 1
            else: self.y += 1
            self.palette = self.master.palette
        else:
            self.x = random.randint(2, self.engine.w - 5)
            self.y = random.randint(2, self.engine.h - 5)
            self.dir = random.choice(['u', 'd', 'l', 'r'])

            current_sets = PALETTES[self.engine.palette_idx][1]
            self.palette = random.choice(current_sets)
        
        self.color_idx = random.randint(0, len(self.palette) - 1)
        self.step_count = 0

    def update(self):
        self.step_count += 1
        if self.step_count > COLOR_SPEED:
            self.step_count = 0
            self.color_idx = (self.color_idx + 1) % len(self.palette)
        
        old_dir = self.dir
        if self.master and random.random() < 0.95:
            self.dir = self.master.dir
        elif random.random() < TURN_CHANCE:
            if self.dir in ['u', 'd']: self.dir = random.choice(['l', 'r'])
            else: self.dir = random.choice(['u', 'd'])

        nx, ny = self.x, self.y
        if self.dir == 'u': ny -= 1
        elif self.dir == 'd': ny += 1
        elif self.dir == 'l': nx -= 1
        elif self.dir == 'r': nx += 1

        if not (0 <= nx < self.engine.w and 0 <= ny < self.engine.h):
            self.reset(self.master)
            return

        idx = self.y * self.engine.w + self.x
        existing = self.engine.buffer[idx].Char.UnicodeChar
        char = STYLE_THIN.get((old_dir, self.dir), '┼')
        
        if (self.dir in ['u', 'd'] and existing == '─') or (self.dir in ['l', 'r'] and existing == '│'):
            char = '┼'

        self.engine.buffer[idx].Char.UnicodeChar = char
        self.engine.buffer[idx].Attributes = self.palette[self.color_idx]
        self.x, self.y = nx, ny

class Win32Circuit:
    def __init__(self):
        self.palette_idx = 0
        self.setup()

    def setup(self):
        csbi = CSBI()
        kernel32.GetConsoleScreenBufferInfo(h_out, byref(csbi))
        self.w = csbi.srWindow.Right - csbi.srWindow.Left + 1
        self.h = csbi.srWindow.Bottom - csbi.srWindow.Top + 1
        self.buffer = (CHAR_INFO * (self.w * self.h))()
        ctypes.memset(byref(self.buffer), 0, ctypes.sizeof(self.buffer))
        self.rect = SMALL_RECT(0, 0, self.w - 1, self.h - 1)
        self.buf_size = COORD(self.w, self.h)
        self.coord_00 = COORD(0, 0)
        
        self.pipes = []
        for _ in range(NUM_PAIRS):
            m = Weaver(self); self.pipes.append(m)
            if random.random() < 0.7: self.pipes.append(Weaver(self)) # Slave
            
        self.frames_until_reset = random.randint(MIN_FRAMES, MAX_FRAMES)

    def change_palette(self, dir):
        self.palette_idx = (self.palette_idx + dir) % len(PALETTES)
        self.reset_all()

    def reset_all(self):
        ctypes.memset(byref(self.buffer), 0, ctypes.sizeof(self.buffer))
        for p in self.pipes: p.reset()
        self.frames_until_reset = random.randint(MIN_FRAMES, MAX_FRAMES)

    def render(self):
        kernel32.WriteConsoleOutputW(h_out, byref(self.buffer), self.buf_size, self.coord_00, byref(self.rect))