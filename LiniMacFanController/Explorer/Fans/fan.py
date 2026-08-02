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
    def refresh(self) -> int:
        return int(self.smc.read(f"fan{self.number}_speed"))

    @property
    def set_rpm(self, rpm: int):
        self.smc.write(f"fan{self.number}_target", str(rpm))
    
    def __str__(self) -> str:
        return f"{self.label}: {self.rpm} RPM (Min {self.minimum}, Max {self.maximum})"
