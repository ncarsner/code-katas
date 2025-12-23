from pathlib import Path


DIRECTORY = Path(r'C:\Users\Directory')
SUBFOLDER = 'REMEDIATED'
REMOVE_SUFFIX = '-UA'

# ANSI color helpers
class Color:
    HEADER = "\033[95m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    RESET = "\033[0m"
    BOLD = "\033[1m"


def remove_suffix_from_files(file_type: str = '*.pdf') -> None:
    total_found = 0
    total_updated = 0

    print(f"\n{Color.BOLD}{Color.HEADER}========== File Rename Summary =========={Color.RESET}\n") # noqa

    # Table Header
    print(f"{Color.BOLD}{'Subdirectory':<30} {'Files Found':<15} {'Renamed':<10}{Color.RESET}") # noqa
    print("-" * 60)

    for subdir in DIRECTORY.iterdir():
        if not subdir.is_dir():
            continue

        stock_path = subdir / SUBFOLDER

        if not stock_path.exists():
            print(f"{subdir.name:<30} {Color.YELLOW}*** No folder found ***{Color.RESET}") # noqa
            continue

        target_files = list(stock_path.glob(file_type))
        file_count = len(target_files)
        total_found += file_count
        updated_count = 0

        for file in target_files:
            stem = file.stem
            if stem.endswith(REMOVE_SUFFIX):
                new_stem = stem[: -len(REMOVE_SUFFIX)]
                new_name = file.with_stem(new_stem)
                file.rename(new_name)
                updated_count += 1

        total_updated += updated_count

        # Color based on rename count
        color = Color.BLUE if updated_count > 0 else Color.RED

        print(f"{subdir.name:<30} {file_count:<15} {color}{updated_count:<10}{Color.RESET}") # noqa

    print("\n" + "-" * 60)
    print(
        f"{Color.BOLD}Total files found:   "
        f"{total_found}{Color.RESET}\n"
        f"{Color.BOLD}Total files renamed: "
        f"{Color.BLUE}{total_updated}{Color.RESET}\n"
    )
    print(f"{Color.BOLD}{Color.HEADER}========================================={Color.RESET}\n")


if __name__ == "__main__":
    remove_suffix_from_files()
