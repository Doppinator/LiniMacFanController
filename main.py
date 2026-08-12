from LiniMacFanController.monitor import monitor

from LiniMacFanController.explorer import HardwareExplorer



def main():
    explorer = HardwareExplorer()

    explorer.discover()

    explorer.monitor(interval=1.0)

if __name__ == "__main__":
    main()
