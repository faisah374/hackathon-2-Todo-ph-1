# Research: In-Memory Console Todo App

## Decision: Application Architecture
**Chosen**: Model-View-Controller (MVC) like separation.
**Rationale**: Keeps business logic (`manager.py`) isolated from console I/O (`views.py` and `app.py`). This ensures testability and makes it easy to swap the console view for a web API later.
**Alternatives considered**: Monolithic `main.py`. Rejected because it violates the constitution's "Clear separation of concerns" and "Forward Compatibility" principles.

## Decision: State Management
**Chosen**: `TodoManager` class holding a dictionary of `Todo` objects keyed by an auto-incrementing integer ID.
**Rationale**: Fast lookup by ID for updates/deletes and easy iteration for listing.
**Alternatives considered**: List of objects. Rejected because lookup/update by ID requires O(n) scan every time.

## Decision: Command Interface
**Chosen**: Loop with `input()` processing simple string commands: `add <text>`, `list`, `complete <id>`, `update <id> <text>`, `delete <id>`, `exit`.
**Rationale**: Simple to implement using standard library, easy for beginners to understand.
**Alternatives considered**: `argparse` for a true CLI. Rejected for Phase I as an interactive loop is more user-friendly for a standalone "app" experience requested.
