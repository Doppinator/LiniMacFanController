import unittest

from LiniMacFanController.explorer import hardware_explorer


class HardwareExplorerTestCase(unittest.TestCase):
    def test_returns_expected_system_fields(self):
        info = hardware_explorer()

        self.assertEqual(
            set(info),
            {
                "System",
                "Node Name",
                "Release",
                "Version",
                "Machine",
                "Processor",
                "CPU Cores",
                "Logical CPUs",
                "RAM Size",
            },
        )
        self.assertIsInstance(info["RAM Size"], float)


if __name__ == "__main__":
    unittest.main()
