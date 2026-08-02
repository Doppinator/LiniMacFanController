"""Objects used to explore the fans and sensors exposed by the SMC."""

from .fans import Fan
from .explorer import hardware_explorer
from .sensors import Sensor

__all__ = ["Fan", "Sensor", "hardware_explorer"]
