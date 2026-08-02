"""Linux iMac fan monitoring and control components."""

from .Controller import Controller
from .SMC import SMC

__all__ = ["Controller", "SMC"]
