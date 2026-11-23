import argparse
from pathlib import Path

from .models import TodoList
from .storage import load, save


MENU = (
    "1) Add task  2) List tasks  3) Complete task  "
    "4) Delete task  5) Quit"
)


def _read_task_id():
    raw_id = input("Task id: ")
    try:
        return int(raw_id)
    except ValueError:
        print(f"{raw_id!r} is not a number.")
        return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", default="todo.json")
    args = parser.parse_args()

    file_path = Path(args.file)
    todo = TodoList(load(file_path))
    print(f"Loaded {len(todo)} task(s) from {args.file}")

    try:
        while True:
            print()
            print(MENU)
            choice = input("Choice: ").strip()

            if choice == "1":
                title = input("Title: ")
                priority = input("Priority (high/medium/low) [medium]: ")
                priority = priority.strip().lower() or "medium"

                try:
                    task = todo.add(title, priority)
                except ValueError as err:
                    print(f"Error: {err}")
                    continue

                save(file_path, todo.tasks)
                print(f"Added task {task.id}.")

            elif choice == "2":
                for task in todo.list_tasks():
                    marker = "[x]" if task.done else "[ ]"
                    print(f"{marker} {task.id:2}. {task.title} ({task.priority})")

                open_count = sum(not task.done for task in todo.tasks)
                done_count = len(todo) - open_count
                print(f"{open_count} open, {done_count} done")

            elif choice == "3":
                task_id = _read_task_id()
                if task_id is None:
                    continue

                try:
                    task = todo.complete(task_id)
                except ValueError as err:
                    print(f"Error: {err}")
                    continue

                save(file_path, todo.tasks)
                print(f"Completed: {task.title}")

            elif choice == "4":
                task_id = _read_task_id()
                if task_id is None:
                    continue

                try:
                    task = todo.delete(task_id)
                except ValueError as err:
                    print(f"Error: {err}")
                    continue

                save(file_path, todo.tasks)
                print(f"Deleted: {task.title}")

            elif choice == "5":
                break

            else:
                print("Please choose 1-5.")

    except EOFError:
        pass

    save(file_path, todo.tasks)
    print(f"Saved {len(todo)} task(s). Bye.")