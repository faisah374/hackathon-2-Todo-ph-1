import pytest
from src.manager import TodoManager

def test_add_todo():
    manager = TodoManager()
    todo_id = manager.add_todo("Buy milk")
    assert todo_id == 1
    assert len(manager.get_all_todos()) == 1
    assert manager.get_all_todos()[0].text == "Buy milk"

def test_get_all_todos_empty():
    manager = TodoManager()
    assert len(manager.get_all_todos()) == 0

def test_mark_completed():
    manager = TodoManager()
    todo_id = manager.add_todo("Test")
    assert manager.mark_completed(todo_id) is True
    assert manager.get_all_todos()[0].is_completed is True

def test_mark_completed_not_found():
    manager = TodoManager()
    assert manager.mark_completed(99) is False

def test_update_todo():
    manager = TodoManager()
    todo_id = manager.add_todo("Old")
    assert manager.update_todo(todo_id, "New") is True
    assert manager.get_all_todos()[0].text == "New"

def test_delete_todo():
    manager = TodoManager()
    todo_id = manager.add_todo("Delete me")
    assert manager.delete_todo(todo_id) is True
    assert len(manager.get_all_todos()) == 0
