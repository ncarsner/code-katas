"""
CLI Progress Ticker Demonstrations

This module demonstrates various ways to show progress indicators
in command-line interfaces while code is executing.
"""

import time
import sys
import threading
from itertools import cycle


def spinner_basic():
    """Basic spinner that rotates through characters."""
    print("Basic Spinner Demo:")
    spinner = cycle(['|', '/', '-', '\\'])
    
    for i in range(40):
        sys.stdout.write(f'\rProcessing... {next(spinner)}')
        sys.stdout.flush()
        time.sleep(0.1)
    
    print('\rProcessing... Done! ✓')


def spinner_with_percentage():
    """Spinner with percentage completion."""
    print("\n\nSpinner with Percentage:")
    spinner = cycle(['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏'])
    total_steps = 50
    
    for i in range(total_steps + 1):
        percentage = (i / total_steps) * 100
        sys.stdout.write(f'\r{next(spinner)} Processing... {percentage:.0f}%')
        sys.stdout.flush()
        time.sleep(0.05)
    
    print('\r✓ Processing... 100% Complete!')


def progress_bar_simple():
    """Simple progress bar with blocks."""
    print("\n\nSimple Progress Bar:")
    total = 50
    bar_length = 40
    
    for i in range(total + 1):
        filled_length = int(bar_length * i / total)
        bar = '█' * filled_length + '░' * (bar_length - filled_length)
        percentage = (i / total) * 100
        
        sys.stdout.write(f'\r[{bar}] {percentage:.0f}%')
        sys.stdout.flush()
        time.sleep(0.05)
    
    print('\n')


def progress_bar_with_stats():
    """Progress bar with statistics (items processed, ETA, etc)."""
    print("Progress Bar with Stats:")
    total_items = 100
    bar_length = 30
    start_time = time.time()
    
    for i in range(total_items + 1):
        filled_length = int(bar_length * i / total_items)
        bar = '▓' * filled_length + '░' * (bar_length - filled_length)
        percentage = (i / total_items) * 100
        
        elapsed = time.time() - start_time
        items_per_sec = i / elapsed if elapsed > 0 else 0
        eta = (total_items - i) / items_per_sec if items_per_sec > 0 else 0
        
        sys.stdout.write(
            f'\r[{bar}] {percentage:.0f}% | '
            f'{i}/{total_items} items | '
            f'{items_per_sec:.1f} items/s | '
            f'ETA: {eta:.1f}s'
        )
        sys.stdout.flush()
        time.sleep(0.03)
    
    print('\n')


def multi_stage_progress():
    """Progress indicator for multi-stage operations."""
    print("Multi-Stage Progress:")
    stages = [
        ("Initializing", 20),
        ("Loading data", 30),
        ("Processing", 40),
        ("Saving results", 25),
        ("Cleanup", 15)
    ]
    
    total_steps = sum(steps for _, steps in stages)
    completed = 0
    
    for stage_name, steps in stages:
        for i in range(steps):
            completed += 1
            percentage = (completed / total_steps) * 100
            bar_length = 30
            filled = int(bar_length * completed / total_steps)
            bar = '█' * filled + '─' * (bar_length - filled)
            
            sys.stdout.write(
                f'\r[{bar}] {percentage:.0f}% | {stage_name}...'
            )
            sys.stdout.flush()
            time.sleep(0.05)
    
    print('\r' + ' ' * 60)  # Clear the line
    print('✓ All stages completed!')


def animated_dots():
    """Animated dots showing activity."""
    print("\n\nAnimated Dots:")
    messages = [
        "Connecting to server",
        "Downloading data",
        "Processing files",
        "Finalizing"
    ]
    
    for message in messages:
        for dots in range(4):
            sys.stdout.write(f'\r{message}{"." * dots}   ')
            sys.stdout.flush()
            time.sleep(0.3)
        print(f'\r{message}... ✓')


class ProgressSpinner:
    """
    Reusable progress spinner that runs in a background thread.
    Useful for operations where you can't track precise progress.
    """
    
    def __init__(self, message="Processing"):
        self.message = message
        self.spinner = cycle(['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏'])
        self.running = False
        self.thread = None
    
    def _spin(self):
        """Internal method that runs the spinner."""
        while self.running:
            sys.stdout.write(f'\r{next(self.spinner)} {self.message}...')
            sys.stdout.flush()
            time.sleep(0.1)
    
    def start(self):
        """Start the spinner in a background thread."""
        self.running = True
        self.thread = threading.Thread(target=self._spin)
        self.thread.daemon = True
        self.thread.start()
    
    def stop(self, final_message=None):
        """Stop the spinner and optionally show a final message."""
        self.running = False
        if self.thread:
            self.thread.join()
        
        if final_message:
            sys.stdout.write(f'\r✓ {final_message}\n')
        else:
            sys.stdout.write(f'\r✓ {self.message}... Done!\n')
        sys.stdout.flush()


def demo_progress_spinner():
    """Demonstrate the reusable ProgressSpinner class."""
    print("\n\nReusable Progress Spinner:")
    
    # Example 1: Simple usage
    spinner = ProgressSpinner("Downloading file")
    spinner.start()
    time.sleep(3)  # Simulate work
    spinner.stop("File downloaded successfully")
    
    # Example 2: Multiple operations
    operations = [
        ("Connecting to database", 2),
        ("Executing query", 2.5),
        ("Fetching results", 1.5)
    ]
    
    for operation, duration in operations:
        spinner = ProgressSpinner(operation)
        spinner.start()
        time.sleep(duration)
        spinner.stop()


def color_progress_bar():
    """Progress bar with color coding (using ANSI escape codes)."""
    print("\n\nColor-Coded Progress Bar:")
    
    # ANSI color codes
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'
    
    total = 100
    bar_length = 40
    
    for i in range(total + 1):
        filled_length = int(bar_length * i / total)
        bar = '█' * filled_length + '░' * (bar_length - filled_length)
        percentage = (i / total) * 100
        
        # Color code based on progress
        if percentage < 33:
            color = RED
        elif percentage < 66:
            color = YELLOW
        else:
            color = GREEN
        
        sys.stdout.write(
            f'\r{color}[{bar}] {percentage:.0f}%{RESET}'
        )
        sys.stdout.flush()
        time.sleep(0.03)
    
    print('\n')


def custom_task_indicator():
    """Custom indicator showing specific tasks being processed."""
    print("\n\nCustom Task Indicator:")
    tasks = [
        "user_data.csv",
        "transactions.json",
        "inventory.xml",
        "logs.txt",
        "config.yaml"
    ]
    
    total = len(tasks)
    
    for idx, task in enumerate(tasks, 1):
        percentage = (idx / total) * 100
        status_bar = '=' * idx + '>' + ' ' * (total - idx)
        
        sys.stdout.write(
            f'\rProgress: [{status_bar}] {percentage:.0f}% | '
            f'Processing: {task:<20}'
        )
        sys.stdout.flush()
        time.sleep(0.5)
    
    print('\n✓ All files processed!')


def main():
    """Run all demonstrations."""
    print("=" * 60)
    print("CLI PROGRESS TICKER DEMONSTRATIONS")
    print("=" * 60)
    
    try:
        spinner_basic()
        spinner_with_percentage()
        progress_bar_simple()
        progress_bar_with_stats()
        multi_stage_progress()
        animated_dots()
        demo_progress_spinner()
        color_progress_bar()
        custom_task_indicator()
        
        print("\n" + "=" * 60)
        print("All demonstrations completed!")
        print("=" * 60)
        
    except KeyboardInterrupt:
        print("\n\nDemonstration interrupted by user.")
        sys.exit(0)


if __name__ == "__main__":
    main()
