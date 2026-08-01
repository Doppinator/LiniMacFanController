from smc import SMC


class Fan:

    def __init__(self, number):
        self.number = number
        self.smc = SMC()

    @property
    def label(self):
        return self.smc.read(f"fan{self.number}_label")

    @property
    def rpm(self):
        return int(self.smc.read(f"fan{self.number}_input"))

    @property
    def minimum(self):
        return int(self.smc.read(f"fan{self.number}_min"))

    @property
    def maximum(self):
        return int(self.smc.read(f"fan{self.number}_max"))

    def __str__(self):
        return (
            f"{self.label}: "
            f"{self.rpm} RPM "
            f"(Min {self.minimum}, Max {self.maximum})"
        )