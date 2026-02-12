"""
Animotion - A creative alternative to tqdm with terminal animations
Author: Eduardo J. Barrios (edujbarrios)
"""

from .core import animate
from .animator import Animator
from .styles import AnimationStyle

__version__ = "1.0.0"
__author__ = "Eduardo J. Barrios"
__all__ = ["animate", "Animator", "AnimationStyle"]
