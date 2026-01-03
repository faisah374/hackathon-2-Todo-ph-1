---

description: "Task list for Phase-1 Console Todo App implementation"
---

# Tasks: Phase-1 Console Todo App

**Input**: Design documents from `/specs/002-console-todo/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), data-model.md, research.md

**Tests**: Tests are NOT requested in the specification - this implementation will focus on functional code only. Testing can be added in a future iteration if needed.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, at repository root (Phase-1 structure)
- Paths shown below use `src/` at repository root

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure. Must verify Phase-1 compliance (Python 3.13+, standard library only, type hints, in-memory only).

- [ ] T001 Create project directory structure (src/ at repository root)
- [ ] T002 [P] Create empty Python files: src/main.py, src/todo_operations.py, src/validation.py
- [ ] T003 [P] Add module docstrings to all three Python files explaining their purpose
- [ ] T004 [P] Add type hints import statements to all three files (from typing import Dict, Tuple, Optional)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T005 Initialize global state variables in src/main.py (tasks: Dict[int, Dict] = {}, next_id: int = 1)
- [ ] T006 [P] Implement validate_title function in src/validation.py (checks 1-200 chars after strip, returns tuple[bool, Optional[str]])
- [ ] T007 [P] Implement validate_description function in src/validation.py (checks 0-1000 chars after strip, returns tuple[bool, Optional[str]])
- [ ] T008 [P] Implement validate_id function in src/validation.py (parses int, checks existence in tasks dict, returns tuple[bool, Optional[int], Optional[str]])
- [ ] T009 [P] Implement validate_menu_choice function in src/validation.py (checks 1-7 range, returns tuple[bool, Optional[int], Optional[str]])
- [ ] T010 [P] Implement display_menu function in src/main.py (prints numbered menu with 7 options)
- [ ] T011 [P] Implement get_menu_choice function in src/main.py (gets and validates menu selection using validate_menu_choice, loops until valid)

**Phase-1 Constraints**: NO database, NO files, NO API routing, NO authentication. All state in-memory only.

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add Task (Priority: P1) 🎯 MVP

**Goal**: User can add a new todo task with title and optional description via console prompts

**Independent Test**: Launch app, select "Add Task", enter title and description, verify task is added to list with confirmation message

- [ ] T012 [US1] Implement add_task function in src/todo_operations.py (takes tasks, next_id, title, description; creates task dict with id, title, description, completed=False; adds to tasks dict; returns new task_id)
- [ ] T013 [US1] Implement prompt_for_title function in src/main.py (prompts for title, validates with validate_title, loops until valid, returns stripped title)
- [ ] T014 [US1] Implement prompt_for_description function in src/main.py (prompts for description with "(optional)" hint, validates with validate_description, loops until valid or empty, returns stripped description)
- [ ] T015 [US1] Implement handle_add_task function in src/main.py (calls prompt_for_title and prompt_for_description, calls add_task, increments next_id, displays "Task #{id} added successfully")

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View All Tasks (Priority: P1) 🎯 MVP

**Goal**: User can view a list of all tasks with their ID, title, description, and completion status

**Independent Test**: Add several tasks, select "View Tasks", verify all tasks are displayed with correct format and details

- [ ] T016 [US2] Implement list_tasks function in src/todo_operations.py (returns list of task dicts sorted by id)
- [ ] T017 [US2] Implement display_tasks function in src/main.py (takes tasks dict; if empty displays "No tasks found. Add a task to get started."; otherwise formats and prints table with columns: ID, Title, Description, Status where Status is "Completed" or "Pending")
- [ ] T018 [US2] Implement handle_view_tasks function in src/main.py (calls list_tasks, calls display_tasks with formatted output)

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 6 - Exit Application (Priority: P1) 🎯 MVP

**Goal**: User can cleanly exit the application with clear indication that data will be lost

**Independent Test**: Select "Exit", verify data loss warning appears, confirm exit, verify "Goodbye!" message and clean termination

- [ ] T019 [US6] Implement confirm_exit function in src/main.py (prompts "All data will be lost. Are you sure? (y/n)", validates y/Y/n/N case-insensitive, loops until valid, returns True for yes, False for no)
- [ ] T020 [US6] Implement handle_exit function in src/main.py (calls confirm_exit; if True displays "Goodbye!" and returns exit signal; if False returns to menu)

**Checkpoint**: At this point, MVP (User Stories 1, 2, 6) should be complete and fully functional

---

## Phase 6: Main Application Loop (Integrates MVP)

**Goal**: Tie together Add Task, View Tasks, and Exit into a working menu-driven application

**Independent Test**: Run app, verify menu displays, test all three operations (add, view, exit) work correctly together

- [ ] T021 Implement main function in src/main.py (initialize tasks and next_id; loop: display_menu, get_menu_choice, handle choice 1=add_task, 2=view_tasks, 7=exit; display "Invalid choice" for unimplemented options 3-6; continue until exit)
- [ ] T022 Add if __name__ == "__main__": main() block in src/main.py
- [ ] T023 Test MVP manually: Run python src/main.py, add task, view tasks, exit - verify all work correctly

**Checkpoint**: MVP is now runnable and deliverable. Remaining user stories add optional features.

---

## Phase 7: User Story 3 - Mark Task Complete/Incomplete (Priority: P2)

**Goal**: User can toggle a task's completion status by entering its ID

**Independent Test**: Add tasks, select "Mark Complete", enter task ID, verify status changes to Completed; select "Mark Incomplete", verify status changes back to Pending

- [ ] T024 [US3] Implement toggle_complete function in src/todo_operations.py (takes tasks dict and task_id, toggles completed boolean, returns True if successful, False if task not found)
- [ ] T025 [US3] Implement prompt_for_id function in src/main.py (prompts "Enter task ID:", validates with validate_id, loops until valid, returns validated task_id)
- [ ] T026 [US3] Implement handle_mark_complete function in src/main.py (calls prompt_for_id, calls get_task to verify existence, calls toggle_complete to set completed=True, displays "Task #{id} marked as complete" or error if not found)
- [ ] T027 [US3] Implement handle_mark_incomplete function in src/main.py (calls prompt_for_id, calls get_task to verify existence, calls toggle_complete to set completed=False, displays "Task #{id} marked as incomplete" or error if not found)
- [ ] T028 [US3] Add menu options 5 and 6 to main function switch/if-elif (5=handle_mark_complete, 6=handle_mark_incomplete)

**Checkpoint**: All user stories should now be independently functional (US1, US2, US3, US6)

---

## Phase 8: User Story 4 - Update Task (Priority: P3)

**Goal**: User can update a task's title and/or description by entering its ID

**Independent Test**: Add task, select "Update Task", enter task ID, modify title/description, verify task updates successfully

- [ ] T029 [US4] Implement get_task function in src/todo_operations.py (takes tasks dict and task_id, returns task dict if found, None if not found)
- [ ] T030 [US4] Implement update_task function in src/todo_operations.py (takes tasks dict, task_id, new_title, new_description; updates task if exists; returns True if successful, False if not found)
- [ ] T031 [US4] Implement prompt_for_update_title function in src/main.py (prompts "Enter new title (or press Enter to keep current): "; if empty returns None; otherwise validates and returns new title)
- [ ] T032 [US4] Implement prompt_for_update_description function in src/main.py (prompts "Enter new description (or press Enter to keep current): "; if empty returns None; otherwise validates and returns new description)
- [ ] T033 [US4] Implement handle_update_task function in src/main.py (calls prompt_for_id, calls get_task to verify existence and get current values, prompts for new title/description with current values as hints, calls update_task with new or current values, displays "Task #{id} updated successfully" or error)
- [ ] T034 [US4] Add menu option 3 to main function switch/if-elif (3=handle_update_task)

**Checkpoint**: All user stories functional except Delete (US1, US2, US3, US4, US6)

---

## Phase 9: User Story 5 - Delete Task (Priority: P3)

**Goal**: User can permanently delete a task from memory by entering its ID

**Independent Test**: Add tasks, select "Delete Task", enter task ID, verify task is removed from list

- [ ] T035 [US5] Implement delete_task function in src/todo_operations.py (takes tasks dict and task_id, removes task from dict if exists, returns True if successful, False if not found)
- [ ] T036 [US5] Implement handle_delete_task function in src/main.py (calls prompt_for_id, calls get_task to verify existence, calls delete_task, displays "Task #{id} deleted successfully" or error if not found)
- [ ] T037 [US5] Add menu option 4 to main function switch/if-elif (4=handle_delete_task)

**Checkpoint**: All user stories should now be fully implemented and independently functional

---

## Phase 10: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T038 [P] Add comprehensive docstrings to all functions in src/validation.py (include parameter types, return types, examples)
- [ ] T039 [P] Add comprehensive docstrings to all functions in src/todo_operations.py (include parameter types, return types, examples)
- [ ] T040 [P] Add comprehensive docstrings to all functions in src/main.py (include parameter types, return types, examples)
- [ ] T041 Verify all error messages match spec requirements (check FR-011 error formats)
- [ ] T042 Verify all confirmation messages match spec requirements (check FR-010 confirmation formats)
- [ ] T043 [P] Test edge case: Add task with 200-character title (should succeed)
- [ ] T044 [P] Test edge case: Add task with 201-character title (should show error and retry)
- [ ] T045 [P] Test edge case: Add task with empty/whitespace-only title (should show error and retry)
- [ ] T046 [P] Test edge case: View tasks when list is empty (should show friendly message)
- [ ] T047 [P] Test edge case: Delete task then verify ID not reused for next add (FR-009)
- [ ] T048 [P] Test edge case: Mark non-existent task complete (should show error)
- [ ] T049 [P] Test edge case: Enter invalid menu choice (letter instead of number)
- [ ] T050 [P] Test edge case: Enter out-of-range menu choice (0 or 8)
- [ ] T051 [P] Test edge case: Unicode characters (emojis) in title and description
- [ ] T052 Run complete workflow test: add → view → mark complete → view → update → view → delete → view → exit

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-9)**: All depend on Foundational phase completion
  - MVP Stories (US1, US2, US6): Can proceed in parallel after Foundational (Priority P1)
  - US3 (Priority P2): Can start after Foundational, independent of MVP
  - US4 and US5 (Priority P3): Can start after Foundational, independent of each other
- **Main Loop (Phase 6)**: Depends on US1, US2, US6 completion (MVP integration)
- **Polish (Phase 10)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1) - Add Task**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1) - View Tasks**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 6 (P1) - Exit**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 3 (P2) - Mark Complete/Incomplete**: Can start after Foundational (Phase 2) - Independent (though benefits from US1 for testing)
- **User Story 4 (P3) - Update Task**: Can start after Foundational (Phase 2) - Independent (though benefits from US1 for testing)
- **User Story 5 (P3) - Delete Task**: Can start after Foundational (Phase 2) - Independent (though benefits from US1 for testing)

### Within Each User Story

- US1: prompt_for_title and prompt_for_description can be parallel → then add_task → then handle_add_task
- US2: list_tasks and display_tasks can be sequential → then handle_view_tasks
- US3: toggle_complete, prompt_for_id can be parallel → then handle functions use both
- US4: get_task, update_task, prompt functions can be parallel → then handle_update_task uses all
- US5: delete_task, (reuses prompt_for_id from US3) → then handle_delete_task
- US6: confirm_exit → handle_exit

### Parallel Opportunities

- All Setup tasks (T001-T004) can run in parallel except T001 must complete first
- All Foundational tasks marked [P] (T006-T011) can run in parallel after T005
- Once Foundational phase completes:
  - US1 (T012-T015) can run in parallel
  - US2 (T016-T018) can run in parallel
  - US6 (T019-T020) can run in parallel
  - US3, US4, US5 can each proceed independently
- All polish tasks marked [P] (T038-T051) can run in parallel

---

## Parallel Example: MVP (User Stories 1, 2, 6)

```bash
# After Foundational phase completes, launch all MVP stories together:
# User Story 1 tasks (T012-T015)
# User Story 2 tasks (T016-T018)
# User Story 6 tasks (T019-T020)

# These can be developed in parallel by different developers or sequentially in any order
```

---

## Implementation Strategy

### MVP First (User Stories 1, 2, 6 Only)

1. Complete Phase 1: Setup (T001-T004)
2. Complete Phase 2: Foundational (T005-T011) - CRITICAL, blocks all stories
3. Complete Phase 3: User Story 1 - Add Task (T012-T015)
4. Complete Phase 4: User Story 2 - View Tasks (T016-T018)
5. Complete Phase 5: User Story 6 - Exit (T019-T020)
6. Complete Phase 6: Main Loop Integration (T021-T023)
7. **STOP and VALIDATE**: Test MVP independently - add, view, exit
8. Deploy/demo if ready

**MVP Delivers**: Core value - users can add tasks, see their task list, and exit cleanly. Fully functional todo app.

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add US1, US2, US6 + Main Loop (T021-T023) → Test independently → Deploy/Demo (MVP!)
3. Add US3 (T024-T028) → Test independently → Deploy/Demo (now users can track completion)
4. Add US4 (T029-T034) → Test independently → Deploy/Demo (now users can edit tasks)
5. Add US5 (T035-T037) → Test independently → Deploy/Demo (now users can delete tasks)
6. Add Polish (T038-T052) → Final validation → Deploy/Demo (production-ready)
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together (T001-T011)
2. Once Foundational is done:
   - Developer A: User Story 1 (T012-T015)
   - Developer B: User Story 2 (T016-T018)
   - Developer C: User Story 6 (T019-T020)
3. Integrate MVP (T021-T023)
4. Then proceed with remaining stories in parallel:
   - Developer A: User Story 3 (T024-T028)
   - Developer B: User Story 4 (T029-T034)
   - Developer C: User Story 5 (T035-T037)
5. Complete Polish tasks in parallel (T038-T052)

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- No tests included (not requested in specification)
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
- All tasks include specific file paths for clarity
- Type hints and docstrings required (constitutional requirement: beginner-friendly)
- Zero external dependencies except Python 3.13+ standard library

---

## Task Count Summary

- **Total Tasks**: 52 tasks
- **Setup**: 4 tasks
- **Foundational**: 7 tasks
- **User Story 1 (Add Task)**: 4 tasks
- **User Story 2 (View Tasks)**: 3 tasks
- **User Story 6 (Exit)**: 2 tasks
- **Main Loop Integration**: 3 tasks (creates runnable MVP)
- **User Story 3 (Mark Complete/Incomplete)**: 5 tasks
- **User Story 4 (Update Task)**: 6 tasks
- **User Story 5 (Delete Task)**: 3 tasks
- **Polish**: 15 tasks

**MVP Scope** (T001-T023): 23 tasks for a fully functional console todo app (add, view, exit)

**Full Feature Set** (T001-T052): 52 tasks for complete Phase-1 implementation
