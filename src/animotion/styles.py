"""
Animation styles for Animotion
"""
from enum import Enum


class AnimationStyle(Enum):
    """Available animation styles"""
    SPINNER = "spinner"
    MATRIX = "matrix"
    BOUNCING = "bouncing"
    PARTICLES = "particles"
    LOADING_DOTS = "loading_dots"
    PROGRESS_BAR = "progress_bar"
    BLOCKS = "blocks"
    ARROWS = "arrows"
    PULSE = "pulse"
    SNAKE = "snake"
    FIREWORKS = "fireworks"
    DNA = "dna"
    CLOCK = "clock"
    BINARY = "binary"
    
    @classmethod
    def list_styles(cls):
        """Return list of all available styles"""
        return [style.value for style in cls]
