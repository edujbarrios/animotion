"""
Main Animator class for Animotion
"""
import sys
import time
import threading
from contextlib import contextmanager
from .styles import AnimationStyle
from .frames import AnimationFrames
from colorama import init, Fore, Back, Style

# Initialize colorama for cross-platform color support
init()


class Animator:
    """
    Main animator class for terminal animations.
    
    Parameters:
    -----------
    style : str or AnimationStyle
        Animation style to use. Can be string or AnimationStyle enum.
    width : int, optional
        Width of the animation (default: 40)
    message : str, optional
        Custom message to display (default: "")
    color : str, optional
        Color for the animation. Options: 'red', 'green', 'blue', 'yellow', 
        'magenta', 'cyan', 'white' (default: 'cyan')
    speed : float, optional
        Animation speed in seconds per frame (default: 0.1)
    total : int, optional
        Total iterations for progress tracking (default: None)
    prefix : str, optional
        Prefix text before animation (default: "")
    suffix : str, optional
        Suffix text after animation (default: "")
    show_time : bool, optional
        Show elapsed time (default: False)
    file : file object, optional
        Output stream (default: sys.stdout)
    """
    
    def __init__(
        self,
        style="spinner",
        width=40,
        message="",
        color="cyan",
        speed=0.1,
        total=None,
        prefix="",
        suffix="",
        show_time=False,
        file=sys.stdout,
    ):
        # Handle style
        if isinstance(style, str):
            style = style.upper()
            if hasattr(AnimationStyle, style):
                self.style = getattr(AnimationStyle, style)
            else:
                raise ValueError(f"Unknown style: {style}. Use AnimationStyle.list_styles() to see options.")
        else:
            self.style = style
        
        self.width = width
        self.message = message
        self.speed = speed
        self.total = total
        self.prefix = prefix
        self.suffix = suffix
        self.show_time = show_time
        self.file = file
        
        # Color mapping
        self.colors = {
            'red': Fore.RED,
            'green': Fore.GREEN,
            'blue': Fore.BLUE,
            'yellow': Fore.YELLOW,
            'magenta': Fore.MAGENTA,
            'cyan': Fore.CYAN,
            'white': Fore.WHITE,
        }
        self.color = self.colors.get(color.lower(), Fore.CYAN)
        
        # Animation state
        self._frame_num = 0
        self._running = False
        self._thread = None
        self._start_time = None
        self._current = 0
        
        # Get animation function
        self._animation_func = self._get_animation_function()
    
    def _get_animation_function(self):
        """Get the animation function based on style"""
        style_map = {
            AnimationStyle.SPINNER: AnimationFrames.spinner,
            AnimationStyle.MATRIX: AnimationFrames.matrix,
            AnimationStyle.BOUNCING: AnimationFrames.bouncing,
            AnimationStyle.PARTICLES: AnimationFrames.particles,
            AnimationStyle.LOADING_DOTS: AnimationFrames.loading_dots,
            AnimationStyle.PROGRESS_BAR: AnimationFrames.progress_bar,
            AnimationStyle.BLOCKS: AnimationFrames.blocks,
            AnimationStyle.ARROWS: AnimationFrames.arrows,
            AnimationStyle.PULSE: AnimationFrames.pulse,
            AnimationStyle.SNAKE: AnimationFrames.snake,
            AnimationStyle.FIREWORKS: AnimationFrames.fireworks,
            AnimationStyle.DNA: AnimationFrames.dna,
            AnimationStyle.CLOCK: AnimationFrames.clock,
            AnimationStyle.BINARY: AnimationFrames.binary,
        }
        return style_map.get(self.style, AnimationFrames.spinner)
    
    def _get_frame(self):
        """Generate a single animation frame"""
        if self.style == AnimationStyle.PROGRESS_BAR and self.total:
            frame = self._animation_func(self._frame_num, self.width, self.total, self._current)
        else:
            frame = self._animation_func(self._frame_num, self.width)
        return frame
    
    def _format_output(self, frame):
        """Format the complete output line"""
        parts = []
        
        if self.prefix:
            parts.append(self.prefix)
        
        if self.message:
            parts.append(self.message)
        
        parts.append(self.color + frame + Style.RESET_ALL)
        
        if self.suffix:
            parts.append(self.suffix)
        
        if self.show_time and self._start_time:
            elapsed = time.time() - self._start_time
            parts.append(f"[{elapsed:.1f}s]")
        
        if self.total:
            parts.append(f"({self._current}/{self.total})")
        
        return " ".join(parts)
    
    def _animate_loop(self):
        """Main animation loop running in separate thread"""
        while self._running:
            frame = self._get_frame()
            output = self._format_output(frame)
            
            # Clear line and write
            self.file.write('\r' + ' ' * 100 + '\r')
            self.file.write(output)
            self.file.flush()
            
            self._frame_num += 1
            time.sleep(self.speed)
    
    def start(self):
        """Start the animation"""
        if not self._running:
            self._running = True
            self._start_time = time.time()
            self._thread = threading.Thread(target=self._animate_loop)
            self._thread.daemon = True
            self._thread.start()
    
    def stop(self, final_message=None):
        """Stop the animation"""
        if self._running:
            self._running = False
            if self._thread:
                self._thread.join()
            
            # Clear the line
            self.file.write('\r' + ' ' * 100 + '\r')
            
            if final_message:
                self.file.write(final_message + '\n')
            
            self.file.flush()
    
    def update(self, n=1):
        """Update progress (for tracked processes)"""
        self._current += n
        if self.total and self._current >= self.total:
            self.stop(f"{Fore.GREEN}✓ Complete!{Style.RESET_ALL}")
    
    def __enter__(self):
        """Context manager entry"""
        self.start()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit"""
        if exc_type is None:
            self.stop(f"{Fore.GREEN}✓ Complete!{Style.RESET_ALL}")
        else:
            self.stop(f"{Fore.RED}✗ Error occurred{Style.RESET_ALL}")
        return False
    
    def iterate(self, iterable):
        """
        Wrap an iterable with animation.
        Similar to tqdm behavior.
        """
        self.start()
        try:
            for item in iterable:
                yield item
                if self.total:
                    self.update(1)
        finally:
            self.stop(f"{Fore.GREEN}✓ Complete!{Style.RESET_ALL}")
