import shutil
import os

# Create sample directory and files
os.makedirs("example_dir/sub_dir", exist_ok=True)
with open("example_dir/file1.txt", "w") as f:
    f.write("This is file 1.")
with open("example_dir/file2.txt", "w") as f:
    f.write("This is file 2.")

shutil.copy("example_dir/file1.txt", "example_dir/file1_copy.txt")

# Copy file with metadata
shutil.copy2("example_dir/file1.txt", "example_dir/file1_copy2.txt")

# Copy directory tree
shutil.copytree("example_dir", "example_dir_copy")

shutil.move("example_dir/file2.txt", "example_dir/sub_dir/file2_moved.txt")

# Remove directory tree
shutil.rmtree("example_dir_copy")

# Archive a directory tree into a zip file
shutil.make_archive("example_dir_archive", "zip", "example_dir")

# Extract an archive
shutil.unpack_archive("example_dir_archive.zip", "extracted_dir")

# Disk usage statistics
total, used, free = shutil.disk_usage("/")
print(f"Total: {total // (2**30)} GiB")
print(f"Used: {used // (2**30)} GiB")
print(f"Free: {free // (2**30)} GiB")

# Deprecated functions:
# shutil.get_archive_formats() and shutil.register_archive_format() are not deprecated but less commonly used.
# shutil.get_unpack_formats() and shutil.register_unpack_format() are also less commonly used.

# Clean up created files and directories for demonstration purposes
shutil.rmtree("example_dir")
shutil.rmtree("extracted_dir")
os.remove("example_dir_archive.zip")
