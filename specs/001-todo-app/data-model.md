# Data Model: In-Memory Console Todo App

## Entities

### Todo
Represents a single task in the system.

| Field | Type | Description | Validation |
|-------|------|-------------|------------|
| id | int | Unique identifier | Positive integer, auto-incremented |
| text | str | Task description | Non-empty, max 200 chars |
| is_completed | bool | Status of task | Default: False |

## State Management

### TodoManager
- **Source of Truth**: `_todos: dict[int, Todo]`
- **Next ID**: `_next_id: int`

### Transitions
- `add_todo(text)`: Creates new Todo, increments next_id.
- `get_all_todos()`: Returns list of all todos.
- `mark_completed(id)`: Sets `is_completed=True` for matching ID.
- `update_todo(id, text)`: Updates text for matching ID.
- `delete_todo(id)`: Removes matching ID from dictionary.
