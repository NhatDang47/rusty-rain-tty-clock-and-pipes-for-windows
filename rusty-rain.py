# rusty-rain.py
import msvcrt
import time
from rusty_core.engine import Win32Matrix
from rusty_core.config import SPEED, PALETTES

def main():
    engine = Win32Matrix()

    try:
        while True:
            if msvcrt.kbhit():
                key = msvcrt.getch()
                if key in [b'q', b'\x1b']: break
                if key in [b'\xe0', b'\x00']:
                    arrow = msvcrt.getch()
                    if arrow == b'M':
                        engine.change_palette(1)
                    elif arrow == b'K':
                        engine.change_palette(-1)

            engine.update()
            engine.render()
            time.sleep(SPEED)

    except KeyboardInterrupt:
        pass
    finally:
        print("\nClean up and exiting...")

if __name__ == "__main__":
    main()