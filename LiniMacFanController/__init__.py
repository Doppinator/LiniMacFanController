"""Linux iMac fan monitoring and control components."""

from .controller import Controller
from .smc import SMC

__all__ = ["Controller", "SMC"]
