import os
import random
import time
import webbrowser
from pathlib import Path
from typing import Dict, Iterable, List, Mapping, Optional, Sequence, Union
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

"""
Hand a URL or a generated file off to the user's browser: opening built reports, deep-linking
dashboards with filters pre-applied, and fanning a morning set of tabs open from a scheduled job.
"""

# Names webbrowser may have registered; get() raises Error for the ones this machine lacks.
BROWSER_CANDIDATES: Sequence[str] = (
    "windows-default",
    "macosx",
    "safari",
    "chrome",
    "google-chrome",
    "chromium",
    "chromium-browser",
    "firefox",
    "opera",
    "edge",
    "wslview",
    "xdg-open",
    "gnome-open",
)

FilterValue = Union[str, int, float, Sequence[Union[str, int, float]]]


def is_browser_available() -> bool:
    """
    Report whether this machine can open a browser at all.
    Guards in pipelines that run both on a desktop and headless on a scheduler.

    Returns:
        True if a default browser resolves, False on a headless box with nothing registered.
    """
    try:
        webbrowser.get()
    except webbrowser.Error:
        return False
    return True


def available_browsers() -> List[str]:
    """
    Probe the known browser names and keep the ones that resolve here.
    Logs what a reporting host can actually drive before scheduling anything visual.

    Returns:
        Registered names that resolve, in probe order. Empty list on a headless host.
    """
    found: List[str] = []
    for name in BROWSER_CANDIDATES:
        try:
            webbrowser.get(name)
        except webbrowser.Error:
            continue
        found.append(name)
    return found


def open_url(url: str, new_tab: bool = True, browser: Optional[str] = None) -> bool:
    """
    Open a URL, optionally in a named browser rather than the system default.
    Sends a finished report or dashboard straight to the analyst who triggered the run.

    Args:
        url: Absolute URL, including scheme (`https://`, `file://`).
        new_tab: True for a new tab, False to reuse the current window when the browser allows it.
        browser: Registered name from `available_browsers()`, or None for the default.

    Returns:
        True if the browser accepted the request. See the gotcha at the bottom of this file.

    Raises:
        webbrowser.Error: No browser is available, or `browser` is not registered here.
    """
    controller = webbrowser.get(browser) if browser else webbrowser.get()
    return controller.open(url, new=2 if new_tab else 0, autoraise=True)


def build_dashboard_url(base_url: str, filters: Mapping[str, FilterValue]) -> str:
    """
    Merge filter values into a URL's query string, keeping any parameters already there.

    Args:
        base_url: Dashboard URL, with or without an existing query string.
        filters: Parameter names to values; a sequence value repeats the parameter.

    Returns:
        The URL with merged, encoded query parameters.
    """
    parts = urlsplit(base_url)
    query: List[tuple] = parse_qsl(parts.query, keep_blank_values=True)
    incoming = dict(filters)
    query = [(key, value) for key, value in query if key not in incoming]
    for key, value in incoming.items():
        if isinstance(value, (list, tuple, set)):
            query.extend((key, item) for item in value)
        else:
            query.append((key, value))
    return urlunsplit((parts.scheme, parts.netloc, parts.path, urlencode(query, doseq=True), parts.fragment))


def open_dashboard(base_url: str, filters: Mapping[str, FilterValue], browser: Optional[str] = None) -> bool:
    """
    Build a filtered dashboard URL and open it.
    Opens the last step of a pipeline: land the user on the exact slice the run just refreshed.

    Args:
        base_url: Dashboard URL.
        filters: Parameters to apply, as in `build_dashboard_url`.
        browser: Registered browser name, or None for the default.

    Returns:
        True if the browser accepted the request.

    Raises:
        webbrowser.Error: No browser is available, or `browser` is not registered here.
    """
    return open_url(build_dashboard_url(base_url, filters), new_tab=True, browser=browser)


def open_local_report(path: Union[str, Path], browser: Optional[str] = None) -> bool:
    """
    Open a file on disk by converting it to a `file://` URL first.
    Open exported HTML reports, plotly output, and profiling summaries.

    Args:
        path: Path to the file; `~` is expanded and the path is resolved.
        browser: Registered browser name, or None for the default.

    Returns:
        True if the browser accepted the request.

    Raises:
        FileNotFoundError: The path does not exist.
        webbrowser.Error: No browser is available, or `browser` is not registered here.
    """
    resolved = Path(path).expanduser().resolve(strict=True)
    return open_url(resolved.as_uri(), new_tab=True, browser=browser)


def open_many(urls: Iterable[str], pause: float = 0.75, browser: Optional[str] = None) -> Dict[str, bool]:
    """
    Open several URLs in sequence, pausing between them.
    Open a start-of-day tab set; the pause keeps a cold browser from dropping later requests.

    Args:
        urls: URLs to open, in order.
        pause: Seconds to wait between opens. Drop below ~0.5 and a launching browser may swallow some.
        browser: Registered browser name, or None for the default.

    Returns:
        Each URL mapped to whether its open succeeded; failures are recorded, not raised.
    """
    results: Dict[str, bool] = {}
    for index, url in enumerate(urls):
        if index:
            time.sleep(pause)
        try:
            results[url] = open_url(url, new_tab=True, browser=browser)
        except webbrowser.Error as exc:
            print(f"Could not open {url}: {exc}")
            results[url] = False
    return results


def register_browser(name: str, executable: str, preferred: bool = False) -> None:
    """
    Register a browser executable under a name so `get()` can drive it.
    Pins reports to a specific profile or a kiosk browser on a reporting host.

    Args:
        name: Name to register under, later passed as the `browser` argument.
        executable: Command or full path to the browser binary.
        preferred: True to make it the default for `webbrowser.open()` calls.
    """
    webbrowser.register(name, None, webbrowser.BackgroundBrowser(executable), preferred=preferred)


if __name__ == "__main__":
    # Opening tabs is a side effect, so the demo only builds and prints unless you opt in.
    LAUNCH = os.environ.get("WEBBROWSER_DEMO_OPEN") == "1"

    print(f"Browser available: {is_browser_available()}")
    print(f"Registered and resolving: {available_browsers() or 'none (headless host)'}")

    region = random.choice(["northeast", "midwest", "south", "west"])
    quarter = f"{random.randint(2022, 2025)}-Q{random.randint(1, 4)}"
    dashboard = "https://bi.example.com/dashboards/revenue?theme=dark"
    filters = {"region": region, "quarter": quarter, "metric": ["revenue", "margin"]}
    print(f"\nDeep link: {build_dashboard_url(dashboard, filters)}")

    port = random.randrange(8000, 8100)
    morning_tabs = [
        f"http://localhost:{port}/pipeline-status",
        build_dashboard_url(dashboard, {"region": region, "quarter": quarter}),
        "https://docs.python.org/3/library/webbrowser.html",
    ]
    print("\nMorning tab set:")
    for tab in morning_tabs:
        print(f"  {tab}")

    report = Path(__file__).resolve()
    print(f"\nLocal report as a URL: {report.as_uri()}")

    # Registering is harmless even when the executable is absent; get() only fails at launch time.
    register_browser("reporting-kiosk", "/usr/bin/chromium", preferred=False)
    print("Registered 'reporting-kiosk' -> /usr/bin/chromium")

    if LAUNCH:
        try:
            print(f"\nopen_url: {open_url('https://docs.python.org/3/library/webbrowser.html')}")
            print(f"open_dashboard: {open_dashboard(dashboard, filters)}")
            print(f"open_local_report: {open_local_report(report)}")
            print(f"open_many: {open_many(morning_tabs, pause=0.75)}")
        except (webbrowser.Error, FileNotFoundError) as exc:
            print(f"Launch failed: {exc}")
    else:
        print("\nSet WEBBROWSER_DEMO_OPEN=1 to actually launch open_url, open_dashboard, open_local_report, open_many.")

    # Gotcha: open() returns True when the launcher was handed the URL, not when a page rendered.
    # macOS `open` and Linux `xdg-open` exit 0 immediately, so a dead profile or a bad URL still reads True.
    # Gotcha: new=2 (new tab) is a request, not a guarantee - most browsers honor their own tab settings first.
    # Gotcha: the BROWSER environment variable overrides the default, so a server's cron env can differ from a shell.
