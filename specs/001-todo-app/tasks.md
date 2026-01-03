# Tasks: In-Memory Console Todo App

**Input**: Design documents from `/specs/001-todo-app/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/cli.md

**Tests**: Unit and integration tests are included as requested by the plan's development standards.

**Organization**: Tasks are grouped by setup, foundation, and then by user story priority to enable incremental delivery of the MVP.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure. Must verify AI-Readiness (type hints, docs).

- [x] T001 Create project directories `src/` and `tests/unit/`, `tests/integration/`
- [x] T002 Initialize Python project and configure pytest in `pyproject.toml` or `pytest.ini`

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core data structures and logic that all user stories depend on.

- [x] T003 Implement `Todo` data model with type hints in `src/models.py`
- [x] T004 Implement `TodoManager` class with basic storage dictionary in `src/manager.py`
- [x] T005 [P] Create base view formatting functions in `src/views.py`

## Phase 3: User Story 1 - Add and View Todos (Priority: P1) 🎯 MVP

**Goal**: Allow users to create tasks and view them in a list.

**Independent Test**: Use the CLI to `add "Test Task"` and then `list`. Verify task appears with ID 1.

### Tests for User Story 1
- [x] T006 Create unit tests for `add_todo` and `get_all_todos` in `tests/unit/test_manager.py`
- [x] T007 Create integration test for `add` and `list` commands in `tests/integration/test_cli_flow.py`

### Implementation for User Story 1
- [x] T008 Implement `add_todo` and `get_all_todos` in `src/manager.py`
- [x] T009 Implement `format_todo_list` in `src/views.py`
- [x] T010 Implement command loop and `add`/`list` logic in `src/app.py`

**Checkpoint**: MVP Functional - User can create and view tasks in a session.

## Phase 4: User Story 2 - Complete and Delete Todos (Priority: P2)

**Goal**: Allow users to manage task lifecycle by completing or removing tasks.

**Independent Test**: Add task, run `complete 1`, verify status change in `list`. Then `delete 1`, verify task is gone.

### Tests for User Story 2
- [x] T011 [US2] Add unit tests for `mark_completed` and `delete_todo` in `tests/unit/test_manager.py`
- [x] T012 [US2] Add integration tests for `complete` and `delete` commands in `tests/integration/test_cli_flow.py`

### Implementation for User Story 2
- [x] T013 [US2] Implement `mark_completed` and `delete_todo` logic in `src/manager.py`
- [x] T014 [US2] Add `complete` and `delete` command handlers in `src/app.py`
- [x] T015 [US2] Implement ID validation logic in `src/manager.py` (referenced by FR-006)

## Phase 5: User Story 3 - Update Todo Text (Priority: P3)

**Goal**: Allow users to edit task descriptions.

**Independent Test**: Add task, run `update 1 NEW_TEXT`, verify change in `list`.

### Tests for User Story 3
- [x] T016 [US3] Add unit test for `update_todo` in `tests/unit/test_manager.py`
- [x] T017 [US3] Add integration test for `update` command in `tests/integration/test_cli_flow.py`

### Implementation for User Story 3
- [x] T018 [US3] Implement `update_todo` in `src/manager.py`
- [x] T019 [US3] Add `update` command handler in `src/app.py`

## Phase N: Polish & Cross-Cutting Concerns

- [x] T020 [P] Implement `help` command in `src/views.py` and `src/app.py`
- [x] T021 Implement graceful `exit` handling and final "Goodbye" message in `src/app.py`
- [x] T022 [P] Add final docstrings and ensure 100% type hint coverage across all files
- [x] T023 Run full test suite and verify all user scenarios from `quickstart.md`

## Dependencies & Execution Order

1. **Setup (Phase 1)** -> **Foundational (Phase 2)**
2. **Foundational (Phase 2)** blocks all User Stories.
3. **User Story 1 (P1)** is the MVP and should be completed first.
4. **User Story 2 (P2)** and **User Story 3 (P3)** can proceed in parallel or after P1.

## Parallel Execution Examples

```bash
# Foundational level parallelization
Task T003: models.py
Task T005: views.py
```

## Implementation Strategy
- **MVP First**: Complete through Phase 3 to have a working "Add/List" application.
- **Incremental**: Add lifecycle management (Phase 4) and then editing (Phase 5).
- **Quality**: Write manager unit tests before CLI integration to ensure business logic is deterministic.
