import time

from LiniMacFanController.explorer import HardwareExplorer

def main():
    explorer = HardwareExplorer()

    explorer.discover()

    while True:
        explorer.refresh()
        print(explorer)
        time.sleep(5)

if __name__ == "__main__":
    main()
