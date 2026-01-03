"""
Business logic module for Phase-1 Console Todo App.

This module provides core CRUD operations for todo tasks:
- add_task: Create new task with auto-incremented ID
- get_task: Retrieve task by ID
- update_task: Modify existing task title/description
- delete_task: Remove task from memory
- toggle_complete: Toggle task completion status
- list_tasks: Return sorted list of all tasks

All tasks are stored in memory only using Python dictionaries.
"""

from typing import Dict, List, Optional


def add_task(tasks: Dict[int, Dict], next_id: int, title: str, description: str) -> int:
    """
    Create a new task and add to tasks dictionary.

    Args:
        tasks: Tasks dictionary
        next_id: Next available task ID
        title: Task title (already validated and stripped)
        description: Task description (already validated and stripped)

    Returns:
        The new task ID
    """
    task_id = next_id
    tasks[task_id] = {
        "id": task_id,
        "title": title,
        "description": description,
        "completed": False
    }
    return task_id


def list_tasks(tasks: Dict[int, Dict]) -> List[Dict]:
    """
    Return sorted list of all tasks.

    Args:
        tasks: Tasks dictionary

    Returns:
        List of task dicts sorted by ID
    """
    return sorted(tasks.values(), key=lambda t: t['id'])


def get_task(tasks: Dict[int, Dict], task_id: int) -> Optional[Dict]:
    """
    Retrieve task by ID.

    Args:
        tasks: Tasks dictionary
        task_id: Task ID to retrieve

    Returns:
        Task dictionary if found, None otherwise
    """
    return tasks.get(task_id)


def toggle_complete(tasks: Dict[int, Dict], task_id: int) -> bool:
    """
    Toggle task completion status.

    Args:
        tasks: Tasks dictionary
        task_id: Task ID to toggle

    Returns:
        True if successful, False if task not found
    """
    task = tasks.get(task_id)
    if task is None:
        return False
    task['completed'] = not task['completed']
    return True


def update_task(tasks: Dict[int, Dict], task_id: int, new_title: str, new_description: str) -> bool:
    """
    Update existing task title and/or description.

    Args:
        tasks: Tasks dictionary
        task_id: Task ID to update
        new_title: New title (already validated and stripped)
        new_description: New description (already validated and stripped)

    Returns:
        True if successful, False if task not found
    """
    task = tasks.get(task_id)
    if task is None:
        return False
    task['title'] = new_title
    task['description'] = new_description
    return True


def delete_task(tasks: Dict[int, Dict], task_id: int) -> bool:
    """
    Delete task from memory.

    Args:
        tasks: Tasks dictionary
        task_id: Task ID to delete

    Returns:
        True if successful, False if task not found
    """
    if task_id in tasks:
        del tasks[task_id]
        return True
    return False
