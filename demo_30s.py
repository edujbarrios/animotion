"""
30-second demo to see Animotion animations in action with progress tracking
"""
import time
from animotion import animate

print("\n" + "="*60)
print("        ANIMOTION DEMO - 30 SECONDS WITH PROGRESS")
print("="*60 + "\n")

# Animation 1: Progress Bar (10 seconds)
print("1. Progress Bar Style - Downloading 100 files:")
for i in animate(range(100), style="progress_bar", color="green", width=50, message="Downloading", speed=0.15):
    time.sleep(0.1)  # Simulate work

print()

# Animation 2: Pulse with progress (10 seconds)
print("2. Pulse Style - Processing 100 items:")
items = range(100)
for item in animate(items, style="pulse", color="cyan", width=50, message="Processing", speed=0.15):
    time.sleep(0.1)  # Simulate work

print()

# Animation 3: Snake with progress (10 seconds)
print("3. Snake Style - Analyzing 100 records:")
records = range(100)
for record in animate(records, style="snake", color="magenta", width=50, message="Analyzing", show_time=True, speed=0.15):
    time.sleep(0.1)  # Simulate work

print()
print("="*60)
print("✨ Demo completed! All 300 items processed successfully.")
print("="*60 + "\n")
