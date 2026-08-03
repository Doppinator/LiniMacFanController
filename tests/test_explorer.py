import unittest

from LiniMacFanController.explorer import HardwareExplorer


class HardwareExplorerTestCase(unittest.TestCase):
    def test_is_exported_by_explorer_package(self):
        self.assertEqual(HardwareExplorer.__name__, "HardwareExplorer")


if __name__ == "__main__":
    unittest.main()
