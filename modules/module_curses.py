import curses
from typing import List, Any, Optional
from datetime import datetime
from dataclasses import dataclass

"""
Practical uses of Python's curses library:
- Interactive data monitoring dashboards
- Log file viewers
- ETL pipeline status monitors
- System health dashboards

Requirements: Unix-like system (Linux, macOS) or Windows with windows-curses package
Install on Windows: pip install windows-curses
"""


@dataclass
class PipelineStatus:
    """Represents the status of a data pipeline."""

    name: str
    status: str  # 'running', 'completed', 'failed', 'pending'
    records_processed: int
    last_updated: datetime


def init_colors() -> None:
    """
    Initialize color pairs for terminal UI.
    Call after curses.start_color().

    Color pairs:
    1: Green on black (success)
    2: Red on black (error)
    3: Yellow on black (warning)
    4: Cyan on black (info)
    """
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)


def draw_header(stdscr: Any, title: str) -> int:
    """
    Draw a header bar at the top of the screen.

    Args:
        stdscr: The curses window object
        title: Header title text

    Returns:
        The y-position where content should start (below header)
    """
    height, width = stdscr.getmaxyx()
    stdscr.attron(curses.color_pair(4) | curses.A_BOLD)
    stdscr.addstr(0, 0, title.center(width))
    stdscr.addstr(1, 0, "=" * width)
    stdscr.attroff(curses.color_pair(4) | curses.A_BOLD)
    return 2


def draw_status_indicator(stdscr: Any, y: int, x: int, status: str) -> None:
    """
    Draw a colored status indicator.

    Args:
        stdscr: The curses window object
        y: Y coordinate
        x: X coordinate
        status: Status string ('running', 'completed', 'failed', 'pending')
    """
    color_map = {
        "running": curses.color_pair(3),
        "completed": curses.color_pair(1),
        "failed": curses.color_pair(2),
        "pending": curses.COLOR_WHITE,
    }

    color = color_map.get(status.lower(), curses.COLOR_WHITE)
    stdscr.attron(color | curses.A_BOLD)
    stdscr.addstr(y, x, f"[{status.upper():^10}]")
    stdscr.attroff(color | curses.A_BOLD)


def pipeline_dashboard(stdscr: Any) -> None:
    """
    Interactive ETL pipeline monitoring dashboard.

    Features:
    - Real-time status updates
    - Color-coded status indicators
    - Keyboard navigation (q to quit, r to refresh)

    Args:
        stdscr: The curses window object (passed automatically by curses.wrapper)
    """
    # Initialize
    curses.curs_set(0)  # Hide cursor
    stdscr.nodelay(1)  # Non-blocking input
    stdscr.timeout(1000)  # Refresh every 1000ms
    init_colors()

    # Sample pipeline data
    pipelines: List[PipelineStatus] = [
        PipelineStatus("Sales Data ETL", "running", 15000, datetime.now()),
        PipelineStatus("Customer Analytics", "completed", 50000, datetime.now()),
        PipelineStatus("Inventory Sync", "failed", 3500, datetime.now()),
        PipelineStatus("Financial Reports", "pending", 0, datetime.now()),
    ]

    while True:
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        # Draw header
        start_y = draw_header(stdscr, "ETL Pipeline Monitoring Dashboard")

        # Draw timestamp
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        stdscr.addstr(start_y, 2, f"Last Updated: {current_time}")
        start_y += 2

        # Draw pipeline statuses
        stdscr.attron(curses.A_BOLD)
        stdscr.addstr(start_y, 2, "Pipeline Name")
        stdscr.addstr(start_y, 35, "Status")
        stdscr.addstr(start_y, 52, "Records")
        stdscr.attroff(curses.A_BOLD)
        start_y += 1
        stdscr.addstr(start_y, 2, "-" * (width - 4))
        start_y += 1

        for i, pipeline in enumerate(pipelines):
            y_pos = start_y + i
            if y_pos >= height - 3:  # Leave room for footer
                break

            stdscr.addstr(y_pos, 2, pipeline.name[:30])
            draw_status_indicator(stdscr, y_pos, 35, pipeline.status)
            stdscr.addstr(y_pos, 52, f"{pipeline.records_processed:,}")

        # Draw footer with instructions
        footer_y = height - 2
        stdscr.attron(curses.color_pair(4))
        stdscr.addstr(
            footer_y, 2, "Press 'q' to quit | 'r' to refresh | Arrow keys to scroll"
        )
        stdscr.attroff(curses.color_pair(4))

        stdscr.refresh()

        # Handle input
        key = stdscr.getch()
        if key == ord("q") or key == ord("Q"):
            break
        elif key == ord("r") or key == ord("R"):
            # Simulate status updates
            pipelines[0].records_processed += 100
            if pipelines[0].records_processed > 20000:
                pipelines[0].status = "completed"


def interactive_menu(
    stdscr: Any, options: List[str], title: str = "Select Option"
) -> Optional[int]:
    """
    Create an interactive menu with keyboard navigation.

    Args:
        stdscr: The curses window object
        options: List of menu option strings
        title: Menu title

    Returns:
        Index of selected option, or None if cancelled

    Usage:
        selection = curses.wrapper(interactive_menu, ["Option 1", "Option 2"], "Menu")
    """
    curses.curs_set(0)
    init_colors()

    current_row = 0

    while True:
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        # Draw title
        start_y = draw_header(stdscr, title)
        start_y += 1

        # Draw menu options
        for idx, option in enumerate(options):
            y_pos = start_y + idx
            if y_pos >= height - 3:
                break

            if idx == current_row:
                stdscr.attron(curses.color_pair(4) | curses.A_REVERSE)
                stdscr.addstr(y_pos, 4, f"> {option}")
                stdscr.attroff(curses.color_pair(4) | curses.A_REVERSE)
            else:
                stdscr.addstr(y_pos, 4, f"  {option}")

        # Footer
        stdscr.addstr(height - 2, 2, "↑↓: Navigate | Enter: Select | q: Cancel")
        stdscr.refresh()

        # Handle input
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(options) - 1:
            current_row += 1
        elif key == ord("\n"):  # Enter key
            return current_row
        elif key == ord("q") or key == ord("Q"):
            return None


def log_viewer(stdscr: Any, log_lines: List[str]) -> None:
    """
    Scrollable log file viewer with search capability.

    Args:
        stdscr: The curses window object
        log_lines: List of log line strings

    Controls:
        - Arrow keys: Scroll
        - Page Up/Down: Fast scroll
        - /: Search
        - q: Quit
    """
    curses.curs_set(0)
    init_colors()

    scroll_pos = 0
    search_term = ""

    while True:
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        start_y = draw_header(stdscr, "Log Viewer")
        visible_lines = height - start_y - 3

        # Display log lines
        for i in range(visible_lines):
            line_idx = scroll_pos + i
            if line_idx >= len(log_lines):
                break

            line = log_lines[line_idx][: width - 2]
            y_pos = start_y + i

            # Highlight errors and warnings
            if "ERROR" in line.upper():
                stdscr.attron(curses.color_pair(2))
            elif "WARN" in line.upper():
                stdscr.attron(curses.color_pair(3))

            # Highlight search term
            if search_term and search_term in line:
                stdscr.attron(curses.A_REVERSE)

            stdscr.addstr(y_pos, 1, line)
            stdscr.attroff(
                curses.color_pair(2) | curses.color_pair(3) | curses.A_REVERSE
            )

        # Footer
        footer = f"Lines {scroll_pos + 1}-{min(scroll_pos + visible_lines, len(log_lines))} of {len(log_lines)}"
        if search_term:
            footer += f" | Search: {search_term}"
        stdscr.addstr(height - 2, 2, footer)
        stdscr.addstr(
            height - 1, 2, "↑↓: Scroll | PgUp/PgDn: Page | /: Search | q: Quit"
        )

        stdscr.refresh()

        key = stdscr.getch()

        if key == ord("q"):
            break
        elif key == curses.KEY_UP and scroll_pos > 0:
            scroll_pos -= 1
        elif key == curses.KEY_DOWN and scroll_pos < len(log_lines) - visible_lines:
            scroll_pos += 1
        elif key == curses.KEY_PPAGE:  # Page Up
            scroll_pos = max(0, scroll_pos - visible_lines)
        elif key == curses.KEY_NPAGE:  # Page Down
            scroll_pos = min(len(log_lines) - visible_lines, scroll_pos + visible_lines)


if __name__ == "__main__":
    # Run pipeline dashboard
    curses.wrapper(pipeline_dashboard)

    # Or run interactive menu
    # options = ["View Sales Data", "Export Reports", "Configure ETL", "Exit"]
    # selection = curses.wrapper(interactive_menu, options, "BI Dashboard Menu")
    # print(f"Selected: {selection}")

    # Or run log viewer
    # sample_logs = [f"2024-01-15 10:{i:02d}:00 INFO Processing batch {i}" for i in range(100)]
    # curses.wrapper(log_viewer, sample_logs)
