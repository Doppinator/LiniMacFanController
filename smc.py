from pathlib import Path


class SMC:
    """Low-level interface to the Apple SMC sysfs files."""

    def __init__(self):
        self.base = self._find_base_path()

    def _find_base_path(self):
        paths = list(Path("/sys/devices/platform").glob("applesmc.*"))

        if not paths:
            raise RuntimeError("Apple SMC driver not found.")

        return paths[0]

    def read(self, filename):
        """Read a value from an SMC file."""
        path = self.base / filename

        with open(path) as f:
            return f.read().strip()

    def exists(self, filename):
        return (self.base / filename).exists()