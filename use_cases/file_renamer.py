import os
import shutil
import re

# Configuration variables
SOURCE_DIR = "data/pictures/1_raw"
OUTPUT_DIR = "data/pictures/2_converted"
OUTLIERS_DIR = "data/pictures/2_converted/Outliers"

def setup_directories():
    """Create output directories if they don't exist"""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(OUTLIERS_DIR, exist_ok=True)

def is_lastname_firstname_format(filename):
    """Check if filename matches 'lastname, firstname' pattern"""
    name_part = os.path.splitext(filename)[0]
    return re.match(r'^[^,]+,\s*[^,]+$', name_part) is not None

def convert_filename(filename):
    """Convert 'lastname, firstname.ext' to 'firstname lastname.ext'"""
    name_part, extension = os.path.splitext(filename)
    if ',' in name_part:
        parts = name_part.split(',')
        lastname = parts[0].strip()
        firstname = parts[1].strip()
        return f"{firstname} {lastname}{extension}"
    return filename

def process_files(source_dir=SOURCE_DIR, output_dir=OUTPUT_DIR, outliers_dir=OUTLIERS_DIR):
    """Process all files in the source directory"""
    if not os.path.exists(source_dir):
        print(f"Source directory '{source_dir}' does not exist")
        return
    
    setup_directories()

    for filename in os.listdir(source_dir):
        source_path = os.path.join(source_dir, filename)

        # Skip directories
        if os.path.isdir(source_path):
            continue
        
        if is_lastname_firstname_format(filename):
            # Convert and move to output directory
            new_filename = convert_filename(filename)
            destination_path = os.path.join(output_dir, new_filename)
            shutil.copy2(source_path, destination_path)
            print(f"Converted: {filename} -> {new_filename}")
        else:
            # Move to outliers directory for manual review
            outlier_path = os.path.join(outliers_dir, filename)
            shutil.copy2(source_path, outlier_path)
            print(f"Outlier: {filename} -> moved to Outliers folder")

if __name__ == "__main__":
    process_files(source_dir=SOURCE_DIR, output_dir=OUTPUT_DIR, outliers_dir=OUTLIERS_DIR)