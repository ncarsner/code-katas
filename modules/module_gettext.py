import gettext
from typing import Callable
from pathlib import Path
from datetime import datetime

"""
Practical usage of gettext where multilingual support is essential (e.g., reports, dashboards, data pipelines, APIs).

Setup:
1. Create locale directories: locale/es_ES/LC_MESSAGES/, locale/fr_FR/LC_MESSAGES/
2. Generate .pot template: xgettext -d base -o locale/base.pot module_gettext.py
3. Initialize .po files: msginit -i locale/base.pot -o locale/es_ES/LC_MESSAGES/base.po -l es_ES
4. Compile .mo files: msgfmt -o locale/es_ES/LC_MESSAGES/base.mo locale/es_ES/LC_MESSAGES/base.po
"""



# Basic gettext setup for single language
def basic_translation_example(language: str = "es_ES") -> None:
    """
    Demonstrates basic message translation using gettext.
    
    Args:
        language: Language code (e.g., 'es_ES', 'fr_FR')
    
    Usage:
        Used in BI reports, dashboards, or ETL logs that need localization.
    """
    # Define locale directory structure
    locale_dir = Path(__file__).parent / "locale"
    
    # Install translation for specific language
    translation = gettext.translation(
        domain="base",  # Name of your .mo file (base.mo)
        localedir=locale_dir,
        languages=[language],
        fallback=True  # Falls back to original strings if translation missing
    )
    
    # Get the translation function
    _ = translation.gettext
    
    # Use _() for translatable strings
    print(_("Data processing started"))
    print(_("Records processed: %d") % 1000)
    print(_("Report generation complete"))


# Class-based translation for multi-tenant applications
class MultilingualReportGenerator:
    """
    Use case: A data platform serving users in different countries
    where report headers, column names, and messages need localization.
    """
    
    def __init__(self, locale_dir: Path, domain: str = "reports"):
        """
        Args:
            locale_dir: Path to locale directory containing translations
            domain: Translation domain (matches .mo filename)
        """
        self.locale_dir = locale_dir
        self.domain = domain
        self._translators: dict[str, gettext.NullTranslations] = {}
    
    def _get_translator(self, language: str) -> Callable[[str], str]:
        """
        Retrieves or creates a translator for specified language.
        
        Args:
            language: Language code (e.g., 'en_US', 'es_ES')
        
        Returns:
            Translation function for the language
        """
        if language not in self._translators:
            try:
                self._translators[language] = gettext.translation(
                    self.domain,
                    localedir=self.locale_dir,
                    languages=[language],
                    fallback=False
                )
            except FileNotFoundError:
                # Fallback to NullTranslations (returns original strings)
                self._translators[language] = gettext.NullTranslations()
        
        return self._translators[language].gettext
    
    def generate_report_header(self, language: str) -> dict[str, str | dict[str, str]]:
        """
        Generates localized report headers.
        
        Args:
            language: Target language for translation
        
        Returns:
            Dictionary of translated header fields
        """
        _ = self._get_translator(language)
        
        return {
            "title": _("Monthly Sales Report"),
            "date": _("Generated on: %s") % datetime.now().strftime("%Y-%m-%d"),
            "columns": {
                "product": _("Product Name"),
                "revenue": _("Revenue"),
                "quantity": _("Quantity Sold"),
                "region": _("Region")
            }
        }


# Using ngettext for plural forms
def format_record_count(count: int, language: str = "en_US") -> str:
    """
    Handles plural forms correctly in different languages.
    
    Args:
        count: Number of records
        language: Target language
    
    Returns:
        Properly pluralized message
    
    Note:
        Different languages have different plural rules.
        English: 1 vs. many; Polish: 1, few, many; Arabic: 0, 1, 2, few, many
    """
    locale_dir = Path(__file__).parent / "locale"
    
    try:
        translation = gettext.translation(
            "base",
            localedir=locale_dir,
            languages=[language]
        )
    except FileNotFoundError:
        translation = gettext.NullTranslations()
    
    # ngettext handles plural forms
    message = translation.ngettext(
        "%d record processed",  # Singular
        "%d records processed",  # Plural
        count
    )
    
    return message % count


# Context-aware translations using pgettext
class DataPipelineLogger:
    """
    Logs data pipeline events with context-aware translations.
    
    Use case: ETL pipelines where same word has different meanings
    in different contexts (e.g., "run" as noun vs. verb).
    """
    
    def __init__(self, language: str = "en_US"):
        """
        Args:
            language: Language for log messages
        """
        locale_dir = Path(__file__).parent / "locale"
        
        try:
            self._translation = gettext.translation(
                "pipeline",
                localedir=locale_dir,
                languages=[language]
            )
        except FileNotFoundError:
            self._translation = gettext.NullTranslations()
    
    def log_event(self, context: str, message: str) -> str:
        """
        Logs event with context-specific translation.
        
        Args:
            context: Message context (e.g., 'database', 'file', 'api')
            message: Message to translate
        
        Returns:
            Translated message with context
        """
        # pgettext provides context to disambiguate translations
        if hasattr(self._translation, 'pgettext'):
            return self._translation.pgettext(context, message)
        else:
            return self._translation.gettext(message)


# Dynamic language switching for APIs
class MultilingualAPIResponse:
    """
    API response handler with dynamic language selection.
    
    Use case: REST APIs serving international clients where
    Accept-Language header determines response language.
    """
    
    def __init__(self, locale_dir: Path):
        self.locale_dir = locale_dir
        self._cache: dict[str, gettext.NullTranslations] = {}
    
    def get_error_message(
        self,
        error_code: str,
        language: str,
        **kwargs
    ) -> dict[str, str]:
        """
        Returns localized error message for API responses.
        
        Args:
            error_code: Internal error code
            language: Client's preferred language
            **kwargs: Format parameters for message
        
        Returns:
            Dictionary with error code and localized message
        """
        _ = self._get_translation(language)
        
        error_messages = {
            "DB_CONNECTION": _("Database connection failed"),
            "INVALID_QUERY": _("Invalid query parameters"),
            "RATE_LIMIT": _("Rate limit exceeded: %(limit)d requests per hour"),
            "NO_DATA": _("No data found for the specified criteria")
        }
        
        message = error_messages.get(error_code, _("Unknown error"))
        
        if kwargs:
            message = message % kwargs
        
        return {
            "error_code": error_code,
            "message": message,
            "language": language
        }
    
    def _get_translation(self, language: str) -> Callable[[str], str]:
        """Cached translator retrieval for performance."""
        if language not in self._cache:
            try:
                self._cache[language] = gettext.translation(
                    "api",
                    localedir=self.locale_dir,
                    languages=[language]
                )
            except FileNotFoundError:
                self._cache[language] = gettext.NullTranslations()
        
        return self._cache[language].gettext


# Practical workflow for creating translations
def create_translation_workflow() -> None:
    """
    Step-by-step guide for setting up gettext in your project.
    
    Workflow:
    1. Mark translatable strings with _() or gettext()
    2. Extract strings: xgettext -d domain -o messages.pot yourfile.py
    3. Create language file: msginit -i messages.pot -o es_ES.po -l es_ES
    4. Translate strings in .po file
    5. Compile: msgfmt -o domain.mo es_ES.po
    6. Place .mo in locale/es_ES/LC_MESSAGES/
    
    Directory structure:
        project/
        ├── module_gettext.py
        └── locale/
            ├── es_ES/
            │   └── LC_MESSAGES/
            │       ├── base.po
            │       └── base.mo
            └── fr_FR/
                └── LC_MESSAGES/
                    ├── base.po
                    └── base.mo
    """
    print("See docstring for translation workflow")


if __name__ == "__main__":
    print("=== Basic Translation ===")
    basic_translation_example("es_ES")
    
    print("\n=== Plural Forms ===")
    print(format_record_count(1, "en_US"))
    print(format_record_count(5, "en_US"))
    
    print("\n=== Report Generator ===")
    locale_path = Path(__file__).parent / "locale"
    report_gen = MultilingualReportGenerator(locale_path)
    headers = report_gen.generate_report_header("en_US")
    print(headers)
    
    print("\n=== API Error Messages ===")
    api = MultilingualAPIResponse(locale_path)
    error = api.get_error_message("RATE_LIMIT", "en_US", limit=100)
    print(error)