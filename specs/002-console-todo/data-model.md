# Data Model: Phase-1 Console Todo App

**Feature**: 002-console-todo
**Date**: 2026-01-04
**Related**: [spec.md](./spec.md) | [plan.md](./plan.md)

## Overview

Phase-1 uses a minimal in-memory data model with a single entity type (Task) stored in a Python dictionary. No persistence, no relationships, no complex data structures.

## Entities

### Task

**Description**: Represents a single todo item in the user's task list.

**Storage**: Dictionary value in module-level `tasks` dict, keyed by integer ID.

**Attributes**:

| Attribute | Type | Constraints | Default | Description |
|-----------|------|-------------|---------|-------------|
| `id` | `int` | Unique, auto-increment, immutable, >= 1 | Assigned by system | Task identifier, never reused after deletion |
| `title` | `str` | Required, 1-200 characters (after trim) | None (user input) | Task description/name |
| `description` | `str` | Optional, 0-1000 characters (after trim) | `""` (empty string) | Additional task details |
| `completed` | `bool` | True or False | `False` | Completion status |

**Validation Rules**:

- **id**: System-assigned, starts at 1, increments for each new task, never decreases or reuses
- **title**:
  - Strip leading/trailing whitespace before validation
  - After stripping, must be 1-200 characters
  - Cannot be empty or whitespace-only
  - Supports Unicode (UTF-8)
- **description**:
  - Strip leading/trailing whitespace before validation
  - After stripping, must be 0-1000 characters
  - Empty string is valid
  - Supports Unicode (UTF-8)
- **completed**:
  - Boolean only
  - Toggleable via menu operations
  - Default False for new tasks

**Python Representation**:

```python
# Example task in memory
task = {
    "id": 1,
    "title": "Buy groceries",
    "description": "Milk, bread, eggs",
    "completed": False
}
```

**Invariants**:

1. Task ID is immutable once assigned
2. Task ID never reused (even after deletion)
3. All tasks have a title (never None or empty after validation)
4. Description can be empty string but never None
5. Completed is always Boolean (never None)

## Application State

**Global State Variables** (module-level in todo_operations.py or main.py):

```python
tasks: dict[int, dict] = {}  # Main storage: {task_id: task_dict}
next_id: int = 1             # Next ID to assign, never decrements
```

**State Transitions**:

1. **Add Task**:
   - Before: `tasks = {}`, `next_id = 1`
   - After: `tasks = {1: {...}}`, `next_id = 2`

2. **Delete Task**:
   - Before: `tasks = {1: {...}, 2: {...}}`, `next_id = 3`
   - After: `tasks = {2: {...}}`, `next_id = 3` (unchanged)

3. **Toggle Complete**:
   - Before: `tasks[1]["completed"] = False`
   - After: `tasks[1]["completed"] = True`

4. **Update Task**:
   - Before: `tasks[1] = {"id": 1, "title": "Old", "description": "...", "completed": False}`
   - After: `tasks[1] = {"id": 1, "title": "New", "description": "...", "completed": False}`
   - Note: ID and completed status unchanged

## Data Flow

```
User Input (stdin)
    ↓
Validation Layer (validation.py)
    ↓
Business Logic (todo_operations.py)
    ↓
In-Memory Storage (tasks dict)
    ↓
Display Logic (main.py)
    ↓
User Output (stdout)
```

**Example: Add Task Flow**:

1. User enters title "Buy groceries" at prompt
2. `validate_title("Buy groceries")` → (True, None)
3. User enters description "Milk, bread, eggs"
4. `validate_description("Milk, bread, eggs")` → (True, None)
5. `add_task(tasks, next_id, "Buy groceries", "Milk, bread, eggs")`
6. Creates: `tasks[1] = {"id": 1, "title": "Buy groceries", "description": "Milk, bread, eggs", "completed": False}`
7. Increments: `next_id = 2`
8. Returns: 1 (new task ID)
9. Display: "Task #1 added successfully"

## Storage Characteristics

**Capacity**:
- Theoretical max: Limited by Python dict capacity (millions of items)
- Practical target: 100+ tasks (per spec SC-004)
- Memory footprint: ~200-300 bytes per task (approximate)

**Performance**:
- Lookup by ID: O(1) - dictionary key access
- List all tasks: O(n) - iterate dict values
- Add task: O(1) - dict insertion
- Delete task: O(1) - dict deletion
- Update task: O(1) - dict value update

**Persistence**:
- NONE - all data lost on application exit
- No serialization, no file I/O, no database
- Users warned on exit: "All data will be lost"

## Edge Cases

1. **Empty Task List**:
   - `tasks = {}`, `next_id = 1`
   - View operation displays: "No tasks found. Add a task to get started."

2. **After Deleting All Tasks**:
   - `tasks = {}`, `next_id = N` (where N > 1)
   - next_id preserves history, never resets

3. **Large Task Count (100+)**:
   - Dictionary performance remains O(1) for operations
   - Display may scroll beyond screen (expected behavior)

4. **Unicode Content**:
   - Full UTF-8 support in title and description
   - Emojis, international characters allowed

5. **Maximum Length Inputs**:
   - Title at 200 chars: Accepted
   - Description at 1000 chars: Accepted
   - Title at 201 chars: Rejected with error

6. **ID Gaps After Deletion**:
   - Example: Delete task #2 from {1, 2, 3}
   - Result: tasks = {1, 3}, next_id = 4
   - IDs 1 and 3 remain, #2 never reused

## No Relationships

Phase-1 has a single entity with no relationships:
- No users (single-user app)
- No categories/tags
- No task dependencies
- No subtasks
- No priority levels

All relationship features deferred to Phase-2+.

## Migration Path (Phase-2)

When adding persistence in Phase-2:
- Task dict structure remains compatible
- Add created_at, updated_at timestamps
- Add user_id for multi-user support
- Convert to SQLModel/SQLAlchemy models
- Maintain ID uniqueness across sessions

Current Phase-1 structure deliberately simple to ease Phase-2 migration.
