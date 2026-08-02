from fan import Fan
import fan
from smc import SMC
from sensor import Sensor
from controller import Controller
import time

def main():

    smc = SMC()
    fans = [Fan(number, smc) for number in smc.fan_numbers()]
    controller = Controller()
    sensor = Sensor(1, smc)  # Assuming sensor number 1 is the CPU temperature sensor

    while True:
        for sensor in [sensor]:
            temperature = sensor.celsius
            rpm = controller.get_interpolated_rpm(temperature)
            print(f"sensor {sensor.number}: {temperature:.1f}°C -> {rpm} RPM")
        time.sleep(5)  

if __name__ == "__main__":
    main()
