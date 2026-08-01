from smc import SMC


class Sensor:
    """A temperature sensor exposed by the Apple SMC hwmon interface."""

    sensor_names = {
        "TC0C": "CPU Core",
        "TG0D": "GPU Diode",
        "TPCD": "Power Supply",
    }

    def __init__(self, number, smc=None):
        if not isinstance(number, int) or number < 1:
            raise ValueError("Sensor number must be a positive integer.")

        self.number = number
        self.smc = smc or SMC()

    @property
    def key(self):
        return self.smc.read(f"temp{self.number}_label")

    @property
    def name(self):
        return self.sensor_names.get(self.key, self.key)

    @property
    def celsius(self):
        """Temperature in degrees Celsius (sysfs stores millidegrees)."""
        return int(self.smc.read(f"temp{self.number}_input")) / 1000

    def __str__(self):
        return f"{self.name}: {self.celsius:.1f}°C"
