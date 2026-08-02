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

    def find_curve_segment(self, temperature):
        lower = None
        upper = None

        for temp, rpm in self.curve:
            if temperature <= temp:
                upper = (temp, rpm)
                break
            lower = (temp, rpm)

        return lower, upper

    def get_interpolated_rpm(self, temperature):
        lower, upper = self.find_curve_segment(temperature)

        if lower is None:
            return upper[1]
        if upper is None:
            return lower[1]

        lower_temp, lower_rpm = lower
        upper_temp, upper_rpm = upper

        # Linear interpolation formula
        slope = (upper_rpm - lower_rpm) / (upper_temp - lower_temp)
        interpolated_rpm = lower_rpm + slope * (temperature - lower_temp)

        return round(interpolated_rpm)
   

