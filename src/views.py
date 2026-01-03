from typing import List
from src.models import Todo

def format_todo(todo: Todo) -> str:
    """Formats a single todo for display."""
    status = "[X]" if todo.is_completed else "[ ]"
    return f"{status} {todo.id}: {todo.text}"

def format_todo_list(todos: List[Todo]) -> str:
    """Formats a list of todos for display."""
    if not todos:
        return "No tasks found."
    return "\n".join(format_todo(t) for t in todos)

def help_menu() -> str:
    """Returns the help message."""
    return """
Available commands:
  add <text>            - Add a new task
  list                  - List all tasks
  complete <id>         - Mark a task as completed
  update <id> <text>    - Update task description
  delete <id>           - Remove a task
  exit                  - Exit the application
  help                  - Show this menu
"""
