import time
import os

from LiniMacFanController.explorer import HardwareExplorer

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    explorer = HardwareExplorer()

    explorer.discover()

    while True:
        explorer.refresh()

        clear_terminal()

        print(explorer)

        time.sleep(1)

if __name__ == "__main__":
    main()
