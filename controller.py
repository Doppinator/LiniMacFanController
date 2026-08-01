class Controller:

    def __init__(self):
        self.curve = [
            (40, 1000),
            (60, 1500),
            (80, 2100),
        ]
    def get_step_rpm(self, temperature):
        for temp, rpm in self.curve:
            if temperature <= temp:
                return rpm
        return self.curve[-1][1]