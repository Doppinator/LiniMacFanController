from pathlib import Path
import re


class SMC:
    """Low-level interface to the Apple SMC sysfs files."""

    def __init__(self, base_path=None):
        """Create an SMC interface, optionally rooted at a test/device path."""
        self.base = Path(base_path) if base_path is not None else self._find_base_path()

        if not self.base.is_dir():
            raise RuntimeError(f"Apple SMC path does not exist: {self.base}")

    def _find_base_path(self):
        paths = sorted(Path("/sys/devices/platform").glob("applesmc.*"))

        if not paths:
            raise RuntimeError("Apple SMC driver not found.")

        return paths[0]

    def read(self, filename):
        """Read a value from an SMC file."""
        return (self.base / filename).read_text().strip()

    def exists(self, filename):
        return (self.base / filename).exists()

    def fan_numbers(self):
        """Return the fan numbers exposed by the driver, in numeric order."""
        return self._numbers_for("fan", "input")

    def sensor_numbers(self):
        """Return the temperature-sensor numbers exposed by the driver."""
        return self._numbers_for("temp", "input")

    def _numbers_for(self, prefix, suffix):
        pattern = re.compile(rf"{re.escape(prefix)}(\d+)_{re.escape(suffix)}")
        return sorted(
            int(match.group(1))
            for path in self.base.iterdir()
            if (match := pattern.fullmatch(path.name))
        )
