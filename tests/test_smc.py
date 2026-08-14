import tempfile
import unittest
from pathlib import Path

from LiniMacFanController.explorer.fans import Fan
from LiniMacFanController.explorer.sensors import Sensor
from LiniMacFanController.smc import SMC
from LiniMacFanController.explorer.sensors.sensor_registry import (
    SensorClassification,
    definition_for,
    select_display_sensors,
)


class SMCFixtureTestCase(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.base = Path(self.temp_dir.name)
        self._write("fan10_input", "2000\n")
        self._write("fan2_input", "1500\n")
        self._write("fan2_label", "HDD\n")
        self._write("fan2_min", "1100\n")
        self._write("fan2_max", "5500\n")
        self._write("fan2_target", "1800\n")
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
        self.assertEqual(fan.refresh, 1500)
        self.assertEqual(fan.target_rpm, 1800)

    def test_fan_target_is_optional(self):
        self.assertIsNone(Fan(10, self.smc).target_rpm)

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

    def test_classifies_known_sensors_and_hides_opaque_keys(self):
        self.assertEqual(definition_for("TC0C").name, "CPU Core")
        self.assertEqual(
            definition_for("TC1C").classification, SensorClassification.ALIAS
        )
        self.assertEqual(
            definition_for("TL0P").classification, SensorClassification.HIDDEN
        )

    def test_prefers_primary_sensor_and_uses_alias_as_a_fallback(self):
        class Reading:
            def __init__(self, key):
                self.key = key

        readings = [Reading("TC1C"), Reading("TC0C"), Reading("TG0H"), Reading("TL0P")]
        selected = select_display_sensors(readings)

        self.assertEqual([reading.key for reading in selected], ["TC0C", "TG0H"])


if __name__ == "__main__":
    unittest.main()
