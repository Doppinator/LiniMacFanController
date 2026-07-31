from pathlib import Path


class SMC:
    def __init__(self):
        self.base = self.find_applesmc()

    def find_applesmc(self):
        paths = list(Path("/sys/devices/platform").glob("applesmc.*"))

        if not paths:
            raise RuntimeError("Apple SMC not found.")

        return paths[0]

    def read(self, filename):
        with open(self.base / filename) as f:
            return f.read().strip()