class HardwareExplorer:

    def __init__(self):
        self.smc = SMC()
        self.fans = []
        self.sensors = []
    def refresh(self):
        ...

    def __str__(self):
        ...

    def discover(self):
        self.refresh()
        return self