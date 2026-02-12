"""
Core animation frames and patterns
"""
import random
import math


class AnimationFrames:
    """Collection of animation frame generators"""
    
    @staticmethod
    def spinner(frame_num, width=40):
        """Classic spinner animation"""
        spinners = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
        char = spinners[frame_num % len(spinners)]
        return f"{char} Processing..."
    
    @staticmethod
    def matrix(frame_num, width=40):
        """Matrix-style falling characters"""
        chars = "0123456789ABCDEFアイウエオカキクケコ"
        output = []
        for i in range(width):
            if random.random() < 0.3:
                output.append(random.choice(chars))
            else:
                output.append(' ')
        return ''.join(output)
    
    @staticmethod
    def bouncing(frame_num, width=40):
        """Bouncing ball animation"""
        position = int(abs(math.sin(frame_num * 0.2) * (width - 1)))
        output = [' '] * width
        output[position] = '●'
        return ''.join(output)
    
    @staticmethod
    def particles(frame_num, width=40):
        """Random particle animation"""
        particles = '·∗✦✧✶✷✸✹★☆'
        output = []
        for i in range(width):
            if random.random() < 0.1:
                output.append(random.choice(particles))
            else:
                output.append(' ')
        return ''.join(output)
    
    @staticmethod
    def loading_dots(frame_num, width=40):
        """Loading dots animation"""
        dots = ['   ', '.  ', '.. ', '...']
        pattern = dots[frame_num % len(dots)]
        return f"Loading{pattern}"
    
    @staticmethod
    def progress_bar(frame_num, width=40, total=100, current=None):
        """Progress bar animation"""
        if current is None:
            current = (frame_num * 2) % (total + 1)
        filled = int(width * current / total)
        bar = '█' * filled + '░' * (width - filled)
        percentage = int(100 * current / total)
        return f"[{bar}] {percentage}%"
    
    @staticmethod
    def blocks(frame_num, width=40):
        """Animated blocks"""
        blocks = ['▖', '▘', '▝', '▗']
        output = []
        for i in range(width):
            block_idx = (i + frame_num) % len(blocks)
            output.append(blocks[block_idx])
        return ''.join(output)
    
    @staticmethod
    def arrows(frame_num, width=40):
        """Arrow animation"""
        arrows = ['→', '↗', '↑', '↖', '←', '↙', '↓', '↘']
        char = arrows[frame_num % len(arrows)]
        return f"{char * (frame_num % 5 + 1)} Processing {char * (frame_num % 5 + 1)}"
    
    @staticmethod
    def pulse(frame_num, width=40):
        """Pulsing animation"""
        intensity = abs(math.sin(frame_num * 0.3))
        chars = ' ░▒▓█'
        char_idx = int(intensity * (len(chars) - 1))
        char = chars[char_idx]
        pulse_width = int(width * intensity)
        padding = (width - pulse_width) // 2
        return ' ' * padding + char * pulse_width + ' ' * padding
    
    @staticmethod
    def snake(frame_num, width=40):
        """Snake animation"""
        snake_len = 8
        position = frame_num % (width + snake_len)
        output = [' '] * width
        for i in range(snake_len):
            pos = position - i
            if 0 <= pos < width:
                if i == 0:
                    output[pos] = '◉'
                else:
                    output[pos] = '○'
        return ''.join(output)
    
    @staticmethod
    def fireworks(frame_num, width=40):
        """Fireworks animation"""
        firework_chars = '✦✧★☆✶✷✸✹'
        output = []
        for i in range(width):
            if random.random() < 0.05:
                output.append(random.choice(firework_chars))
            else:
                output.append(' ')
        return ''.join(output)
    
    @staticmethod
    def dna(frame_num, width=40):
        """DNA helix animation"""
        dna_chars = '╱╲'
        output = []
        for i in range(width):
            char_idx = (i + frame_num) % len(dna_chars)
            output.append(dna_chars[char_idx])
        return ''.join(output)
    
    @staticmethod
    def clock(frame_num, width=40):
        """Clock animation"""
        clock = ['🕐', '🕑', '🕒', '🕓', '🕔', '🕕', '🕖', '🕗', '🕘', '🕙', '🕚', '🕛']
        char = clock[frame_num % len(clock)]
        return f"{char} Processing..."
    
    @staticmethod
    def binary(frame_num, width=40):
        """Binary rain animation"""
        output = []
        for i in range(width):
            if random.random() < 0.3:
                output.append(str(random.randint(0, 1)))
            else:
                output.append(' ')
        return ''.join(output)
