import os
import shutil


downloads_folder = r"C:\Users\myUser\Downloads"

file_categories = {
    "PDFs": ["pdf"],
    "Word documents": ["doc", "docx"],
    "Excel documents": ["xls", "xlsx", "xlsb", "csv"],
    "Powerpoint documents": ["ppt", "pptx"],
    "Text documents": ["txt"],
    "Executables": ["exe", "msi", "bat", "sh"],
    "Media": ["mp3", "wav", "mp4", "mkv", "avi", "mov"],
    "Archives": ["zip", "rar", "7z", "tar", "gz"],
    "Images": ["jpg", "jpeg", "png", "gif", "bmp", "tiff", "webp"],
    "Code": ["py", "js", "html", "css", "java", "cpp", "c", "cs", "sql"],
}

if not os.path.exists(downloads_folder):
    print("Source folder not found!")
    exit()

for category in file_categories.keys():
    category_path = os.path.join(downloads_folder, category)
    os.makedirs(category_path, exist_ok=True)

misc_folder = os.path.join(downloads_folder, "MISC")
os.makedirs(misc_folder, exist_ok=True)

for file_name in os.listdir(downloads_folder):
    file_path = os.path.join(downloads_folder, file_name)

    # Skip directories
    if os.path.isdir(file_path):
        continue

    file_extension = file_name.split(".")[-1].lower() if "." in file_name else ""

    # Set default folder
    destination_folder = misc_folder

    for category, extensions in file_categories.items():
        if file_extension in extensions:
            destination_folder = os.path.join(downloads_folder, category)
            break

    # Move the file
    shutil.move(file_path, os.path.join(destination_folder, file_name))

print("Folder organization complete!")
