# Feature Specification: Phase-1 Console Todo App

**Feature Branch**: `002-console-todo`
**Created**: 2026-01-04
**Status**: Draft
**Input**: User description: "Phase-1 In-Memory Python Console Todo App"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Add Task (Priority: P1)

User can add a new todo task with title and optional description via console prompts.

**Why this priority**: Core functionality - without the ability to add tasks, no other operations are possible. This is the foundational operation that enables all other user stories.

**Independent Test**: Can be fully tested by launching the app, selecting "Add Task", entering a title and description, and verifying the task is added to the list. Delivers immediate value as users can start capturing todos.

**Acceptance Scenarios**:

1. **Given** the app is running and showing the main menu, **When** user selects "Add Task" and enters title "Buy groceries" and description "Milk, bread, eggs", **Then** system assigns unique ID, stores task in memory with completed=false, and displays confirmation "Task #1 added successfully"

2. **Given** user is adding a task, **When** user enters title "Call dentist" and leaves description empty, **Then** system stores task with empty description and displays confirmation

3. **Given** user is adding a task, **When** user enters title with 200 characters (max length), **Then** system accepts and stores the task

4. **Given** user is adding a task, **When** user enters title exceeding 200 characters, **Then** system displays error "Title must be 1-200 characters" and prompts again

5. **Given** user is adding a task, **When** user enters empty title or whitespace-only title, **Then** system displays error "Title is required" and prompts again

---

### User Story 2 - View All Tasks (Priority: P1)

User can view a list of all tasks with their ID, title, description, and completion status.

**Why this priority**: Essential for users to see what tasks exist. Without viewing capability, users can't verify additions or identify which tasks to update/delete/complete. Equally critical as adding tasks for a viable MVP.

**Independent Test**: Can be fully tested by adding several tasks, selecting "View Tasks", and verifying all tasks are displayed with correct details and formatting. Delivers value by providing visibility into stored todos.

**Acceptance Scenarios**:

1. **Given** 3 tasks exist in memory, **When** user selects "View Tasks", **Then** system displays all 3 tasks with format: "ID | Title | Description | Status" where Status is "Completed" or "Pending"

2. **Given** no tasks exist, **When** user selects "View Tasks", **Then** system displays "No tasks found. Add a task to get started."

3. **Given** tasks with varying title lengths and completion states exist, **When** user views tasks, **Then** system displays them in a readable format with proper alignment and clear status indicators

4. **Given** multiple tasks exist, **When** user views tasks, **Then** tasks are displayed in order of ID (oldest first)

---

### User Story 3 - Mark Task Complete/Incomplete (Priority: P2)

User can toggle a task's completion status by entering its ID.

**Why this priority**: Completing tasks is core to todo functionality, but users can still derive value from adding and viewing tasks without this feature. Priority 2 makes this app truly functional as a todo manager.

**Independent Test**: Can be fully tested by adding tasks, selecting "Mark Complete", entering a task ID, and verifying status changes. Delivers value by allowing users to track progress.

**Acceptance Scenarios**:

1. **Given** task #1 exists with completed=false, **When** user selects "Mark Complete" and enters ID "1", **Then** system sets task #1 completed=true and displays "Task #1 marked as complete"

2. **Given** task #2 exists with completed=true, **When** user selects "Mark Incomplete" and enters ID "2", **Then** system sets task #2 completed=false and displays "Task #2 marked as incomplete"

3. **Given** user selects "Mark Complete", **When** user enters non-existent ID "999", **Then** system displays error "Task #999 not found" and returns to main menu

4. **Given** user selects "Mark Complete", **When** user enters invalid input "abc", **Then** system displays error "Invalid ID. Please enter a number" and prompts again

---

### User Story 4 - Update Task (Priority: P3)

User can update a task's title and/or description by entering its ID.

**Why this priority**: Nice-to-have enhancement. Users can work around this by deleting and re-adding tasks. Less critical than core CRUD operations.

**Independent Test**: Can be fully tested by adding a task, selecting "Update Task", entering task ID, and modifying title/description. Delivers value by allowing users to correct mistakes or refine details.

**Acceptance Scenarios**:

1. **Given** task #1 exists with title "Buy milk", **When** user selects "Update Task", enters ID "1", and updates title to "Buy groceries", **Then** system updates task #1 title and displays "Task #1 updated successfully"

2. **Given** task #2 exists with description "Old description", **When** user updates only the description to "New description", **Then** system updates only description and keeps title unchanged

3. **Given** user is updating task #3, **When** user provides new title exceeding 200 characters, **Then** system displays error "Title must be 1-200 characters" and prompts again

4. **Given** user selects "Update Task", **When** user enters non-existent ID "999", **Then** system displays error "Task #999 not found" and returns to main menu

---

### User Story 5 - Delete Task (Priority: P3)

User can permanently delete a task from memory by entering its ID.

**Why this priority**: Useful for removing unwanted tasks, but not critical for MVP. Users can work around by ignoring completed tasks. Same priority as Update.

**Independent Test**: Can be fully tested by adding tasks, selecting "Delete Task", entering task ID, and verifying task is removed from list. Delivers value by allowing users to clean up their task list.

**Acceptance Scenarios**:

1. **Given** task #1 exists, **When** user selects "Delete Task" and enters ID "1", **Then** system removes task #1 from memory and displays "Task #1 deleted successfully"

2. **Given** 3 tasks exist, **When** user deletes task #2, **Then** system removes only task #2, and tasks #1 and #3 remain with their original IDs unchanged

3. **Given** user selects "Delete Task", **When** user enters non-existent ID "999", **Then** system displays error "Task #999 not found" and returns to main menu

4. **Given** user selects "Delete Task", **When** user enters invalid input "xyz", **Then** system displays error "Invalid ID. Please enter a number" and prompts again

---

### User Story 6 - Exit Application (Priority: P1)

User can cleanly exit the application, with clear indication that data will be lost.

**Why this priority**: Essential for good UX. Users need a clean way to terminate the program. Critical for MVP completeness.

**Independent Test**: Can be fully tested by selecting "Exit" and verifying program terminates gracefully with appropriate message. Delivers value through proper application lifecycle management.

**Acceptance Scenarios**:

1. **Given** the app is running at main menu, **When** user selects "Exit", **Then** system displays "All data will be lost. Are you sure? (y/n)" and waits for confirmation

2. **Given** exit confirmation prompt is shown, **When** user enters "y", **Then** system displays "Goodbye!" and terminates cleanly

3. **Given** exit confirmation prompt is shown, **When** user enters "n", **Then** system returns to main menu without exiting

---

### Edge Cases

- What happens when user enters invalid menu choices (letters when numbers expected)?
  - System displays "Invalid choice. Please enter a number from the menu" and re-displays menu

- What happens when description exceeds 1000 characters?
  - System displays error "Description must be 0-1000 characters" and prompts again

- What happens when user tries to mark the same task complete multiple times?
  - System updates status even if already complete and displays confirmation message (idempotent operation)

- What happens when all tasks are deleted and user tries to view tasks?
  - System displays "No tasks found. Add a task to get started."

- What happens if user rapidly adds many tasks (e.g., 1000+)?
  - System continues to function normally as long as memory permits (Python list/dict handles this)

- What happens when user enters title/description with special characters or emojis?
  - System accepts and stores any valid Unicode characters

## Requirements *(mandatory)*

- **Simplicity Check**: Requirement adds minimum necessary complexity (Phase-1: no manual coding, standard library only) ✅
- **Deterministic Check**: Outcome is strictly defined for given inputs (same input → same output) ✅
- **Phase-1 Scope Check**: Requirement must NOT involve persistence, web, networking, AI, or authentication ✅
- **In-Memory Check**: All data must be stored in-memory only (no files, databases, cloud storage) ✅

### Functional Requirements

- **FR-001**: System MUST provide a numbered menu interface listing all available operations (Add, View, Update, Delete, Mark Complete, Mark Incomplete, Exit)

- **FR-002**: System MUST display the main menu after every operation completes (except Exit)

- **FR-003**: System MUST validate all user inputs and display helpful error messages for invalid inputs without crashing

- **FR-004**: System MUST assign unique, auto-incrementing integer IDs to tasks starting from 1

- **FR-005**: System MUST store tasks in memory only using Python standard data structures (list/dict)

- **FR-006**: System MUST enforce title length constraint (1-200 characters, required)

- **FR-007**: System MUST enforce description length constraint (0-1000 characters, optional)

- **FR-008**: System MUST initialize all new tasks with completed=false

- **FR-009**: System MUST preserve task IDs when tasks are deleted (no ID reuse)

- **FR-010**: System MUST display clear confirmation messages after successful operations

- **FR-011**: System MUST display clear error messages when operations fail (non-existent ID, invalid input)

- **FR-012**: System MUST handle non-numeric input gracefully when numeric input is expected (menu choice, task ID)

- **FR-013**: System MUST display exit confirmation warning users that all data will be lost

- **FR-014**: System MUST support toggling task completion status (incomplete → complete, complete → incomplete)

- **FR-015**: System MUST display task status clearly in view operations ("Completed" or "Pending")

### Key Entities

- **Task**: Represents a single todo item with the following attributes:
  - `id`: Unique integer identifier, auto-assigned, immutable, starts from 1
  - `title`: String, 1-200 characters, required, describes the task
  - `description`: String, 0-1000 characters, optional, provides additional details
  - `completed`: Boolean, default false, indicates completion status

### Assumptions

- **Input Method**: User interacts via keyboard input (stdin) and sees output on terminal (stdout)
- **Character Encoding**: UTF-8 encoding for all text inputs (supports international characters and emojis)
- **Menu Navigation**: Numeric menu choices (1-7) for operations
- **ID Format**: Task IDs displayed as integers without leading zeros (e.g., "1", "12", "123")
- **Empty List Handling**: Displaying empty task list shows friendly message rather than error
- **Case Sensitivity**: Menu choices and confirmation inputs (y/n) are case-insensitive
- **Whitespace Handling**: Leading/trailing whitespace in title/description is trimmed before validation
- **Task Ordering**: Tasks displayed in ID order (ascending) by default

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can add a task in under 30 seconds (title + optional description)

- **SC-002**: Users can view all tasks and identify task details (ID, title, status) within 5 seconds

- **SC-003**: Users can complete core workflow (add → view → mark complete → view) in under 2 minutes

- **SC-004**: System handles 100+ tasks without noticeable performance degradation

- **SC-005**: 95% of valid operations (correct input format) succeed on first attempt

- **SC-006**: Invalid input operations provide clear error messages that allow users to correct their mistake without restarting the application

- **SC-007**: Application never crashes during normal use (only terminates via Exit command)

- **SC-008**: All task IDs remain unique throughout application session

- **SC-009**: Task completion status accurately reflects user actions (no false positives/negatives)

- **SC-010**: Users can independently learn all features from menu options without external documentation
