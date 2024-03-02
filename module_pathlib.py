import pathlib

# Path class:
# This is the primary entry point when working with the pathlib module.
""" Use case: Imagine you're working with data files that you regularly analyze.
    You might use the Path class to generate file paths dynamically."""

data_directory = pathlib.Path("C:/data/nashville/")
report_file = data_directory / "monthly_report.csv"
print(report_file)
# Outputs: C:\data\nashville\monthly_report.csv


# PurePath classes:
# These are base classes containing pure path operations without any I/O operations.
""" Description: Description: Classes for pure (non I/O) path operations,
    with PurePosixPath and PureWindowsPath being platform-specific representations.
    
    Use case: You're developing a cross-platform tool and need to generate
    platform-specific paths without actually accessing the filesystem."""

posix_path = pathlib.PurePosixPath("/etc/hosts")
win_path = pathlib.PureWindowsPath("C:/Windows/System32/drivers/etc/hosts")
print(posix_path, win_path)
# Outputs: /etc/hosts C:\Windows\System32\drivers\etc\hosts


# Path methods:
# Path.cwd() returns the current working directory as a new path object.
current_dir = pathlib.Path.cwd()
print(f"Running the script from: {current_dir}")

# Path.home() returns the home directory as a new path object.
backup_dir = pathlib.Path.home() / "backup_files"
# backup_dir.mkdir(exist_ok=True)

# Path.glob() iterates over the directory contents and yields path objects matching the given pattern.
# Use case: a BI developer needs to process all CSV files in a directory.

data_dir = pathlib.Path("C:/data/reports/")
for csv_file in data_dir.glob("*.csv"):
    print(f"Processing file: {csv_file.name}")

# Path.mkdir() Description: Creates a new directory at the given path.
# Use case: Setting up a new project and creating directories for different data sets.

project_dir = pathlib.Path("C:/projects/baseball_analysis/")
datasets_dir = project_dir / "datasets"
# datasets_dir.mkdir(parents=True, exist_ok=True)

# Path.exists() checks if the path exists.
# Use case: check if config file exists before attempting to read it.

config_path = pathlib.Path("C:/app/config.ini")
if config_path.exists():
    print("Configuration file exists.")
else:
    print("Configuration file not found.")


# Path.is_dir() checks if the path is a directory.
# Use case: When writing a script to clean up empty directories in a specific folder.

data_dir = pathlib.Path("C:/data/reports/")
for item in data_dir.iterdir():
    if item.is_dir() and not any(item.iterdir()):
        item.rmdir()
        print(f"Removed empty directory: {item}")

# Path.is_file() checks if the path is a file.
# Use case: Ensure a log file exists before appending to it.

log_path = pathlib.Path("C:/app/logs/app.log")
if log_path.is_file():
    with log_path.open("a") as log_file:
        log_file.write("New entry\n")

# Path.unlink() removes the file or symbolic link.
# Use case: Removing outdated files as part of a data retention policy.

report_path = pathlib.Path("C:/data/reports/old_report.csv")
if report_path.exists():
    report_path.unlink()
    print("Old report removed.")

# Path.rmdir() removes the directory. The directory must be empty.
# Use case: After processing and moving data files, clean up any remaining empty directories.

empty_dir = pathlib.Path("C:/data/processed/old_data/")
if empty_dir.is_dir() and not any(empty_dir.iterdir()):
    empty_dir.rmdir()
    print("Removed empty data directory.")

# Path.iterdir() iterates over the directory, yielding each entry as a new Path object.
# Description: Returns an iterator yielding the path objects of the directory contents.
# Use case: List all files in a directory to audit the data files present.

data_dir = pathlib.Path("C:/data/new_entries/")
for entry in data_dir.iterdir():
    print(entry.name)

# Path.rename() renames the file or directory to the given path.
# Use case: Organize files by renaming them according to a new naming convention.

original_file = pathlib.Path("C:/reports/summary.txt")
new_file = pathlib.Path("C:/reports/2024_summary_report.txt")
original_file.rename(new_file)
print(f"File renamed to {new_file}")

# Path.touch() creates a file at this given path. If the file exists, it updates the modification time.
# Use case: Ensure a log file exists before starting a new session of logging.

log_file = pathlib.Path("C:/app/logs/session.log")
log_file.touch(exist_ok=True)
print("Log file is ready.")
