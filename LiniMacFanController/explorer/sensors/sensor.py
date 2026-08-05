from ...smc import SMC
from .sensor_registry import KNOWN_SENSORS


class Sensor:
    """A temperature sensor exposed by the Apple SMC hwmon interface."""


    def __init__(self, number: int, smc: SMC | None = None):
        if not isinstance(number, int) or number < 1:
            raise ValueError("Sensor number must be a positive integer.")

        self.number = number
        self.smc = smc or SMC()
        self._celsius: float | None = None
        self._delta = 0.0
        self._previous_celsius: float | None = None
        self._current_celsius: float | None = None
        
    @property
    def is_valid(self) -> bool:
        return self.celsius not in (-127.0, -7.0, 0.0)

    @property
    def key(self) -> str:
        return self.smc.read(f"temp{self.number}_label")

    @property
    def name(self) -> str:
        return KNOWN_SENSORS.get(self.key, self.key)

    @property
    def celsius(self) -> float:
        """Temperature in degrees Celsius (sysfs stores millidegrees)."""
        return int(self.smc.read(f"temp{self.number}_input")) / 1000

    def _read_celsius(self):
        """Read the current temperature in degrees Celsius."""
        return self.celsius
        
    def refresh(self):
        self._previous_celsius = self._current_celsius
        self._current_celsius = self._read_celsius()


    @property
    def delta(self):
        if self._previous_celsius is None or self._current_celsius is None:
            return 0.0
        return self._current_celsius - self._previous_celsius

    def __str__(self) -> str:
        return f"{self.name}: {self.celsius:.1f}°C"
