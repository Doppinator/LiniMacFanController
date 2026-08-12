from ..smc import SMC
from .fans import Fan
from .sensors import Sensor


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

    def refresh(self):

        for sensor in self.sensors:
            sensor.refresh()

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

        for sensor in self.sensors:

            output.append(
                f"{sensor.name:<20}"
                f"{sensor.celsius:>8.1f}°C"
                f"{sensor.delta:+8.1f}°C"
            )

        return "\n".join(output)
