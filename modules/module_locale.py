import locale
from typing import Optional, Tuple
import random


def set_locale(locale_name: str) -> None:
    """Set the locale for the application."""
    try:
        locale.setlocale(locale.LC_ALL, locale_name)
        print(f"\nLocale set to {locale_name}")
    except locale.Error as e:
        print(f"\nError setting locale: {e}")


def format_currency(amount: float, currency_symbol: Optional[str] = None) -> str:
    """Format a number as currency based on the current locale."""
    try:
        formatted = locale.currency(amount, symbol=bool(currency_symbol), grouping=True)
        if currency_symbol:
            formatted = formatted.replace(locale.localeconv()["currency_symbol"], currency_symbol)
        return formatted
    except Exception as e:
        return f"Error formatting currency: {e}"


def format_number(number: float) -> str:
    """Format a number with grouping based on the current locale."""
    try:
        return locale.format_string("%f", number, grouping=True)
    except Exception as e:
        return f"Error formatting number: {e}"


def get_locale_info() -> Tuple[str, str]:
    """Retrieve the current locale settings."""
    try:
        return locale.getlocale(), locale.getpreferredencoding()
    except Exception as e:
        return f"Error retrieving locale info: {e}", ""


def display_locale_options(locales: dict) -> str:
    """Display available locales and return the selected locale."""
    print("Available locales:")
    for i, alias in enumerate(locales, 1):
        print(f"{i}. {alias}")
    try:
        choice = int(input("Enter the preferred locale: "))
        return list(locales.values())[choice - 1] if 1 <= choice <= len(locales) else locales["English"]
    except (ValueError, IndexError):
        print("Invalid input. Defaulting to 'English'.")
        return locales["English"]


def main() -> None:
    locales = {
        "English": "en_US.UTF-8",
        "German": "de_DE.UTF-8",
        "French": "fr_FR.UTF-8",
        "Spanish": "es_ES.UTF-8",
        "Italian": "it_IT.UTF-8",
        "Japanese": "ja_JP.UTF-8",
        "Chinese (Simplified)": "zh_CN.UTF-8",
        "Chinese (Traditional)": "zh_TW.UTF-8",
        "Korean": "ko_KR.UTF-8",
    }

    # Set and display the selected locale
    selected_locale = display_locale_options(locales)
    set_locale(selected_locale)

    # Display locale information
    current_locale, encoding = get_locale_info()
    print(f"\nCurrent Locale: {current_locale}, Encoding: {encoding}")

    # Generate a random number and format it
    number = round(random.uniform(1000, 1000000), 2)
    print(f"\nFormatted Number: {format_number(number)}")
    print(f"Formatted Currency (Default): {format_currency(number)}")

    # Format currency with the native currency symbol
    native_currency_symbol = locale.localeconv().get("currency_symbol", "")
    print(f"Formatted Currency (Custom): {format_currency(number, currency_symbol=native_currency_symbol)}")

    # Change to a random locale and display formatted values
    random_locale = random.choice([loc for loc in locales.values() if loc != selected_locale])
    set_locale(random_locale)
    random_locale_name = next(name for name, loc in locales.items() if loc == random_locale)
    print(f"\nFormatted Number ({random_locale_name}): {format_number(number)}")
    print(f"Formatted Currency ({random_locale_name}): {format_currency(number)}")
    random_currency_symbol = locale.localeconv().get("currency_symbol", "")
    print(f"Formatted Currency (Custom): {format_currency(number, currency_symbol=random_currency_symbol)}")


if __name__ == "__main__":
    main()
