"""
Validation module for Phase-1 Console Todo App.

This module provides input validation functions for user inputs including:
- Task titles (1-200 characters, required)
- Task descriptions (0-1000 characters, optional)
- Task IDs (integer, must exist in tasks dict)
- Menu choices (1-7 range)

All validation functions return tuples indicating success/failure with error messages.
"""

from typing import Dict, Tuple, Optional


def validate_title(title: str) -> Tuple[bool, Optional[str]]:
    """
    Validate task title.

    Args:
        title: Raw title input from user

    Returns:
        Tuple of (is_valid, error_message)
        - (True, None) if valid
        - (False, error_message) if invalid
    """
    stripped = title.strip()
    if not stripped:
        return (False, "Title is required")
    if len(stripped) > 200:
        return (False, "Title must be 1-200 characters")
    return (True, None)


def validate_description(description: str) -> Tuple[bool, Optional[str]]:
    """
    Validate task description.

    Args:
        description: Raw description input from user

    Returns:
        Tuple of (is_valid, error_message)
        - (True, None) if valid
        - (False, error_message) if invalid
    """
    stripped = description.strip()
    if len(stripped) > 1000:
        return (False, "Description must be 0-1000 characters")
    return (True, None)


def validate_id(id_str: str, tasks: Dict[int, Dict]) -> Tuple[bool, Optional[int], Optional[str]]:
    """
    Validate and parse task ID.

    Args:
        id_str: Raw ID input from user
        tasks: Tasks dictionary to check existence

    Returns:
        Tuple of (is_valid, task_id, error_message)
        - (True, task_id, None) if valid
        - (False, None, error_message) if invalid
    """
    try:
        task_id = int(id_str.strip())
        if task_id not in tasks:
            return (False, None, f"Task #{task_id} not found")
        return (True, task_id, None)
    except ValueError:
        return (False, None, "Invalid ID. Please enter a number")


def validate_menu_choice(choice_str: str) -> Tuple[bool, Optional[int], Optional[str]]:
    """
    Validate menu choice.

    Args:
        choice_str: Raw choice input from user

    Returns:
        Tuple of (is_valid, choice, error_message)
        - (True, choice, None) if valid (1-7)
        - (False, None, error_message) if invalid
    """
    try:
        choice = int(choice_str.strip())
        if choice < 1 or choice > 7:
            return (False, None, "Invalid choice. Please enter a number from the menu (1-7)")
        return (True, choice, None)
    except ValueError:
        return (False, None, "Invalid choice. Please enter a number from the menu (1-7)")
