from ...smc import SMC
from .sensor_registry import SensorClassification, definition_for


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
        self._baseline_celsius = self._current_celsius

    @property
    def key(self) -> str:
        return self.smc.read(f"temp{self.number}_label")

    @property
    def name(self) -> str:
        return self.definition.name

    @property
    def definition(self):
        """The display classification assigned to this SMC key."""
        return definition_for(self.key)

    @property
    def is_displayable(self) -> bool:
        return self.definition.classification is not SensorClassification.HIDDEN

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
    def change_from_baseline(self):
        return self._current_celsius - self._baseline_celsius

    def reset_baseline(self):
        self._baseline_celsius = self._current_celsius

    def format_delta(delta: float) -> str:
        if abs(delta) < 0.05:
            return "   0.0°C"
        return f"{delta:+7.1f}°C"

    @property
    def is_valid(self) -> bool:
        return self.celsius not in (-127.0, -7.0, 0.0)

    def __str__(self) -> str:
        return f"{self.name}: {self.celsius:.1f}°C"
