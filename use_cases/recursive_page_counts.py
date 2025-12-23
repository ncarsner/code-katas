from pathlib import Path
from typing import Optional, List

# from colorama import init, Fore, Style
from pypdf import PdfReader

# ----------------------------- CONFIG ----------------------------------

DIRECTORY = Path(r'C:\Users\Directory')
SUBDIRECTORY = 'Subdirectory'

DIRECTORY = Path(r'C:\Users\Directory')
SUBDIRECTORY: Optional[str] = None   # <-- Set to None to scan recursively

WIDTH = 45

# --------------------------- ANSI COLOR HELPERS -------------------------

class Color:
    HEADER = "\033[95m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

# -------------------------- PAGE COUNT FUNCTIONS ------------------------

def count_pdf_pages(filepath: Path) -> int:
    """Return number of pages in a PDF file using pypdf."""
    try:
        reader = PdfReader(str(filepath))
        return len(reader.pages)
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return 0


def count_docx_pages(filepath: Path) -> int:
    """Placeholder for DOCX; requires custom logic."""
    raise NotImplementedError("DOCX page counting logic not implemented yet.")


# Map file extensions to their counting function
PAGE_COUNTERS = {
    ".pdf": count_pdf_pages,
    # ".docx": count_docx_pages,
}


# -------------------------- DIRECTORY SCANNING LOGIC -------------------

def collect_files(root: Path, target_subdir: Optional[str], extensions: List[str]):
    """
    Returns a dict: { folder_name : [list of PDF Paths] }

    Behavior:
    - If target_subdir is a string -> only look inside that subdirectory of each folder.
    - If target_subdir is None -> recursively search all subdirectories.
    """

    folder_map = {}

    if target_subdir is None:
        # Recursive mode — group PDFs by their parent directory
        for file in root.rglob("*"):
            if file.is_file() and file.suffix.lower() in extensions:
                parent = file.parent.name
                folder_map.setdefault(parent, []).append(file)

    else:
        # Specific-subdirectory mode
        for folder in root.iterdir():
            if not folder.is_dir():
                continue

            subfolder = folder / target_subdir
            if not (subfolder.exists() and subfolder.is_dir()):
                continue

            pdfs = []
            for ext in extensions:
                pdfs.extend(subfolder.rglob(f"*{ext}"))

            folder_map[folder.name] = pdfs

    return folder_map



def analyze_directory(root: Path, target_subdir: Optional[str], extensions: List[str]):
    """Analyze directory structure and print colorized, tabular output."""

    mode_label = (
        f"(recursive search — all subdirectories)"
        if target_subdir is None
        else f"(searching only '{target_subdir}' subdirectories)"
    )

    print(f"\n{Color.HEADER}{Color.BOLD}Scanning Directory: {root}{Color.RESET}")
    print(f"{Color.BLUE}{mode_label}{Color.RESET}\n")

    # Table header
    print(
        f"{Color.HEADER}{Color.BOLD}"
        f"{'Subfolder':{WIDTH-25}}  {'Files':>10}  {'Pages':>10}"
        f"{Color.RESET}"
    )
    print(f"{Color.HEADER}{'-' * WIDTH}{Color.RESET}")

    folder_map = collect_files(root, target_subdir, extensions)

    total_files = 0
    total_pages = 0
    folders_scanned = len(folder_map)

    for folder_name, file_list in sorted(folder_map.items()):
        file_count = len(file_list)
        page_count = sum(PAGE_COUNTERS[file.suffix.lower()](file)
                         for file in file_list)

        total_files += file_count
        total_pages += page_count

        folder_color = Color.YELLOW + Color.BOLD
        file_color = Color.GREEN + Color.BOLD if file_count > 0 else Color.RED + Color.BOLD
        page_color = Color.GREEN + Color.BOLD if page_count > 0 else Color.RED + Color.BOLD

        print(
            f"{folder_color}{folder_name:{WIDTH-25}}{Color.RESET}  "
            f"{file_color}{file_count:>10}{Color.RESET}  "
            f"{page_color}{page_count:>10}{Color.RESET}"
        )

    # Totals row
    print(f"{Color.HEADER}{'-' * WIDTH}{Color.RESET}")

    total_file_color = Color.GREEN + Color.BOLD if total_files > 0 else Color.RED + Color.BOLD
    total_page_color = Color.GREEN + Color.BOLD if total_pages > 0 else Color.RED + Color.BOLD

    print(
        f"{Color.BLUE}{Color.BOLD}{'TOTALS':{WIDTH-25}}{Color.RESET}  "
        f"{total_file_color}{total_files:>10}{Color.RESET}  "
        f"{total_page_color}{total_pages:>10}{Color.RESET}"
    )

    print(f"\n{Color.BOLD}Subdirectories scanned: {folders_scanned}{Color.RESET}\n")



# ----------------------------- RUN SCRIPT --------------------------------

if __name__ == "__main__":
    analyze_directory(DIRECTORY, SUBDIRECTORY, extensions=[".pdf"])