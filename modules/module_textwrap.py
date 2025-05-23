import textwrap
from typing import List

"""
Useful for formatting plain text for reports, emails, dashboards, and logs, ensuring readability and consistency.
"""


def wrap_text(text: str, width: int = 70) -> List[str]:
    """
    Wraps a single string into a list of lines, each at most `width` characters long.

    Args:
        text (str): The input text to wrap.
        width (int): The maximum line width.

    Returns:
        List[str]: A list of wrapped lines.

    Example:
        >>> wrap_text("This is a long line that needs to be wrapped.", width=20)
        ['This is a long line', 'that needs to be', 'wrapped.']
    """
    return textwrap.wrap(text, width=width)


def fill_text(text: str, width: int = 70) -> str:
    """
    Wraps and joins text into a single string with newlines at each wrap point.

    Args:
        text (str): The input text to fill.
        width (int): The maximum line width.

    Returns:
        str: The wrapped text as a single string.

    Example:
        >>> fill_text("This is a long line that needs to be wrapped.", width=20)
        'This is a long line\nthat needs to be\nwrapped.'
    """
    return textwrap.fill(text, width=width)


def shorten_text(text: str, width: int = 70, placeholder: str = "...") -> str:
    """
    Shortens text to fit within a given width, appending a placeholder if truncated.

    Args:
        text (str): The input text to shorten.
        width (int): The maximum width of the output string.
        placeholder (str): The string to append if text is truncated.

    Returns:
        str: The shortened text.

    Example:
        >>> shorten_text("This is a very long sentence that should be shortened.", width=30)
        'This is a very long...'
    """
    return textwrap.shorten(text, width=width, placeholder=placeholder)


def indent_text(text: str, prefix: str = "    ") -> str:
    """
    Indents each line in the given text with the specified prefix.

    Args:
        text (str): The input text to indent.
        prefix (str): The string to prepend to each line.

    Returns:
        str: The indented text.

    Example:
        >>> indent_text("Line 1\nLine 2", prefix="> ")
        '> Line 1\n> Line 2'
    """
    return textwrap.indent(text, prefix)


def dedent_text(text: str) -> str:
    """
    Removes any common leading whitespace from every line in the input text.

    Args:
        text (str): The input text to dedent.

    Returns:
        str: The dedented text.

    Example:
        >>> dedent_text("    Line 1\n    Line 2")
        'Line 1\nLine 2'
    """
    return textwrap.dedent(text)


if __name__ == "__main__":
    sample_report = """
        Sales Report Q1 2024

        The total revenue for Q1 exceeded expectations. The following regions performed exceptionally well:
        - North America
        - EMEA
        - APAC

        Please review the attached charts for more details.
    """

    print("Original Report:")
    print(sample_report)

    print("\nDedented Report:")
    print(dedent_text(sample_report))

    print("\nWrapped Report (width=50):")
    print(fill_text(dedent_text(sample_report), width=50))

    print("\nShortened Summary (width=60):")
    print(
        shorten_text(
            "Total revenue for Q1 exceeded expectations and set a new record for the company.",
            width=60,
        )
    )

    print("\nIndented for Email Quoting:")
    print(indent_text(fill_text(dedent_text(sample_report), width=50), prefix="> "))

"""
TROUBLESHOOTING TIPS:
- If text is not wrapping as expected, check for long words or URLs; consider using break_long_words=True in wrap/fill.
- For multi-line strings, dedent before wrapping to avoid uneven indentation.
- Use indent() to format quoted replies or code blocks in emails/reports.
- Use shorten() for summaries or dashboard tooltips, but note it only works on single paragraphs.
"""
