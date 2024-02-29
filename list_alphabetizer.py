import re


def sort_lists_in_file_mixed_comments(file_path):
    """
    This script focuses on correctly extracting both commented and uncommented items in a list,
    sorting indiscriminantly, and preserving these markers in the sorted output.
    The re.findall() function is used to match list names and their contents accurately,
    and the loop unpacks these matches as two elements per iteration.
    Adjust the path of the target file.
    """

    def extract_and_sort_items(list_content):
        # Extract all items, preserving their commented or uncommented format
        items = re.findall(r'\s*(#?\s*".+?",?)', list_content, flags=re.DOTALL)
        # Sort items by their content, ignoring comment markers for sorting
        sorted_items = sorted(items, key=lambda x: x.lstrip("#").strip().lower())
        return "\n".join(sorted_items)

    # Read the original file content
    with open(file_path, "r") as file:
        content = file.read()

    # Regex to find list assignments and capture list name and its content
    list_assignments = re.findall(r"(\w+)\s*=\s*\[((?:.|\n)*?)\]", content, flags=re.DOTALL)

    for list_name, list_body in list_assignments:
        # Sort the list items, including handling commented items correctly
        sorted_list_body = extract_and_sort_items(list_body)
        # Construct the new list assignment with sorted items
        new_list_assignment = f"{list_name} = [\n{sorted_list_body}\n]"
        # Replace the original list in the content with its sorted version
        content = re.sub(
            rf"{list_name}\s*=\s*\[.*?\]", new_list_assignment, content, flags=re.DOTALL
        )

    # Write the modified content back to the file
    with open(file_path, "w") as file:
        file.write(content)


# Replace 'your_path/unordered_list.py' with the actual path to your file
sort_lists_in_file_mixed_comments("long_list_unsorted.py")


"""
SAMPLE LISTS

students = [
    "Olivia",
    # "Blake",
    "Chris",
    # "Alex",
]

departments = [
    "Engineer",
    # "Marketing",
    "Accounting",
]
"""
