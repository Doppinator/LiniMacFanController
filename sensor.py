from smc import SMC


class SensorReader:
    """Placeholder sensor reader for SMC-backed monitoring data."""

    def __init__(self, smc: SMC):
        self.smc = smc

    def read_temperature(self, sensor_name: str) -> float:
        raise NotImplementedError("Temperature reading logic will be implemented here.")
