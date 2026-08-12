

from ..smc import SMC
from .fans import Fan
from .sensors import Sensor
import os
import time

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

class HardwareExplorer:

    def __init__(self):
        self.smc = SMC()

        self.fans = []
        self.sensors = []

    def discover(self):
        self.fans.clear()
        self.sensors.clear()

        for number in self.smc.fan_numbers():
            self.fans.append(Fan(number, self.smc))

        for number in self.smc.sensor_numbers():
            sensor = Sensor(number, self.smc)
            sensor.refresh()
            if sensor.is_valid:
                self.sensors.append(sensor)

        return self

    def monitor(self, interval: float = 1.0):
        """Monitor the fans and sensors, printing their status to the console."""
        while True:
            self.refresh()
            clear_terminal()
            print(self)
            time.sleep(interval)

    def refresh(self):

        for sensor in self.sensors:
            sensor.refresh()

    def get_sorted_sensors(self):
        return sorted(
            self.sensors,
            key=lambda s: abs(s.delta),
            reverse=True,
        )

    def __str__(self):

        output = ["Fans:"]

        for fan in self.fans:
            output.append(
                f"{fan.label:<20}"
                f"{fan.rpm:>8} RPM"
                f"{fan.minimum:>8} Min"
                f"{fan.maximum:>8} Max")

        output.append("")
        output.append("Sensors:")

        for sensor in self.get_sorted_sensors():
            sensor.reset_baseline()
            output.append(
                f"{sensor.name:<20}"
                f"{sensor.celsius:>8.1f}°C"
                f"{sensor.delta:+8.1f}°C"
                f"{sensor.change_from_baseline:+8.1f}°C"
            )
        return "\n".join(output)


