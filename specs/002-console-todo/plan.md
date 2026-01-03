# Implementation Plan: Phase-1 Console Todo App

**Branch**: `002-console-todo` | **Date**: 2026-01-04 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/002-console-todo/spec.md`

## Summary

Build an in-memory, console-based Todo application in Python 3.13+ using only the standard library. The application provides a numbered menu interface for managing todo tasks (add, view, update, delete, mark complete/incomplete, exit). All data is stored in memory using Python dictionaries and lost on exit. Focus on simplicity, deterministic behavior, and robust input validation with clear user feedback.

**Technical Approach**: Single-file or minimal-file Python application with functional programming style, using dictionaries for task storage keyed by auto-incrementing IDs. Menu-driven interface with input validation loops, clear separation between UI (input/output), business logic (task operations), and data management (in-memory storage).

## Technical Context

**Language/Version**: Python 3.13+ (Phase-1 requirement)
**Primary Dependencies**: Standard library only (no external dependencies except pytest for testing if specified)
**Storage**: In-memory dictionary keyed by task ID - NO persistence permitted in Phase-1
**Testing**: pytest (optional - only if explicitly requested in specification)
**Target Platform**: Console/Terminal (stdin/stdout interaction)
**Project Type**: Single console application (CLI)
**Performance Goals**: Deterministic behavior (same input → same output), instant response times for all operations
**Constraints**: No persistence, no web, no networking, no AI, no authentication, no external dependencies
**Scale/Scope**: Single-user, single-process, runtime-only state, support 100+ tasks in memory

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [x] **Simplicity Over Cleverness**: Design uses minimal, readable Python with functional style - no classes unless clearly beneficial, no manual coding
- [x] **Determinism**: All logic paths predictable and testable (same input → same output) - no randomness, no time-based variation except display timestamps
- [x] **In-Memory State Integrity**: State management in-memory only with dictionary storage - absolutely no file I/O, databases, or external storage
- [x] **Spec-Driven Development**: Follows Constitution → Spec → Plan → Tasks → Implementation sequence - this is the Plan phase
- [x] **Phase-1 Scope**: All features within Phase-1 boundaries - no web, DB, AI, auth, networking, advanced features
- [x] **Standard Library Only**: Zero external dependencies (pytest allowed only for testing if specified)

**Gate Status**: ✅ PASS - All constitutional requirements met, no violations to track

## Project Structure

### Documentation (this feature)

```text
specs/002-console-todo/
├── spec.md              # Feature specification (completed)
├── plan.md              # This file - implementation plan
├── research.md          # Phase 0 research findings (minimal - see below)
├── data-model.md        # Phase 1 data model design
├── quickstart.md        # Phase 1 user guide
├── contracts/           # N/A for Phase-1 (no APIs)
└── checklists/
    └── requirements.md  # Spec quality checklist (completed)
```

### Source Code (repository root)

```text
src/
├── main.py              # Entry point: menu loop, input/output, main() function
├── todo_operations.py   # Business logic: add_task, view_tasks, update_task, delete_task, toggle_complete
└── validation.py        # Input validation: validate_title, validate_description, validate_id

tests/                   # Optional - only if testing explicitly requested
├── test_todo_operations.py
├── test_validation.py
└── test_integration.py
```

**Structure Decision**: Phase-1 uses a simple, flat 3-file structure with clear separation:
- `main.py`: User interface (menu, prompts, output formatting)
- `todo_operations.py`: Core task operations (CRUD + toggle status)
- `validation.py`: Input validation and sanitization

No subdirectories, no classes unless clearly beneficial (simple functions preferred), no over-engineering. This structure allows independent testing of business logic while keeping UI concerns separate.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

No violations. All constitutional requirements met without exceptions.

---

## Phase 0: Research & Analysis

### Research Summary

Phase-1 requirements are straightforward with well-established patterns. No external research needed beyond Python standard library documentation.

**Key Findings**:

1. **Data Structure Choice**:
   - **Decision**: Use dictionary with integer keys for task storage
   - **Rationale**: O(1) lookup by ID, natural fit for auto-incrementing IDs, simple to iterate
   - **Alternatives Considered**:
     - List: Would require linear search for ID lookup, ID management more complex
     - Dataclass/NamedTuple: Adds unnecessary structure for simple dictionary values

2. **ID Management**:
   - **Decision**: Maintain separate `next_id` counter, never reuse IDs after deletion
   - **Rationale**: Meets FR-009 requirement, prevents confusion, simple to implement
   - **Alternatives Considered**:
     - Reuse IDs: Violates spec requirement FR-009
     - UUID: Overkill for in-memory, non-distributed application

3. **Input Validation Strategy**:
   - **Decision**: Validate-then-process with retry loops for invalid input
   - **Rationale**: Meets robustness requirements, prevents crashes, guides users
   - **Alternatives Considered**:
     - Fail-fast: Poor UX, forces restart
     - Silent correction: Violates transparency, confuses users

4. **Menu Navigation**:
   - **Decision**: Numbered menu (1-7) with case-insensitive confirmation prompts (y/n)
   - **Rationale**: Standard CLI pattern, accessible, unambiguous
   - **Alternatives Considered**:
     - Letter-based (A/V/U/D): Less intuitive, harder to remember
     - Command-line args: Not interactive, violates menu requirement

5. **Error Handling**:
   - **Decision**: Try-except blocks for input conversion, explicit validation for business rules
   - **Rationale**: Separates system errors from validation errors, clear messaging
   - **Alternatives Considered**:
     - Single error handler: Loses specificity in error messages

6. **Display Formatting**:
   - **Decision**: Simple formatted strings with fixed-width columns for task listing
   - **Rationale**: Readable, standard library only, no external dependencies
   - **Alternatives Considered**:
     - Rich/Tabulate libraries: Violates standard-library-only constraint
     - ASCII art boxes: Over-engineering, poor accessibility

### Technology Stack Decisions

| Component | Technology | Rationale |
|-----------|-----------|-----------|
| Language | Python 3.13+ | Constitutional requirement |
| Data Storage | dict (in-memory) | O(1) lookup, simple, standard library |
| Input/Output | stdin/stdout (input(), print()) | Standard console I/O, no dependencies |
| String Validation | len(), str.strip() | Standard library, deterministic |
| ID Generation | Integer counter | Simple, deterministic, meets requirements |
| Testing Framework | pytest (optional) | Standard, only if testing requested |

---

## Phase 1: Design & Data Model

### Data Model

See [data-model.md](./data-model.md) for complete entity definitions.

**Core Entities**:

1. **Task** (dictionary structure):
   ```python
   {
       "id": int,           # Unique, auto-incremented, immutable
       "title": str,        # 1-200 chars, required, stripped
       "description": str,  # 0-1000 chars, optional, stripped
       "completed": bool    # Default False
   }
   ```

2. **Application State** (module-level variables):
   ```python
   tasks = {}           # Dict[int, Dict] - main storage
   next_id = 1          # int - ID counter, never decrements
   ```

### Functional Architecture

**Module: main.py**
- Responsibilities: Menu display, user input, output formatting, main loop
- Key Functions:
  - `display_menu()`: Print numbered menu options
  - `get_menu_choice()`: Get and validate menu selection (1-7)
  - `display_tasks(tasks)`: Format and print task list
  - `prompt_for_title()`: Get and validate task title
  - `prompt_for_description()`: Get and validate description
  - `prompt_for_id()`: Get and validate task ID
  - `confirm_exit()`: Handle exit confirmation
  - `main()`: Main application loop

**Module: todo_operations.py**
- Responsibilities: Core task CRUD operations
- Key Functions:
  - `add_task(tasks, next_id, title, description)`: Create task, return new ID
  - `get_task(tasks, task_id)`: Retrieve task by ID or None
  - `update_task(tasks, task_id, title, description)`: Modify existing task
  - `delete_task(tasks, task_id)`: Remove task from storage
  - `toggle_complete(tasks, task_id)`: Toggle completion status
  - `list_tasks(tasks)`: Return sorted list of tasks by ID

**Module: validation.py**
- Responsibilities: Input validation and sanitization
- Key Functions:
  - `validate_title(title)`: Check 1-200 chars after strip, return (valid, error_msg)
  - `validate_description(desc)`: Check 0-1000 chars after strip, return (valid, error_msg)
  - `validate_id(id_str, tasks)`: Parse int, check existence, return (valid, id_int, error_msg)
  - `validate_menu_choice(choice_str)`: Check 1-7 range, return (valid, choice_int, error_msg)

### Control Flow

**Main Application Loop**:
1. Initialize empty tasks dict and next_id counter
2. Loop until exit:
   a. Display menu
   b. Get menu choice (with validation loop)
   c. Execute operation based on choice
   d. Display result/confirmation
   e. Return to step 2

**Operation Patterns**:

*Add Task*:
1. Prompt for title (loop until valid)
2. Prompt for description (loop until valid or empty)
3. Call add_task(), increment next_id
4. Display confirmation with new task ID

*View Tasks*:
1. Call list_tasks()
2. If empty: display "No tasks found" message
3. If not empty: format and display each task

*Update/Delete/Toggle*:
1. Prompt for task ID (loop until valid)
2. Verify task exists
3. For update: prompt for new title/description
4. Call appropriate operation function
5. Display confirmation

*Exit*:
1. Display data loss warning
2. Prompt for confirmation (y/n, case-insensitive)
3. If yes: display goodbye message and exit
4. If no: return to main menu

### Input Validation Rules

| Input Type | Validation Rules | Error Message |
|------------|------------------|---------------|
| Menu Choice | Integer 1-7 | "Invalid choice. Please enter a number from the menu (1-7)" |
| Task Title | 1-200 chars after strip, not empty | "Title is required" or "Title must be 1-200 characters" |
| Description | 0-1000 chars after strip | "Description must be 0-1000 characters" |
| Task ID | Valid integer, exists in tasks dict | "Invalid ID. Please enter a number" or "Task #{id} not found" |
| Exit Confirm | 'y', 'Y', 'n', 'N' | "Please enter 'y' or 'n'" |

### Error Handling Strategy

1. **Input Conversion Errors** (ValueError, etc.):
   - Catch with try-except in validation functions
   - Return validation failure with specific message
   - Prompt user to retry

2. **Validation Failures**:
   - Return (False, error_message) from validation functions
   - Display error message to user
   - Loop back to input prompt

3. **Business Logic Errors** (task not found, etc.):
   - Check preconditions before operations
   - Return None or error indicator
   - Display appropriate error message
   - Return to main menu

4. **No System Crashes**:
   - All user input wrapped in validation
   - No unhandled exceptions in normal flow
   - Exit only through Exit menu option

### User Experience Flow

**Happy Path (Add → View → Complete → View)**:
```
1. App starts, displays menu
2. User enters "1" (Add Task)
3. System prompts: "Enter task title: "
4. User enters: "Buy groceries"
5. System prompts: "Enter description (optional): "
6. User enters: "Milk, bread, eggs"
7. System displays: "Task #1 added successfully"
8. Menu redisplays
9. User enters "2" (View Tasks)
10. System displays:
    ID | Title          | Description       | Status
    1  | Buy groceries  | Milk, bread, eggs | Pending
11. Menu redisplays
12. User enters "5" (Mark Complete)
13. System prompts: "Enter task ID: "
14. User enters: "1"
15. System displays: "Task #1 marked as complete"
16. Menu redisplays
17. User enters "2" (View Tasks)
18. System displays:
    ID | Title          | Description       | Status
    1  | Buy groceries  | Milk, bread, eggs | Completed
```

**Error Handling Example**:
```
1. User enters "5" (Mark Complete)
2. System prompts: "Enter task ID: "
3. User enters: "abc"
4. System displays: "Invalid ID. Please enter a number"
5. System prompts again: "Enter task ID: "
6. User enters: "999"
7. System displays: "Task #999 not found"
8. Returns to main menu
```

---

## Phase 2: Implementation Readiness

### Prerequisites for /sp.tasks

- [x] Specification complete and validated
- [x] Constitution check passed
- [x] Data model defined
- [x] Functional architecture designed
- [x] Project structure determined
- [x] No unresolved NEEDS CLARIFICATION items

**Status**: ✅ Ready for `/sp.tasks`

### Implementation Notes

1. **Start with Core Operations**: Implement todo_operations.py functions first (unit testable)
2. **Then Validation**: Implement validation.py (independently testable)
3. **Finally UI**: Implement main.py (integration testing)
4. **Testing Strategy**: If tests requested, write tests before implementation (TDD)
5. **Acceptance Testing**: Manually verify each user story from spec.md

### Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Input validation edge cases missed | Users encounter crashes | Comprehensive validation.py with explicit tests for edge cases |
| Menu loop logic errors | Infinite loops or unexpected exits | Clear state management, explicit exit flag |
| ID management bugs (reuse after delete) | Violates FR-009, user confusion | Separate next_id counter, never decrement, unit test coverage |
| Output formatting inconsistent | Poor UX | Centralize formatting in display functions, test with various data |
| Empty state handling | Crashes on empty tasks dict | Explicit empty checks before iteration, friendly messages |

### Success Validation

After implementation, validate against Success Criteria from spec.md:

- [ ] SC-001: Task addition completes in <30 seconds
- [ ] SC-002: Task viewing completes in <5 seconds
- [ ] SC-003: Full workflow (add → view → complete → view) in <2 minutes
- [ ] SC-004: 100+ tasks handled without degradation
- [ ] SC-005: 95% valid operations succeed first try
- [ ] SC-006: Invalid inputs show clear, actionable error messages
- [ ] SC-007: No crashes during normal use
- [ ] SC-008: All task IDs remain unique
- [ ] SC-009: Completion status accurately reflects actions
- [ ] SC-010: All features learnable from menu alone

---

## Appendix

### Quickstart Guide

See [quickstart.md](./quickstart.md) for end-user instructions.

### Contracts

N/A - Phase-1 has no APIs or external interfaces. Console I/O only.

### Data Model Details

See [data-model.md](./data-model.md) for complete entity specifications.
