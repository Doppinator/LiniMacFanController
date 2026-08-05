from ...smc import SMC
from .sensor_registry import KNOWN_SENSORS


class Sensor:
    """A temperature sensor exposed by the Apple SMC hwmon interface."""

    def __init__(self, number: int, smc: SMC | None = None):
        if not isinstance(number, int) or number < 1:
            raise ValueError("Sensor number must be a positive integer.")

        self.number = number
        self.smc = smc or SMC()

        self._previous_celsius: float | None = None
        self._current_celsius: float | None = None

    def _read_celsius(self) -> float:
        """Read the current temperature from the hardware."""
        return int(self.smc.read(f"temp{self.number}_input")) / 1000

    def refresh(self) -> None:
        """Refresh the cached temperature reading."""
        self._previous_celsius = self._current_celsius
        self._current_celsius = self._read_celsius()

    @property
    def key(self) -> str:
        return self.smc.read(f"temp{self.number}_label")

    @property
    def name(self) -> str:
        return KNOWN_SENSORS.get(self.key, self.key)

    @property
    def celsius(self) -> float:
        if self._current_celsius is None:
            self.refresh()

        return self._current_celsius

    @property
    def delta(self) -> float:
        if self._previous_celsius is None:
            return 0.0

        return self._current_celsius - self._previous_celsius

    @property
    def is_valid(self) -> bool:
        return self.celsius not in (-127.0, -7.0, 0.0)

    def __str__(self) -> str:
        return f"{self.name}: {self.celsius:.1f}°C"
