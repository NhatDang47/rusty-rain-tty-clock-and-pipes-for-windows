import msvcrt
import time
import ctypes
from ctypes import byref, Structure, c_int
from clock_core.engine import Win32Clock

class CONSOLE_CURSOR_INFO(Structure):
    _fields_ = [("dwSize", c_int), ("bVisible", c_int)]

def main():
    kernel32 = ctypes.windll.kernel32
    h_std = kernel32.GetStdHandle(-11)
    
    cursor_info = CONSOLE_CURSOR_INFO(1, 0)
    kernel32.SetConsoleCursorInfo(h_std, byref(cursor_info))
    
    engine = Win32Clock()

    try:
        while True:
            if msvcrt.kbhit():
                key = msvcrt.getch()
                if key in [b'q', b'\x1b', b'\x03']: break
                if key in [b'\xe0', b'\x00']:
                    arrow = msvcrt.getch()
                    if arrow == b'M': engine.change_palette(1)
                    elif arrow == b'K': engine.change_palette(-1)

            engine.draw()
            engine.render()
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        pass
    finally:
        cursor_info.bVisible = 1
        kernel32.SetConsoleCursorInfo(h_std, byref(cursor_info))
        kernel32.SetConsoleTextAttribute(h_std, 7)
        print("\nClock stopped.")

if __name__ == "__main__":
    main()