

from LiniMacFanController.explorer.sensors import sensor

from LiniMacFanController.explorer.sensors import sensor

from ..smc import SMC
from .fans import Fan
from .sensors import Sensor

class HardwareExplorer:

    def __init__(self):
        self.smc = SMC()
        self.fans = []
        self.sensors = []
    def refresh(self):
        ...

    def __str__(self):
        ...

    def discover(self):
        for fan_number in self.smc.fan_numbers():
            self.fans.append(Fan(fan_number, self.smc))
        for sensor_number in self.smc.sensor_numbers():
            sensor = Sensor(sensor_number, self.smc)
            if sensor.is_valid():
                self.sensors.append(sensor)
        self.refresh()
        return self

    def __str__(self) -> str:
        fan_str = "\n".join(str(fan) for fan in self.fans)
        sensor_str = "\n".join(str(sensor) for sensor in self.sensors)
        return f"Fans:\n{fan_str}\n\nSensors:\n{sensor_str}"
