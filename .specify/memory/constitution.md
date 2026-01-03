<!--
Sync Impact Report:
- Version change: 1.0.0 -> 2.0.0
- Rationale: MAJOR version bump due to backward-incompatible changes - stricter Phase-1 constraints, Python version requirement updated to 3.13+, added mandatory Spec-Driven Development sequencing, removed AI-Assist Readiness principle (out of scope for Phase-1), restructured principles to align with Phase-1 scope
- List of modified principles:
  - Simplicity First -> Simplicity Over Cleverness (strengthened with explicit no-manual-coding rule)
  - Deterministic Behavior -> Deterministic Behavior (unchanged principle, updated description)
  - In-Memory State Integrity -> In-Memory State Integrity (strengthened with explicit no-persistence constraints)
  - Spec-Driven Development -> Spec-Driven Development Mandate (elevated to mandatory with strict sequencing)
  - Forward Compatibility -> REMOVED (explicitly out of scope for Phase-1)
  - AI-Assist Readiness -> REMOVED (explicitly out of scope for Phase-1)
- Added sections:
  - Explicit Constraints section with Runtime Limitations and Prohibited Actions
  - Success Criteria section with Phase-1 specific validation
  - Scope Boundary section defining Phase-1 limits
  - Authority hierarchy for conflict resolution
- Removed sections:
  - Forward Compatibility (Phase-2+ concern)
  - AI-Assist Readiness (Phase-2+ concern)
- Templates requiring updates:
  - ✅ .specify/templates/plan-template.md (Constitution Check updated)
  - ✅ .specify/templates/spec-template.md (aligned with Phase-1 constraints)
  - ✅ .specify/templates/tasks-template.md (aligned with in-memory, console-only scope)
- Follow-up TODOs: None
-->

# Phase-1 In-Memory Python Console Todo Application Constitution

## Core Principles

### Simplicity Over Cleverness
Phase-1 MUST use minimal, readable Python code suitable for console execution. Minimal dependencies (standard library only) and clear logic are paramount. No manual coding is permitted—all code must be generated following the Spec-Driven Development workflow.

**Rationale**: Phase-1 establishes the foundation. Complexity added now will compound in future phases. Simplicity ensures the codebase remains maintainable and easily understandable by junior developers and future AI agents.

### Deterministic Behavior
All operations MUST produce predictable, testable outputs. Given the same input sequence, the system MUST respond with identical output every time. No randomness, no time-based variation (except timestamps for display purposes).

**Rationale**: Console applications must be reliably testable. Deterministic behavior enables automated testing and ensures users can trust the application's consistency.

### In-Memory State Integrity
Todo data exists ONLY in memory during runtime. No persistence to files, databases, or external storage is permitted in Phase-1. State management MUST be reliable, self-contained, and reset on every program restart.

**Rationale**: Phase-1 focuses on core logic and user experience. Adding persistence introduces complexity (file I/O, serialization, error recovery) that is explicitly deferred to Phase-2. In-memory storage keeps the implementation simple and forces clear thinking about data structures.

### Spec-Driven Development Mandate
Every feature MUST map directly to an explicit requirement in the specification. Development MUST follow the strict sequence: Constitution → Specification → Plan → Tasks → Implementation. No code may be written manually or out-of-sequence.

**Rationale**: Manual coding leads to drift from requirements, untested behavior, and technical debt. The SDD workflow ensures every line of code is justified, planned, and testable.

## Key Standards

### Phase-1 Technical Requirements
- **Language**: Python 3.13+ (minimum version enforced)
- **Execution Mode**: Console/Terminal only (stdin/stdout interaction)
- **State Management**: Todos stored in in-memory data structures (list/dict). No persistence permitted.
- **Architecture**: Single entry point (main.py) with clear separation of concerns:
  - Input handling (menu, prompts)
  - Business logic (task operations)
  - Output rendering (display formatting)
- **Coding Standards**:
  - Type hints mandatory for all function signatures
  - Single-purpose functions with descriptive names
  - Standard library only (no external dependencies except testing frameworks)
  - Beginner-friendly code structure

### User Experience Requirements
- **CLI Prompts**: Clear, numbered menus with explicit instructions
- **Feedback**: Every action MUST provide explicit confirmation or error message
- **Error Handling**: Graceful handling of invalid input (non-existent task IDs, malformed input)
  - No unhandled exceptions in normal use
  - User-friendly error messages guiding correction
- **Navigation**: Simple, intuitive menu-based navigation
- **Display**: Human-readable task listing with clear formatting

## Constraints

### Phase-1 Scope Limitations
**In Scope**:
- Add new todo tasks
- View/list all tasks
- Update existing task descriptions
- Delete tasks
- Mark tasks as complete/incomplete
- Basic task properties (ID, description, status)

**Out of Scope** (explicitly prohibited in Phase-1):
- Persistence (files, databases, cloud storage)
- Web interfaces or APIs
- Authentication or user management
- AI integration or natural language processing
- Network communication
- Multi-user support or concurrency
- Task priorities, tags, categories, due dates
- Search or filtering (may be reconsidered if simple)
- Data export/import

### Runtime Limitations
- **No Persistence**: Data is lost when the program exits (by design)
- **Single-Threaded**: No concurrency or parallel execution
- **Single Process**: No inter-process communication
- **Console Only**: No GUI, no web interface

### Prohibited Actions
- Writing code manually without following Constitution → Spec → Plan → Tasks sequence
- Adding features not explicitly specified in the Phase-1 specification
- Introducing external dependencies (except pytest for testing)
- Using files, databases, or any form of persistent storage
- Over-engineering with classes, design patterns, or abstractions not required by the specification
- Adding "future-proofing" code for Phase-2+ features

## Quality Standards

### Code Quality
- **Readability**: Code MUST be readable by junior Python developers
- **Naming**: Descriptive names for all functions, variables, and modules
- **Documentation**: Docstrings for all public functions; inline comments for non-obvious logic
- **Testing**: Unit tests for all business logic functions (if testing is specified)

### Error Handling
- **User Input**: All user input MUST be validated before processing
- **Invalid IDs**: Attempting to operate on non-existent task IDs MUST produce helpful error messages
- **Graceful Degradation**: Invalid input MUST NOT crash the application
- **Recovery**: Users MUST be able to return to the main menu after any error

### Testing
- **Testability**: All functions MUST be independently testable
- **Coverage**: Core business logic MUST have test coverage (if testing is specified)
- **Determinism**: Tests MUST be deterministic and repeatable

## Success Criteria

Phase-1 implementation is considered successful when ALL of the following are true:

1. **Functional Completeness**:
   - User can add new todo tasks
   - User can view all tasks
   - User can update task descriptions
   - User can delete tasks
   - User can mark tasks complete/incomplete
   - Task IDs are auto-incremented and unique

2. **Technical Compliance**:
   - Python 3.13+ compatible
   - Runs from terminal via `python src/main.py` (or similar)
   - All tasks stored in-memory only
   - No files, databases, or external storage used
   - Clean separation of input handling, business logic, and output

3. **User Experience**:
   - Clear menu-based navigation
   - Explicit feedback for every action
   - Graceful handling of all invalid input scenarios
   - Application never crashes during normal use

4. **Process Compliance**:
   - Implementation strictly follows the specification
   - All code generated via SDD workflow (no manual coding)
   - Constitution → Spec → Plan → Tasks → Implementation sequence followed

## Scope Boundary

This constitution applies ONLY to Phase-1 of the Todo application. The following are explicitly out of scope and MUST NOT be implemented in Phase-1:

- Web interfaces (FastAPI, React, Next.js) → Phase-2
- Persistent storage (files, SQLite, PostgreSQL, cloud databases) → Phase-2
- AI integration (natural language processing, LLM agents) → Phase-3+
- Authentication and user management → Phase-2+
- Cloud deployment and scaling → Phase-3+
- Advanced features (priorities, tags, search, filtering) → Phase-2+

If future phases require changes to these principles, a new constitution version MUST be ratified with explicit justification for deviations.

## Governance

### Authority Hierarchy
This constitution is the authoritative source for Phase-1 development standards. In case of conflict or ambiguity, the following hierarchy applies:

1. **Constitution** (this document) - highest authority
2. **Specification** (specs/*/spec.md) - functional requirements
3. **Plan** (specs/*/plan.md) - technical approach
4. **Tasks** (specs/*/tasks.md) - implementation sequence
5. **Implementation** (source code) - must conform to all above

### Amendment Process
Any deviation from constitutional principles MUST be:
1. Documented in the "Complexity Tracking" section of the implementation plan
2. Justified with specific rationale
3. Approved explicitly before implementation proceeds

### Versioning Policy
- **MAJOR**: Backward-incompatible principle changes, scope redefinition, or constraint removal
- **MINOR**: New principles added, materially expanded guidance, or new constraints
- **PATCH**: Clarifications, wording improvements, typo fixes, non-semantic changes

### Compliance Review
Every specification, plan, and task list MUST include a "Constitution Check" section verifying compliance with these principles before implementation begins.

---

**Version**: 2.0.0
**Ratified**: 2026-01-02
**Last Amended**: 2026-01-03
