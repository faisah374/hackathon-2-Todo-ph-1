# CLI Command Contracts: In-Memory Console Todo App

## Commands

### ADD
- **Format**: `add <description>`
- **Example**: `add Buy groceries`
- **Output**: `Task added with ID: 1`

### LIST
- **Format**: `list`
- **Output**:
  ```text
  [ ] 1: Buy groceries
  [X] 2: Clean room
  ```

### COMPLETE
- **Format**: `complete <id>`
- **Example**: `complete 1`
- **Output**: `Task 1 marked as completed.`

### UPDATE
- **Format**: `update <id> <new description>`
- **Example**: `update 1 Buy organic milk`
- **Output**: `Task 1 updated.`

### DELETE
- **Format**: `delete <id>`
- **Example**: `delete 1`
- **Output**: `Task 1 deleted.`

### EXIT
- **Format**: `exit`
- **Output**: `Goodbye!`

## Error Responses
- **Invalid Command**: `Unknown command: <cmd>. Type 'help' for options.`
- **Missing Arguments**: `Error: <cmd> requires more arguments.`
- **Invalid ID**: `Error: Task ID <id> not found.`
- **Empty Description**: `Error: Task description cannot be empty.`
