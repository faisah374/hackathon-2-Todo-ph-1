"""
Main application module for Phase-1 Console Todo App.

This module provides the console user interface including:
- Menu display and navigation
- User input prompts and validation loops
- Task display formatting
- Main application loop

Entry point: main() function
Run: python src/main.py
"""

from typing import Dict, Tuple, Optional, List

# Global state variables (module-level)
tasks: Dict[int, Dict] = {}  # Main storage: {task_id: task_dict}
next_id: int = 1  # Next ID to assign, never decrements


# Import validation functions
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from validation import validate_title, validate_description, validate_id, validate_menu_choice
from todo_operations import add_task, list_tasks, get_task, toggle_complete, update_task, delete_task


def display_menu() -> None:
    """Display the main menu with all available options."""
    print("\n=== Todo App Menu ===")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task Complete")
    print("6. Mark Task Incomplete")
    print("7. Exit")
    print()


def get_menu_choice() -> int:
    """
    Get and validate menu choice from user.

    Returns:
        Valid menu choice (1-7)
    """
    while True:
        choice_str = input("Enter your choice (1-7): ")
        valid, choice, error = validate_menu_choice(choice_str)
        if valid:
            return choice
        print(f"Error: {error}")


def prompt_for_title() -> str:
    """
    Prompt for task title and validate.

    Returns:
        Valid, stripped task title
    """
    while True:
        title = input("Enter task title: ")
        valid, error = validate_title(title)
        if valid:
            return title.strip()
        print(f"Error: {error}")


def prompt_for_description() -> str:
    """
    Prompt for task description and validate.

    Returns:
        Valid, stripped task description (or empty string)
    """
    while True:
        description = input("Enter description (optional): ")
        valid, error = validate_description(description)
        if valid:
            return description.strip()
        print(f"Error: {error}")


def handle_add_task() -> None:
    """Handle the Add Task operation."""
    global next_id
    title = prompt_for_title()
    description = prompt_for_description()
    task_id = add_task(tasks, next_id, title, description)
    next_id += 1
    print(f"Task #{task_id} added successfully")


def display_tasks(task_list: List[Dict]) -> None:
    """
    Display formatted task list.

    Args:
        task_list: List of task dictionaries
    """
    if not task_list:
        print("No tasks found. Add a task to get started.")
        return

    print(f"\n{'ID':<5} | {'Title':<30} | {'Description':<40} | {'Status':<10}")
    print("-" * 92)
    for task in task_list:
        status = "Completed" if task['completed'] else "Pending"
        title = task['title'][:30]  # Truncate if too long
        description = task['description'][:40]  # Truncate if too long
        print(f"{task['id']:<5} | {title:<30} | {description:<40} | {status:<10}")


def handle_view_tasks() -> None:
    """Handle the View All Tasks operation."""
    task_list = list_tasks(tasks)
    display_tasks(task_list)


def confirm_exit() -> bool:
    """
    Prompt for exit confirmation.

    Returns:
        True if user confirms exit, False to return to menu
    """
    while True:
        response = input("All data will be lost. Are you sure? (y/n): ").strip().lower()
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' or 'n'")


def handle_exit() -> bool:
    """
    Handle the Exit operation.

    Returns:
        True if should exit, False to return to menu
    """
    if confirm_exit():
        print("Goodbye!")
        return True
    return False


def prompt_for_id() -> int:
    """
    Prompt for task ID and validate.

    Returns:
        Valid task ID
    """
    while True:
        id_str = input("Enter task ID: ")
        valid, task_id, error = validate_id(id_str, tasks)
        if valid:
            return task_id
        print(f"Error: {error}")


def handle_mark_complete() -> None:
    """Handle the Mark Task Complete operation."""
    task_id = prompt_for_id()
    task = get_task(tasks, task_id)
    if task:
        task['completed'] = True
        print(f"Task #{task_id} marked as complete")
    else:
        print(f"Task #{task_id} not found")


def handle_mark_incomplete() -> None:
    """Handle the Mark Task Incomplete operation."""
    task_id = prompt_for_id()
    task = get_task(tasks, task_id)
    if task:
        task['completed'] = False
        print(f"Task #{task_id} marked as incomplete")
    else:
        print(f"Task #{task_id} not found")


def prompt_for_update_title(current_title: str) -> Optional[str]:
    """
    Prompt for updated title.

    Args:
        current_title: Current task title for reference

    Returns:
        New title if provided, None to keep current
    """
    title = input(f"Enter new title (or press Enter to keep current: '{current_title}'): ")
    if not title.strip():
        return None
    valid, error = validate_title(title)
    if valid:
        return title.strip()
    print(f"Error: {error}")
    return prompt_for_update_title(current_title)


def prompt_for_update_description(current_description: str) -> Optional[str]:
    """
    Prompt for updated description.

    Args:
        current_description: Current task description for reference

    Returns:
        New description if provided, None to keep current
    """
    description = input(f"Enter new description (or press Enter to keep current: '{current_description}'): ")
    if not description.strip():
        return None
    valid, error = validate_description(description)
    if valid:
        return description.strip()
    print(f"Error: {error}")
    return prompt_for_update_description(current_description)


def handle_update_task() -> None:
    """Handle the Update Task operation."""
    task_id = prompt_for_id()
    task = get_task(tasks, task_id)
    if not task:
        print(f"Task #{task_id} not found")
        return

    new_title = prompt_for_update_title(task['title'])
    new_description = prompt_for_update_description(task['description'])

    final_title = new_title if new_title is not None else task['title']
    final_description = new_description if new_description is not None else task['description']

    if update_task(tasks, task_id, final_title, final_description):
        print(f"Task #{task_id} updated successfully")
    else:
        print(f"Task #{task_id} not found")


def handle_delete_task() -> None:
    """Handle the Delete Task operation."""
    task_id = prompt_for_id()
    if delete_task(tasks, task_id):
        print(f"Task #{task_id} deleted successfully")
    else:
        print(f"Task #{task_id} not found")


def main() -> None:
    """Main application loop."""
    while True:
        display_menu()
        choice = get_menu_choice()

        if choice == 1:
            handle_add_task()
        elif choice == 2:
            handle_view_tasks()
        elif choice == 3:
            handle_update_task()
        elif choice == 4:
            handle_delete_task()
        elif choice == 5:
            handle_mark_complete()
        elif choice == 6:
            handle_mark_incomplete()
        elif choice == 7:
            if handle_exit():
                break


if __name__ == "__main__":
    main()
