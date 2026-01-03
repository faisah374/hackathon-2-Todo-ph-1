from typing import Dict, List
from src.models import Todo

class TodoManager:
    """Business logic for managing todos in memory."""
    def __init__(self) -> None:
        self._todos: Dict[int, Todo] = {}
        self._next_id: int = 1

    def add_todo(self, text: str) -> int:
        """Creates a new Todo and returns its ID."""
        todo_id = self._next_id
        self._todos[todo_id] = Todo(id=todo_id, text=text)
        self._next_id += 1
        return todo_id

    def get_all_todos(self) -> List[Todo]:
        """Returns a list of all todos."""
        return list(self._todos.values())

    def mark_completed(self, todo_id: int) -> bool:
        """Sets is_completed=True for matching ID. Returns success."""
        if todo_id in self._todos:
            self._todos[todo_id].is_completed = True
            return True
        return False

    def update_todo(self, todo_id: int, text: str) -> bool:
        """Updates text for matching ID. Returns success."""
        if todo_id in self._todos:
            self._todos[todo_id].text = text
            return True
        return False

    def delete_todo(self, todo_id: int) -> bool:
        """Removes matching ID from dictionary. Returns success."""
        if todo_id in self._todos:
            del self._todos[todo_id]
            return True
        return False
