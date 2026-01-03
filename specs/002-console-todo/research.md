# Research: Phase-1 Console Todo App

**Feature**: 002-console-todo
**Date**: 2026-01-04
**Related**: [spec.md](./spec.md) | [plan.md](./plan.md)

## Overview

Research phase for Phase-1 Console Todo App. Requirements are straightforward with well-established CLI patterns. No novel technologies or complex integrations. Research focuses on design decisions and best practices for console applications.

## Research Questions

### 1. Data Structure for Task Storage

**Question**: What Python data structure should store tasks in memory?

**Options Evaluated**:

| Option | Pros | Cons | Decision |
|--------|------|------|----------|
| List of dicts | Simple, ordered | O(n) lookup by ID, complex ID management | ❌ Rejected |
| Dict with int keys | O(1) lookup, natural ID mapping | Unordered in Python <3.7 | ✅ **Selected** |
| Dataclass/NamedTuple | Type safety, structured | Overkill for simple app, needs external storage | ❌ Rejected |
| Custom class | Object-oriented, encapsulation | Over-engineering for Phase-1 | ❌ Rejected |

**Decision**: Use `dict[int, dict]` with integer keys as task IDs.

**Rationale**:
- O(1) lookup by ID (optimal performance)
- Natural mapping: ID → task data
- Simple to implement and maintain
- Ordered by insertion in Python 3.7+ (bonus, though not required)
- Standard library, no dependencies
- Easy to iterate for display (dict.values())

**Implementation**:
```python
tasks = {
    1: {"id": 1, "title": "...", "description": "...", "completed": False},
    2: {"id": 2, "title": "...", "description": "...", "completed": False}
}
```

---

### 2. ID Generation Strategy

**Question**: How to generate and manage unique task IDs?

**Options Evaluated**:

| Option | Pros | Cons | Decision |
|--------|------|------|----------|
| Reuse deleted IDs | Compact ID space | Violates FR-009, confusing | ❌ Rejected |
| Auto-increment counter | Simple, unique, predictable | IDs have gaps after deletion | ✅ **Selected** |
| UUID | Globally unique, no collisions | Overkill, not user-friendly | ❌ Rejected |
| Timestamp-based | Chronological | Not sequential, collisions possible | ❌ Rejected |

**Decision**: Auto-incrementing integer counter (`next_id`), never reuse IDs.

**Rationale**:
- Meets FR-009: "MUST preserve task IDs when tasks are deleted (no ID reuse)"
- Simple to implement: `next_id += 1` after each add
- User-friendly: Sequential numbers (1, 2, 3...)
- Deterministic: Same operations produce same IDs
- Never decrements, even after all tasks deleted

**Implementation**:
```python
next_id = 1  # Module-level global

def add_task(tasks, next_id, title, description):
    task_id = next_id
    tasks[task_id] = {
        "id": task_id,
        "title": title,
        "description": description,
        "completed": False
    }
    return task_id  # Caller increments next_id
```

---

### 3. Input Validation Approach

**Question**: How to validate user input robustly without crashing?

**Options Evaluated**:

| Option | Pros | Cons | Decision |
|--------|------|------|----------|
| Fail-fast (raise exceptions) | Simple code | Poor UX, forces restart | ❌ Rejected |
| Silent correction | Seamless UX | Confusing, violates transparency | ❌ Rejected |
| Validate-retry loops | Clear feedback, guides user | More code, complex loops | ✅ **Selected** |
| Regex patterns | Precise validation | Overkill for simple constraints | ❌ Rejected |

**Decision**: Validate-then-process with retry loops for invalid input.

**Rationale**:
- Meets FR-003: "MUST validate all user inputs and display helpful error messages"
- Provides clear, actionable error messages
- Allows users to correct mistakes without restarting
- Deterministic: Same invalid input produces same error
- Separation of concerns: Validation logic in separate module

**Implementation Pattern**:
```python
def validate_title(title: str) -> tuple[bool, str | None]:
    """Validate title. Returns (is_valid, error_message)."""
    stripped = title.strip()
    if not stripped:
        return (False, "Title is required")
    if len(stripped) > 200:
        return (False, "Title must be 1-200 characters")
    return (True, None)

# Usage in main.py
while True:
    title = input("Enter task title: ")
    valid, error = validate_title(title)
    if valid:
        break
    print(f"Error: {error}")
```

---

### 4. Menu Interface Design

**Question**: What menu style is most usable and standard for CLI?

**Options Evaluated**:

| Option | Pros | Cons | Decision |
|--------|------|------|----------|
| Numbered menu (1-7) | Standard, unambiguous | Requires numeric input | ✅ **Selected** |
| Letter menu (A/V/U/D) | Mnemonic, fast | Harder to remember, conflicts | ❌ Rejected |
| Command-line args | Scriptable | Not interactive, poor UX | ❌ Rejected |
| Natural language | User-friendly | Complex parsing, out of scope | ❌ Rejected |

**Decision**: Numbered menu with options 1-7.

**Rationale**:
- Industry standard for CLI applications
- Unambiguous: Numbers map clearly to actions
- Accessible: Works on all terminals
- Simple input validation: Check range 1-7
- Easy to document: "Enter 1 for Add Task"

**Implementation**:
```
=== Todo App Menu ===
1. Add Task
2. View All Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete
6. Mark Task Incomplete
7. Exit

Enter your choice (1-7):
```

---

### 5. Error Handling Strategy

**Question**: How to handle errors without crashing?

**Approach**: Three-tier error handling:

1. **Input Conversion Errors** (ValueError, etc.):
   ```python
   try:
       choice = int(input("Enter choice: "))
   except ValueError:
       print("Error: Please enter a number")
       continue
   ```

2. **Validation Failures**:
   ```python
   valid, error = validate_title(title)
   if not valid:
       print(f"Error: {error}")
       continue  # Retry loop
   ```

3. **Business Logic Errors**:
   ```python
   task = get_task(tasks, task_id)
   if task is None:
       print(f"Error: Task #{task_id} not found")
       return  # Back to main menu
   ```

**Rationale**:
- Separates system errors from validation errors
- Provides specific, actionable messages
- Never exposes stack traces to users
- Meets FR-003 and SC-007 (no crashes)

---

### 6. Display Formatting

**Question**: How to format task list for readability without external libraries?

**Options Evaluated**:

| Option | Pros | Cons | Decision |
|--------|------|------|----------|
| Simple formatted strings | No dependencies, flexible | Manual alignment | ✅ **Selected** |
| Rich/Tabulate library | Beautiful output | Violates standard-library-only | ❌ Rejected |
| ASCII art boxes | Visually appealing | Over-engineering, poor accessibility | ❌ Rejected |
| CSV format | Machine-readable | Poor human UX | ❌ Rejected |

**Decision**: Formatted strings with fixed-width columns.

**Rationale**:
- Standard library only (constitutional requirement)
- Readable and professional
- Accessible (screen readers compatible)
- Flexible for long titles/descriptions

**Implementation**:
```python
print(f"{'ID':<5} | {'Title':<30} | {'Description':<40} | {'Status':<10}")
print("-" * 90)
for task in sorted(tasks.values(), key=lambda t: t['id']):
    status = "Completed" if task['completed'] else "Pending"
    print(f"{task['id']:<5} | {task['title']:<30} | {task['description']:<40} | {status:<10}")
```

---

### 7. Exit Confirmation

**Question**: Should exit require confirmation?

**Decision**: Yes, with data loss warning.

**Rationale**:
- Meets FR-013: "MUST display exit confirmation warning users that all data will be lost"
- Prevents accidental data loss
- Standard pattern for destructive actions
- Simple y/n prompt, case-insensitive

**Implementation**:
```python
def confirm_exit() -> bool:
    """Prompt for exit confirmation. Returns True if user confirms."""
    while True:
        response = input("All data will be lost. Are you sure? (y/n): ").strip().lower()
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' or 'n'")
```

---

## Best Practices Applied

### Python CLI Best Practices

1. **Clear prompts**: Every input() has descriptive prompt
2. **Explicit feedback**: Every action confirmed or error reported
3. **Graceful degradation**: Invalid input never crashes app
4. **Separation of concerns**: UI, logic, validation in separate modules
5. **Type hints**: All functions annotated for clarity
6. **Docstrings**: Public functions documented
7. **Standard library only**: No external dependencies (constitutional)

### Console Application Patterns

1. **Menu-driven**: Standard numbered menu
2. **Input validation loops**: Retry until valid
3. **Empty state handling**: Friendly messages for empty lists
4. **Exit strategy**: Explicit exit command with confirmation
5. **Status feedback**: Clear success/error messages
6. **ID-based operations**: Simple integer IDs for user convenience

---

## Technology Stack (Final)

| Component | Technology | Version | Rationale |
|-----------|-----------|---------|-----------|
| Language | Python | 3.13+ | Constitutional requirement |
| Data Storage | dict | Built-in | O(1) lookup, simple, standard library |
| I/O | stdin/stdout | Built-in | Console app, no dependencies |
| Validation | len(), strip() | Built-in | Deterministic, standard library |
| ID Generation | int counter | Built-in | Simple, meets FR-009 |
| Testing | pytest | Latest | Standard, only if testing specified |

**External Dependencies**: ZERO (except pytest if testing requested)

---

## Architectural Decisions

### AD-1: Functional Programming Over OOP

**Decision**: Use simple functions instead of classes.

**Rationale**:
- Phase-1 scope is simple (CRUD operations)
- No complex state management or polymorphism needed
- Functions are testable, composable, and beginner-friendly
- Meets constitutional requirement: "Simplicity Over Cleverness"
- Can refactor to classes in Phase-2 if needed

**Impact**: Three modules with pure functions, pass state explicitly.

---

### AD-2: Module-Level State

**Decision**: Store `tasks` and `next_id` as module-level globals in `main.py`.

**Rationale**:
- Phase-1 is single-user, single-process (no concurrency)
- Simplifies function signatures (don't pass state everywhere)
- Easy to initialize and reset
- Acceptable for Phase-1 scope
- Phase-2 can refactor to class-based state or database

**Impact**: All functions access shared global state.

---

### AD-3: No Persistence Layer

**Decision**: Absolutely no file I/O, database, or serialization in Phase-1.

**Rationale**:
- Constitutional prohibition: "No persistence to files, databases, or external storage is permitted in Phase-1"
- Forces focus on core logic and UX
- Simplifies implementation and testing
- Data loss on exit is by design (user warned)

**Impact**: Phase-2 will add persistence as separate layer.

---

## Research Conclusions

**Summary**: Phase-1 requirements are well-served by standard Python CLI patterns. No novel research or complex technologies needed. Implementation focuses on simplicity, robustness, and user experience.

**Key Takeaways**:
1. Dictionary with integer keys optimal for task storage
2. Auto-incrementing ID counter meets requirements simply
3. Validate-retry loops provide best UX for invalid input
4. Numbered menu is industry standard and accessible
5. Three-tier error handling prevents crashes
6. Simple formatted strings sufficient for display
7. Exit confirmation prevents accidental data loss

**Risks Addressed**:
- Input validation: Comprehensive validation module
- ID management: Never reuse, separate counter
- Error handling: No unhandled exceptions
- Empty state: Explicit checks and friendly messages
- Unicode support: UTF-8 by default in Python 3

**Ready for Implementation**: All design questions resolved, no blockers.
