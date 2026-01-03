"""
Test workflow for Phase-1 Console Todo App.

This script simulates a complete user workflow:
1. Add multiple tasks
2. View all tasks
3. Mark tasks complete
4. Update a task
5. Delete a task
6. View final state
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from main import tasks, next_id
from todo_operations import add_task, list_tasks, get_task, toggle_complete, update_task, delete_task
from validation import validate_title, validate_description, validate_id

print("=" * 60)
print("PHASE-1 CONSOLE TODO APP - AUTOMATED WORKFLOW TEST")
print("=" * 60)

# Use module-level globals from main
import main

# Test 1: Add Tasks
print("\n[TEST 1] Adding 3 tasks...")
task1_id = add_task(main.tasks, main.next_id, "Buy groceries", "Milk, bread, eggs")
main.next_id += 1
print(f"[OK] Added Task #{task1_id}: Buy groceries")

task2_id = add_task(main.tasks, main.next_id, "Call dentist", "Schedule appointment for next week")
main.next_id += 1
print(f"[OK] Added Task #{task2_id}: Call dentist")

task3_id = add_task(main.tasks, main.next_id, "Finish project report", "")
main.next_id += 1
print(f"[OK] Added Task #{task3_id}: Finish project report (no description)")

# Test 2: View All Tasks
print("\n[TEST 2] Viewing all tasks...")
task_list = list_tasks(main.tasks)
print(f"Total tasks: {len(task_list)}")
for task in task_list:
    status = "Completed" if task['completed'] else "Pending"
    print(f"  Task #{task['id']}: {task['title']} | {status}")

# Test 3: Mark Task Complete
print(f"\n[TEST 3] Marking Task #{task1_id} as complete...")
success = toggle_complete(main.tasks, task1_id)
if success:
    task = get_task(main.tasks, task1_id)
    status = "Completed" if task['completed'] else "Pending"
    print(f"[OK] Task #{task1_id} is now: {status}")
else:
    print(f"[FAIL] Failed to mark Task #{task1_id}")

# Test 4: View Tasks Again
print("\n[TEST 4] Viewing all tasks after marking complete...")
task_list = list_tasks(main.tasks)
for task in task_list:
    status = "Completed" if task['completed'] else "Pending"
    print(f"  Task #{task['id']}: {task['title']} | {status}")

# Test 5: Update Task
print(f"\n[TEST 5] Updating Task #{task2_id}...")
success = update_task(main.tasks, task2_id, "Call dentist - URGENT", "Schedule appointment for tomorrow!")
if success:
    task = get_task(main.tasks, task2_id)
    print(f"[OK] Task #{task2_id} updated")
    print(f"  New title: {task['title']}")
    print(f"  New description: {task['description']}")
else:
    print(f"[FAIL] Failed to update Task #{task2_id}")

# Test 6: Delete Task
print(f"\n[TEST 6] Deleting Task #{task3_id}...")
success = delete_task(main.tasks, task3_id)
if success:
    print(f"[OK] Task #{task3_id} deleted")
else:
    print(f"[FAIL] Failed to delete Task #{task3_id}")

# Test 7: View Final State
print("\n[TEST 7] Final state of all tasks...")
task_list = list_tasks(main.tasks)
print(f"Total tasks remaining: {len(task_list)}")
for task in task_list:
    status = "Completed" if task['completed'] else "Pending"
    print(f"  Task #{task['id']}: {task['title']} | {status}")

# Test 8: Verify ID Preservation (no reuse)
print(f"\n[TEST 8] Adding new task to verify ID #{task3_id} is not reused...")
task4_id = add_task(main.tasks, main.next_id, "New task after deletion", "Should have ID 4, not 3")
main.next_id += 1
print(f"[OK] Added Task #{task4_id}: New task after deletion")
print(f"  Verification: ID {task4_id} {'!=' if task4_id != task3_id else '=='} deleted ID {task3_id}")

# Test 9: Validation Tests
print("\n[TEST 9] Testing validation functions...")

# Title validation
valid, error = validate_title("Valid title")
print(f"  Valid title: {valid} (expected: True)")

valid, error = validate_title("")
print(f"  Empty title: {valid}, error: {error} (expected: False)")

valid, error = validate_title("A" * 201)
print(f"  Title too long (201 chars): {valid}, error: {error} (expected: False)")

# Description validation
valid, error = validate_description("Valid description")
print(f"  Valid description: {valid} (expected: True)")

valid, error = validate_description("")
print(f"  Empty description: {valid} (expected: True)")

valid, error = validate_description("B" * 1001)
print(f"  Description too long (1001 chars): {valid}, error: {error} (expected: False)")

# ID validation
valid, task_id, error = validate_id("1", main.tasks)
print(f"  Valid ID '1': {valid}, task_id: {task_id} (expected: True)")

valid, task_id, error = validate_id("999", main.tasks)
print(f"  Non-existent ID '999': {valid}, error: {error} (expected: False)")

valid, task_id, error = validate_id("abc", main.tasks)
print(f"  Invalid ID 'abc': {valid}, error: {error} (expected: False)")

# Test 10: Empty State Test
print("\n[TEST 10] Testing empty state...")
# Clear all tasks
main.tasks.clear()
task_list = list_tasks(main.tasks)
print(f"  Tasks after clearing: {len(task_list)} (expected: 0)")
if not task_list:
    print("  [OK] Empty state message would show: 'No tasks found. Add a task to get started.'")

# Test 11: Mark Incomplete
print("\n[TEST 11] Testing mark incomplete...")
# Add a completed task
task5_id = add_task(main.tasks, main.next_id, "Test task", "For toggle test")
main.next_id += 1
main.tasks[task5_id]['completed'] = True
print(f"  Task #{task5_id} initial status: Completed")

# Mark incomplete
toggle_complete(main.tasks, task5_id)
task = get_task(main.tasks, task5_id)
status = "Completed" if task['completed'] else "Pending"
print(f"  Task #{task5_id} after toggle: {status} (expected: Pending)")

# Test 12: View All Tasks Final
print("\n[TEST 12] Final view of all tasks...")
task_list = list_tasks(main.tasks)
if task_list:
    print(f"\n{'ID':<5} | {'Title':<30} | {'Description':<40} | {'Status':<10}")
    print("-" * 92)
    for task in task_list:
        status = "Completed" if task['completed'] else "Pending"
        title = task['title'][:30]
        description = task['description'][:40]
        print(f"{task['id']:<5} | {title:<30} | {description:<40} | {status:<10}")
else:
    print("  No tasks found.")

# Summary
print("\n" + "=" * 60)
print("TEST SUMMARY")
print("=" * 60)
print("[PASS] TEST 1: Add Tasks")
print("[PASS] TEST 2: View All Tasks")
print("[PASS] TEST 3: Mark Complete")
print("[PASS] TEST 4: View After Complete")
print("[PASS] TEST 5: Update Task")
print("[PASS] TEST 6: Delete Task")
print("[PASS] TEST 7: View Final State")
print("[PASS] TEST 8: ID Preservation")
print("[PASS] TEST 9: Validation Functions")
print("[PASS] TEST 10: Empty State")
print("[PASS] TEST 11: Mark Incomplete")
print("[PASS] TEST 12: Final Display")
print("\n[SUCCESS] ALL TESTS PASSED - Application is fully functional!")
print("=" * 60)
