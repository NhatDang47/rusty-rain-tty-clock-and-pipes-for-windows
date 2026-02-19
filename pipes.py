import msvcrt
import time
import ctypes
from pipes_core.engine import Win32Circuit
from pipes_core.config import SPEED

def main():
    kernel32 = ctypes.windll.kernel32
    h_out = kernel32.GetStdHandle(-11)
    
    class CURSOR(ctypes.Structure): _fields_ = [("dwSize", ctypes.c_int), ("bVisible", ctypes.c_int)]
    kernel32.SetConsoleCursorInfo(h_out, ctypes.byref(CURSOR(1, 0)))

    engine = Win32Circuit()

    try:
        while True:
            if msvcrt.kbhit():
                key = msvcrt.getch()
                if key in [b'q', b'\x1b']: break
                if key == b'r': engine.reset_all()
                if key in [b'\xe0', b'\x00']:
                    arrow = msvcrt.getch()
                    if arrow == b'M': engine.change_palette(1)
                    elif arrow == b'K': engine.change_palette(-1)

            engine.frames_until_reset -= 1
            if engine.frames_until_reset <= 0: engine.reset_all()

            for p in engine.pipes: p.update()
            engine.render()
            time.sleep(SPEED)
            
    except KeyboardInterrupt: pass
    finally:
        kernel32.SetConsoleTextAttribute(h_out, 7)
        kernel32.SetConsoleCursorInfo(h_out, ctypes.byref(CURSOR(1, 1)))

if __name__ == "__main__":
    main()