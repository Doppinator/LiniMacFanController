from ...smc import SMC


class Sensor:
    """A temperature sensor exposed by the Apple SMC hwmon interface."""

    sensor_names = {
        "TC0C": "CPU Core",
        "TG0D": "GPU Diode",
        "TPCD": "Power Supply",
    }

    def __init__(self, number: int, smc: SMC | None = None):
        if not isinstance(number, int) or number < 1:
            raise ValueError("Sensor number must be a positive integer.")

        self.number = number
        self.smc = smc or SMC()
    
    def is_valid(self) -> bool:
        return self.celsius not in (-127.0, -7.0, 0.0)

    @property
    def key(self) -> str:
        return self.smc.read(f"temp{self.number}_label")

    @property
    def name(self) -> str:
        return self.sensor_names.get(self.key, self.key)

    @property
    def celsius(self) -> float:
        """Temperature in degrees Celsius (sysfs stores millidegrees)."""
        return int(self.smc.read(f"temp{self.number}_input")) / 1000

    def __str__(self) -> str:
        return f"{self.name}: {self.celsius:.1f}°C"
