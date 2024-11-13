from collections import Counter
import string
import re

first_tasks = [
    "Report System Time",
    "Report Billable Time",
    "Finish Task Manager",
    "Test Task Mananger",
]

# Decorator function to validate input
def validate_input(func):
    """Decorator to validate input is a non-empty string for functions with task descriptions"""
    def wrapper(*args):
        # Check if the function has at least one argument, and if the argument is a string
        task_description = args[1] if len(args) > 1 else args[0]
        if not isinstance(task_description, str) or not task_description.strip():
            raise ValueError("Task must be a non-empty string")
        return func(*args)
    return wrapper

# Add Task function
@validate_input
def add_task(task):
    """Adds a task to the list"""
    first_tasks.append(task)
    return f"Task '{task}' added."

# Delete Task function
def delete_task(num):
    """Removes a task from the list based on numeric value (starting at 1)"""
    index = num - 1  # Adjust for 1-based indexing
    if index < 0 or index >= len(first_tasks):
        return "Invalid task number."
    removed_task = first_tasks.pop(index)
    return f"Task '{removed_task}' removed."

# Display Tasks function
def show_tasks():
    """Displays all current tasks starting from 1 using the enumerate built-in"""
    if not first_tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(first_tasks, start=1):  # Start enumerate at 1
            print(f"{i}. {task}")

# Update Task function
@validate_input
def update_task(num, new_task):
    """Reprioritizes existing task by updating the specified task with new content"""
    index = num - 1  # Adjust for 1-based indexing
    if index < 0 or index >= len(first_tasks):
        return "Invalid task number."
    old_task = first_tasks[index]
    first_tasks[index] = new_task
    return f"Task '{old_task}' updated to '{new_task}'."

# Reprioritize Task function
def reprioritize_task(current_num, new_position):
    """Moves a task to a new position in the list, adjusting other tasks accordingly"""
    current_index = current_num - 1  # Convert to zero-based index
    new_index = new_position - 1     # Convert to zero-based index

    if current_index < 0 or current_index >= len(first_tasks):
        return "Invalid current task number."
    if new_index < 0 or new_index >= len(first_tasks):
        return "Invalid new position."

    # Remove the task from the current position
    task_to_move = first_tasks.pop(current_index)
    # Insert the task at the new position
    first_tasks.insert(new_index, task_to_move)
    
    return f"'{task_to_move}' moved to position {new_position}."

if __name__ == "__main__":
    while True:
        print("\nTask Manager")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Update Task")
        print("5. Reprioritize Task")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            show_tasks()
        elif choice == "2":
            task = input("Enter task to add: ")
            try:
                print(add_task(task))
            except ValueError as e:
                print(e)
        elif choice == "3":
            show_tasks()
            num = int(input("Enter task number to delete: "))
            print(delete_task(num))
        elif choice == "4":
            show_tasks()
            num = int(input("Enter task number to update: "))
            new_task = input("Enter new task description: ")
            try:
                print(update_task(num, new_task))
            except ValueError as e:
                print(e)
        elif choice == "5":
            show_tasks()
            current_num = int(input("Enter current task number to move: "))
            new_position = int(input("Enter new position for the task: "))
            print(reprioritize_task(current_num, new_position))
        elif choice == "6":
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid option, please try again.")
