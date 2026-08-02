import tempfile
import unittest
from pathlib import Path

from LiniMacFanController.Explorer.Fans import Fan
from LiniMacFanController.Explorer.Sensors import Sensor
from LiniMacFanController.SMC import SMC


class SMCFixtureTestCase(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.base = Path(self.temp_dir.name)
        self._write("fan10_input", "2000\n")
        self._write("fan2_input", "1500\n")
        self._write("fan2_label", "HDD\n")
        self._write("fan2_min", "1100\n")
        self._write("fan2_max", "5500\n")
        self._write("temp12_input", "44500\n")
        self._write("temp12_label", "TC0C\n")
        self.smc = SMC(self.base)

    def tearDown(self):
        self.temp_dir.cleanup()

    def _write(self, filename, value):
        (self.base / filename).write_text(value)

    def test_discovers_numeric_device_indexes(self):
        self.assertEqual(self.smc.fan_numbers(), [2, 10])
        self.assertEqual(self.smc.sensor_numbers(), [12])

    def test_fan_reads_values_from_shared_smc(self):
        fan = Fan(2, self.smc)
        self.assertEqual(str(fan), "HDD: 1500 RPM (Min 1100, Max 5500)")

    def test_sensor_converts_millidegrees_and_uses_friendly_name(self):
        sensor = Sensor(12, self.smc)
        self.assertEqual(sensor.name, "CPU Core")
        self.assertEqual(sensor.celsius, 44.5)
        self.assertEqual(str(sensor), "CPU Core: 44.5°C")

    def test_rejects_invalid_indexes(self):
        with self.assertRaises(ValueError):
            Fan(0, self.smc)
        with self.assertRaises(ValueError):
            Sensor(0, self.smc)


if __name__ == "__main__":
    unittest.main()
