import time

from LiniMacFanController import explorer
from LiniMacFanController.controller import Controller
from LiniMacFanController.explorer.fans import Fan
from LiniMacFanController.explorer.sensors import Sensor
from LiniMacFanController.smc import SMC

def main():
    smc = SMC()
    fans = [Fan(number, smc) for number in smc.fan_numbers()]
    controller = Controller()
    sensors = [Sensor(number, smc) for number in smc.sensor_numbers()]

    while True:
        explorer.discover()
        explorer.refresh()
        time.sleep(5)

if __name__ == "__main__":
    main()
