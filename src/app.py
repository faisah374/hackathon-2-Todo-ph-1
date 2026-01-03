import sys
from src.manager import TodoManager
from src.views import format_todo_list, help_menu

def main():
    """Main application loop."""
    manager = TodoManager()
    print("Welcome to the In-Memory Todo App!")
    print("Type 'help' for a list of commands.")

    while True:
        try:
            line = input("\ntodo> ").strip()
            if not line:
                continue

            parts = line.split(maxsplit=1)
            cmd = parts[0].lower()
            args = parts[1] if len(parts) > 1 else ""

            if cmd == "exit":
                print("Goodbye!")
                break

            elif cmd == "help":
                print(help_menu())

            elif cmd == "add":
                if not args:
                    print("Error: add requires a description.")
                else:
                    todo_id = manager.add_todo(args)
                    print(f"Task added with ID: {todo_id}")

            elif cmd == "list":
                print(format_todo_list(manager.get_all_todos()))

            elif cmd == "complete":
                if not args:
                    print("Error: complete requires an ID.")
                else:
                    try:
                        tid = int(args)
                        if manager.mark_completed(tid):
                            print(f"Task {tid} marked as completed.")
                        else:
                            print(f"Error: Task ID {tid} not found.")
                    except ValueError:
                        print(f"Error: {args} is not a valid ID.")

            elif cmd == "update":
                if not args or " " not in args:
                    print("Error: update requires an ID and a new description.")
                else:
                    try:
                        id_str, new_text = args.split(maxsplit=1)
                        tid = int(id_str)
                        if manager.update_todo(tid, new_text):
                            print(f"Task {tid} updated.")
                        else:
                            print(f"Error: Task ID {tid} not found.")
                    except ValueError:
                        print(f"Error: Invalid ID format.")

            elif cmd == "delete":
                if not args:
                    print("Error: delete requires an ID.")
                else:
                    try:
                        tid = int(args)
                        if manager.delete_todo(tid):
                            print(f"Task {tid} deleted.")
                        else:
                            print(f"Error: Task ID {tid} not found.")
                    except ValueError:
                        print(f"Error: {args} is not a valid ID.")

            else:
                print(f"Unknown command: {cmd}. Type 'help' for options.")

        except EOFError:
            print("\nGoodbye!")
            break
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    main()
