from smc import SMC


class FanController:
    """Placeholder controller for managing Apple fan behavior."""

    def __init__(self, smc: SMC):
        self.smc = smc

    def list_fans(self):
        return []

    def set_speed(self, fan_id: int, speed: int) -> None:
        raise NotImplementedError("Fan control logic will be implemented here.")
