import time

from LiniMacFanController.Controller import Controller
from LiniMacFanController.Explorer.Fans import Fan
from LiniMacFanController.Explorer.Sensors import Sensor
from LiniMacFanController.SMC import SMC

def main():
    smc = SMC()
    fans = [Fan(number, smc) for number in smc.fan_numbers()]
    controller = Controller()
    sensors = [Sensor(number, smc) for number in smc.sensor_numbers()]

    while True:
        for sensor in sensors:
            temperature = sensor.celsius
            rpm = controller.get_interpolated_rpm(temperature)
            print(f"sensor {sensor.number}: {temperature:.1f}°C -> {rpm} RPM")
        time.sleep(5)

if __name__ == "__main__":
    main()
