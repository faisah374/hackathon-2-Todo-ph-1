# Quickstart Guide: Phase-1 Console Todo App

**Feature**: 002-console-todo
**For**: End Users
**Date**: 2026-01-04

## Prerequisites

- Python 3.13 or higher installed
- Terminal/Command prompt access
- Basic keyboard input skills

## Installation

1. Navigate to the project directory:
   ```bash
   cd path/to/hackathon-2-Todo-ph-1
   ```

2. No dependencies to install (standard library only)

## Running the Application

Start the application from the command line:

```bash
python src/main.py
```

Or on some systems:

```bash
python3 src/main.py
```

## Using the Application

### Main Menu

When you start the app, you'll see:

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

### 1. Adding a Task

1. Enter `1` at the main menu
2. Enter a task title (1-200 characters, required)
3. Enter a description (0-1000 characters, optional - press Enter to skip)
4. You'll see: "Task #N added successfully"

**Example**:
```
Enter your choice (1-7): 1
Enter task title: Buy groceries
Enter description (optional): Milk, bread, eggs
Task #1 added successfully
```

### 2. Viewing All Tasks

1. Enter `2` at the main menu
2. All tasks display in a table format:
   ```
   ID    | Title               | Description           | Status
   ---------------------------------------------------------------------------
   1     | Buy groceries       | Milk, bread, eggs     | Pending
   2     | Call dentist        |                       | Completed
   ```

3. If no tasks exist: "No tasks found. Add a task to get started."

### 3. Updating a Task

1. Enter `3` at the main menu
2. Enter the task ID to update
3. Enter new title (or press Enter to keep current)
4. Enter new description (or press Enter to keep current)
5. You'll see: "Task #N updated successfully"

**Example**:
```
Enter your choice (1-7): 3
Enter task ID: 1
Enter new title (or press Enter to keep current): Buy groceries and toiletries
Enter new description (or press Enter to keep current): Milk, bread, eggs, shampoo
Task #1 updated successfully
```

### 4. Deleting a Task

1. Enter `4` at the main menu
2. Enter the task ID to delete
3. You'll see: "Task #N deleted successfully"

**Example**:
```
Enter your choice (1-7): 4
Enter task ID: 2
Task #2 deleted successfully
```

**Note**: Deleted task IDs are never reused.

### 5. Marking a Task Complete

1. Enter `5` at the main menu
2. Enter the task ID to mark as complete
3. You'll see: "Task #N marked as complete"

**Example**:
```
Enter your choice (1-7): 5
Enter task ID: 1
Task #1 marked as complete
```

### 6. Marking a Task Incomplete

1. Enter `6` at the main menu
2. Enter the task ID to mark as incomplete
3. You'll see: "Task #N marked as incomplete"

### 7. Exiting the Application

1. Enter `7` at the main menu
2. You'll see: "All data will be lost. Are you sure? (y/n):"
3. Enter `y` to exit or `n` to return to menu
4. If you exit: "Goodbye!"

**IMPORTANT**: All tasks are stored in memory only. When you exit, all data is lost permanently.

## Common Workflows

### Daily Task Management

**Start of day - Add tasks**:
1. Run app: `python src/main.py`
2. Press `1` → Add task: "Review emails"
3. Press `1` → Add task: "Prepare presentation"
4. Press `1` → Add task: "Team meeting at 2pm"

**Check progress**:
5. Press `2` → View all tasks

**Complete tasks**:
6. Press `5` → Enter task ID → Mark complete
7. Repeat for each completed task

**End of day - Review**:
8. Press `2` → View all tasks (see completed vs pending)
9. Press `7` → `y` → Exit (data lost - by design)

### Correcting Mistakes

**Fix typo in title**:
1. Press `3` (Update Task)
2. Enter task ID
3. Enter corrected title
4. Press Enter to keep description

**Remove incorrect task**:
1. Press `4` (Delete Task)
2. Enter task ID

## Error Messages

| Error Message | Meaning | Solution |
|---------------|---------|----------|
| "Invalid choice. Please enter a number from the menu (1-7)" | Menu input out of range | Enter a number between 1 and 7 |
| "Title is required" | Empty or whitespace-only title | Enter at least one character |
| "Title must be 1-200 characters" | Title too long | Shorten title to 200 chars or less |
| "Description must be 0-1000 characters" | Description too long | Shorten description to 1000 chars |
| "Invalid ID. Please enter a number" | Non-numeric task ID | Enter a number (e.g., 1, 2, 3) |
| "Task #N not found" | Task ID doesn't exist | Check ID with "View All Tasks" (option 2) |
| "Please enter 'y' or 'n'" | Invalid exit confirmation | Type y or n (case-insensitive) |

## Tips & Best Practices

1. **Check IDs before operations**: Use "View All Tasks" to see current task IDs before updating/deleting/completing

2. **Use descriptions for details**: Keep titles short and descriptive, put details in description

3. **Review before exiting**: Remember that ALL data is lost on exit - review completed tasks before closing

4. **Empty descriptions OK**: Descriptions are optional - just press Enter to skip

5. **Case doesn't matter for y/n**: Exit confirmation accepts Y, y, N, or n

6. **Whitespace is trimmed**: Leading/trailing spaces automatically removed from titles and descriptions

7. **Unicode supported**: Emojis and international characters work in titles and descriptions

8. **ID gaps are normal**: After deleting tasks, you'll see gaps in IDs (e.g., 1, 3, 5) - this is expected

## Limitations (Phase-1)

This is Phase-1 of the Todo app with intentional limitations:

- ❌ No data persistence (lost on exit)
- ❌ No file save/load
- ❌ No database storage
- ❌ No web interface
- ❌ No user accounts
- ❌ No task priorities or tags
- ❌ No due dates
- ❌ No search or filtering
- ❌ No task sharing or collaboration

These features are planned for future phases (Phase-2+).

## Troubleshooting

### App won't start

**Error**: "python: command not found"
- **Solution**: Try `python3 src/main.py` or install Python 3.13+

**Error**: "No module named..."
- **Solution**: Ensure you're in the correct directory (where `src/` folder exists)

**Error**: "Python version too old"
- **Solution**: Upgrade to Python 3.13 or higher

### App crashes during use

**Unexpected error messages**:
- This shouldn't happen - the app is designed never to crash
- If you encounter crashes, please report with exact steps to reproduce

### Data disappeared

**All tasks gone after restart**:
- This is expected behavior in Phase-1
- All data stored in memory only
- Data lost when app exits
- You'll see warning: "All data will be lost. Are you sure? (y/n)"

## Getting Help

1. **Review error messages**: They provide specific guidance
2. **Check this guide**: Most common issues covered above
3. **View menu options**: All features listed in main menu
4. **Report bugs**: If app crashes or behaves unexpectedly, report with steps to reproduce

## Quick Reference

| Action | Menu Number | Requires |
|--------|-------------|----------|
| Add Task | 1 | Title (required), Description (optional) |
| View All Tasks | 2 | None |
| Update Task | 3 | Task ID, New title and/or description |
| Delete Task | 4 | Task ID |
| Mark Complete | 5 | Task ID |
| Mark Incomplete | 6 | Task ID |
| Exit | 7 | Confirmation (y/n) |

**Remember**: All data is lost when you exit. This is Phase-1 behavior by design.
