"""
Quick example of CLI progress tickers - run individual functions
"""

from cli_ticker import (
    spinner_basic,
    progress_bar_simple,
    ProgressSpinner
)
import time


def quick_demo():
    """Quick demo showing a few key examples."""
    print("Quick Progress Ticker Demo\n")
    
    # 1. Basic spinner
    print("1. Basic Spinner:")
    spinner_basic()
    
    time.sleep(1)
    
    # 2. Progress bar
    print("\n2. Progress Bar:")
    progress_bar_simple()
    
    time.sleep(1)
    
    # 3. Reusable spinner for long operations
    print("3. Background Spinner (most practical):")
    spinner = ProgressSpinner("Processing data")
    spinner.start()
    time.sleep(3)  # Your actual work goes here
    spinner.stop("Processing completed")
    
    print("\n✓ Demo complete!")


if __name__ == "__main__":
    quick_demo()
