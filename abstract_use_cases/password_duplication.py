from __future__ import annotations
from string import ascii_letters, digits, punctuation
import math
import time
from prettytable import PrettyTable

# Define character set once
CHARS = ascii_letters + digits
# CHARS = ascii_letters + digits + punctuation

def format_human_readable(n):
    """Converts large numbers into readable magnitudes using match-case."""
    if n < 1_000: return f"{int(n)}"
    
    magnitude = int(math.log10(n) // 3)
    
    match magnitude:
        case 1: return f"{n / 1e3:.2f} k"
        case 2: return f"{n / 1e6:.2f} M"
        case 3: return f"{n / 1e9:.2f} B"
        case 4: return f"{n / 1e12:.2f} T"
        case 5: return f"{n / 1e15:.2f} Quadrillion (M|B)"
        case 6: return f"{n / 1e18:.2f} Quintillion (B|B)"
        case 7: return f"{n / 1e21:.2f} Sextillion (B|T)"
        case 8: return f"{n / 1e24:.2f} Septillion (T|T)"
        case 9: return f"{n / 1e27:.2f} Octillion (B|B|B)"
        case 10: return f"{n / 1e30:.2f} Nonillion (B|B|T)"
        case _: return f"{n:.2e}"

def benchmark_security_thresholds(lengths, charset_size=len(CHARS)):
    table = PrettyTable()

    # Title centered within the table border
    table.title = f"CRITICAL SECURITY ANALYSIS: RANDOM PASSWORD OVERLAP @ {charset_size} CHARS"

    table.field_names = [
        "Pass Length",
        "Unique Combinations",
        "Collision Risk",
        "Max Population Size (n)",
        "Benchmark Speed"
    ]
    table.align = "l"
    
    risk_levels = [0.01, 0.10, 0.25, 0.50]
    
    for i, L in enumerate(lengths):
        if i > 0:
            table.add_row(["-" * 15, "-" * 25, "-" * 15, "-" * 25, "-" * 15])

        H = charset_size ** L
        h_readable = format_human_readable(H)
        
        for p in risk_levels:
            start_time = time.perf_counter()
            
            # Birthday Paradox formula
            n = math.sqrt(2 * H * math.log(1 / (1 - p)))
            
            elapsed_us = (time.perf_counter() - start_time) * 1_000_000
            
            table.add_row([
                f"{L} characters", 
                h_readable, 
                f"{p:.0%}", 
                format_human_readable(n), 
                f"{elapsed_us:.2f} μs"
            ])

    print(table)
    print("Documentation: 'Max Population Size' is the count generated before hitting the 'Collision Risk' probability.")

# Evaluate settings
benchmark_security_thresholds([8, 12, 16])