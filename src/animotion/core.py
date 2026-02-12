"""
Convenience functions for quick animation usage
"""
import time
from .animator import Animator
from .styles import AnimationStyle


def animate(
    iterable=None,
    style="spinner",
    width=40,
    message="",
    color="cyan",
    speed=0.1,
    total=None,
    prefix="",
    suffix="",
    show_time=False,
):
    """
    Convenience function to animate an iterable or use as context manager.
    
    Usage examples:
    --------------
    # Iterate over items with animation
    for item in animate(my_list, style="wave"):
        process(item)
    
    # Use as context manager
    with animate(style="matrix", message="Processing"):
        do_work()
    
    Parameters:
    -----------
    iterable : iterable, optional
        Iterable to wrap with animation
    style : str or AnimationStyle, optional
        Animation style (default: "spinner")
    width : int, optional
        Animation width (default: 40)
    message : str, optional
        Message to display (default: "")
    color : str, optional
        Animation color (default: "cyan")
    speed : float, optional
        Animation speed in seconds (default: 0.1)
    total : int, optional
        Total items for progress tracking (default: None)
    prefix : str, optional
        Prefix text (default: "")
    suffix : str, optional
        Suffix text (default: "")
    show_time : bool, optional
        Show elapsed time (default: False)
    
    Returns:
    --------
    Generator or Animator context manager
    """
    if total is None and iterable is not None:
        try:
            total = len(iterable)
        except TypeError:
            total = None
    
    animator = Animator(
        style=style,
        width=width,
        message=message,
        color=color,
        speed=speed,
        total=total,
        prefix=prefix,
        suffix=suffix,
        show_time=show_time,
    )
    
    if iterable is not None:
        return animator.iterate(iterable)
    else:
        return animator


def list_styles():
    """List all available animation styles"""
    return AnimationStyle.list_styles()
