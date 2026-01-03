# Phase-1 Console Todo App

A fully functional in-memory console todo application built with Python 3.13+, following strict Phase-1 constraints and Spec-Driven Development workflow.

## Features

- ✅ **Add Task** - Create tasks with title (1-200 chars) and optional description (0-1000 chars)
- ✅ **View All Tasks** - Display all tasks in formatted table with ID, title, description, and status
- ✅ **Mark Complete/Incomplete** - Toggle task completion status between Pending and Completed
- ✅ **Update Task** - Edit task title and/or description with optional updates
- ✅ **Delete Task** - Remove tasks from memory with ID preservation (no reuse)
- ✅ **Exit Application** - Clean exit with data loss warning and confirmation

## Phase-1 Constraints

This implementation adheres to strict Phase-1 constraints:

- **In-memory only** - No persistence, all data lost on exit
- **Console/terminal only** - No web interfaces, pure command-line interface
- **Python 3.13+** - Minimum Python version requirement
- **Standard library only** - No external dependencies for core functionality
- **Single-user, single-process** - No concurrency or multi-user support

## Requirements

- **Python 3.13 or higher** (tested with Python 3.14.0)
- No external dependencies required for running the application
- Optional: pytest for running unit tests (development only)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/faisah374/hackathon-2-Todo-ph-1.git
   cd hackathon-2-Todo-ph-1
   ```

2. **Verify Python version**:
   ```bash
   python --version
   ```
   Ensure you have Python 3.13 or higher installed.

3. **No dependencies to install** - The application uses only Python's standard library!

## Usage

### Running the Application

Start the interactive console application:

```bash
python src/main.py
```

### Main Menu

When you run the application, you'll see the main menu:

```
=== Todo App Menu ===
1. Add Task
2. View All Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete
6. Mark Task Incomplete
7. Exit
```

### Example Workflow

1. **Add a task**:
   - Select option `1`
   - Enter task title: `Buy groceries`
   - Enter description (optional): `Milk, bread, eggs`
   - Task created with auto-generated ID

2. **View all tasks**:
   - Select option `2`
   - See formatted table with all tasks

3. **Mark task complete**:
   - Select option `5`
   - Enter task ID: `1`
   - Task status changes to "Completed"

4. **Update a task**:
   - Select option `3`
   - Enter task ID
   - Enter new title (or press Enter to keep current)
   - Enter new description (or press Enter to keep current)

5. **Delete a task**:
   - Select option `4`
   - Enter task ID
   - Task removed from list

6. **Exit**:
   - Select option `7`
   - Confirm exit (all data will be lost)

## Testing

### Run Automated Tests

Execute the comprehensive test suite:

```bash
python test_workflow.py
```

This runs 12 automated tests covering:
- Adding tasks with various inputs
- Viewing tasks in formatted output
- Marking tasks complete/incomplete
- Updating task details
- Deleting tasks
- ID preservation (deleted IDs not reused)
- All validation rules
- Empty state handling
- Edge cases

**Expected output**: All 12 tests should pass with `[PASS]` status.

### Manual Testing

Test the application interactively by running `python src/main.py` and trying different operations.

## Architecture

### 3-Module Design

The application is organized into three clean modules:

1. **`src/validation.py`** (95 lines)
   - Input validation and sanitization
   - 4 validation functions:
     - `validate_title()` - Title validation (1-200 chars, required)
     - `validate_description()` - Description validation (0-1000 chars, optional)
     - `validate_id()` - Task ID validation (must exist)
     - `validate_menu_choice()` - Menu choice validation (1-7 range)

2. **`src/todo_operations.py`** (122 lines)
   - Business logic for CRUD operations
   - 6 core functions:
     - `add_task()` - Create new task
     - `get_task()` - Retrieve task by ID
     - `list_tasks()` - Get all tasks sorted by ID
     - `update_task()` - Modify task title/description
     - `delete_task()` - Remove task from memory
     - `toggle_complete()` - Toggle task completion status

3. **`src/main.py`** (281 lines)
   - Console UI, menu system, and main application loop
   - 15+ functions including:
     - Menu display and navigation
     - User input prompts with validation loops
     - Task display formatting
     - Main application loop

### Key Technical Decisions

- **Dictionary-based storage** (`Dict[int, Dict]`) for O(1) task lookup
- **Auto-incrementing IDs** starting from 1, never reused after deletion
- **Validate-retry loops** for robust user input handling
- **Type hints** on all function signatures using `typing` module
- **Comprehensive docstrings** following Python conventions
- **Separation of concerns** between validation, business logic, and UI

### Data Model

Each task is stored as a dictionary with the following structure:

```python
{
    "id": int,              # Auto-incremented unique ID
    "title": str,           # Task title (1-200 chars)
    "description": str,     # Task description (0-1000 chars)
    "completed": bool       # Completion status (default: False)
}
```

Tasks are stored in a module-level dictionary: `tasks: Dict[int, Dict]`

## Validation Rules

The application enforces the following validation rules:

- **Title**: Required, 1-200 characters after stripping whitespace
- **Description**: Optional, 0-1000 characters after stripping whitespace
- **Task ID**: Must be a valid integer and must exist in the task list
- **Menu Choice**: Must be an integer between 1-7

All validation errors display helpful messages and allow the user to retry input.

## Project Structure

```
hackathon-2-Todo-ph-1/
├── src/
│   ├── __init__.py
│   ├── main.py                 # Console UI and main application loop
│   ├── todo_operations.py      # Business logic (CRUD operations)
│   └── validation.py           # Input validation functions
├── specs/
│   └── 002-console-todo/
│       ├── spec.md             # Feature specification
│       ├── plan.md             # Implementation plan
│       ├── tasks.md            # Task breakdown
│       ├── data-model.md       # Data model documentation
│       └── research.md         # Research findings
├── history/
│   └── prompts/                # Prompt History Records (PHRs)
├── tests/                      # Unit tests (optional)
├── test_workflow.py            # Automated integration tests
├── .gitignore                  # Git ignore rules
├── pytest.ini                  # Pytest configuration
└── README.md                   # This file
```

## Documentation

Complete documentation is available in the `specs/` directory:

- **Specification** (`specs/002-console-todo/spec.md`): 6 user stories, 18 acceptance scenarios, 15 functional requirements
- **Implementation Plan** (`specs/002-console-todo/plan.md`): Architecture decisions, research findings, data model
- **Task Breakdown** (`specs/002-console-todo/tasks.md`): 52 dependency-ordered implementation tasks
- **Constitution** (`.specify/memory/constitution.md`): Project governance rules and Phase-1 constraints

## Development Workflow

This project was built using **Spec-Driven Development (SDD)** workflow:

1. **Constitution** → Define project principles and constraints
2. **Specification** → Document user stories and requirements
3. **Planning** → Design architecture and data model
4. **Tasks** → Break down implementation into actionable tasks
5. **Implementation** → Execute tasks in dependency order
6. **Testing** → Verify all functionality works correctly

All development history is documented in Prompt History Records (PHRs) in the `history/prompts/` directory.

## Known Limitations

As this is a Phase-1 implementation, the following limitations are intentional:

- **No persistence** - All data is lost when the application exits
- **No file storage** - Tasks are stored in memory only
- **Single session** - Cannot save/load tasks between sessions
- **No undo/redo** - Changes are immediate and irreversible (until exit)
- **No search/filter** - Must view all tasks at once
- **No task priorities** - All tasks are equal priority
- **No due dates** - Tasks have no time-based attributes
- **No categories/tags** - No task organization beyond the list

These limitations are by design for Phase-1 and can be addressed in future phases.

## Future Enhancements (Phase-2+)

Potential enhancements for future phases:

- **Persistence** - Save tasks to JSON or SQLite database
- **Search and Filter** - Find tasks by title, status, or other criteria
- **Task Priorities** - Support for high/medium/low priority levels
- **Due Dates** - Add deadlines and time-based task management
- **Categories/Tags** - Organize tasks with custom tags
- **Task History** - Track changes and modifications to tasks
- **Undo/Redo** - Revert recent changes
- **Multi-user Support** - Share task lists across users
- **Web Interface** - Browser-based UI as alternative to console

## Contributing

This is a Phase-1 implementation following strict constraints. Contributions should maintain:

- Python 3.13+ compatibility
- Standard library only (no external dependencies for core features)
- Type hints on all functions
- Comprehensive docstrings
- Adherence to validation rules
- Separation of concerns (validation, business logic, UI)

## License

This project is part of a hackathon implementation demonstrating Spec-Driven Development principles.

## Credits

Built with [Claude Code](https://claude.com/claude-code) following Spec-Driven Development (SDD) workflow.

**Development Statistics**:
- 52 implementation tasks completed
- 12/12 automated tests passed (100% pass rate)
- 3 core modules (498 lines of code)
- 30+ documentation files
- 100% Phase-1 constraint compliance

---

**Version**: Phase-1 (v1.0.0)
**Status**: ✅ Complete and fully functional
**Last Updated**: 2026-01-04
