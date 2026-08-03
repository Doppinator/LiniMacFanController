"""Objects used to explore the fans and sensors exposed by the SMC."""

from .fans import Fan
from .explorer import HardwareExplorer
from .sensors import Sensor

__all__ = ["Fan", "HardwareExplorer", "Sensor"]
