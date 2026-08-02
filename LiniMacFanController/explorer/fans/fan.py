from ...smc import SMC


class Fan:
    """A fan exposed by the Apple SMC hwmon interface."""

    def __init__(self, number: int, smc: SMC | None = None):
        if not isinstance(number, int) or number < 1:
            raise ValueError("Fan number must be a positive integer.")

        self.number = number
        self.smc = smc or SMC()

    @property
    def label(self) -> str:
        return self.smc.read(f"fan{self.number}_label")

    @property
    def rpm(self) -> int:
        return int(self.smc.read(f"fan{self.number}_input"))

    @property
    def minimum(self) -> int:
        return int(self.smc.read(f"fan{self.number}_min"))

    @property
    def maximum(self) -> int:
        return int(self.smc.read(f"fan{self.number}_max"))

    @property
    def target_rpm(self) -> int | None:
        """Return the requested fan speed when the driver exposes one.

        ``fanN_target`` is optional in the Linux hwmon interface, so callers
        can distinguish an unsupported target from a real RPM value.
        """
        filename = f"fan{self.number}_target"
        return int(self.smc.read(filename)) if self.smc.exists(filename) else None

    @property
    def refresh(self) -> int:
        """Return a fresh reading of the current fan speed.

        Kept as a convenience alias for callers that used the old API.
        """
        return self.rpm

    def __str__(self) -> str:
        return f"{self.label}: {self.rpm} RPM (Min {self.minimum}, Max {self.maximum})"
