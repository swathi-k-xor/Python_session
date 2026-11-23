# Build a to-do list manager with a numbered menu:

# 1. Add task. Ask for a title and a priority (`high`, `medium` or `low`). Pressing Enter gives `medium`.
# 2. List tasks. Show open tasks first, then sort by priority, then by id. Show `[x]` for done
#    and `[ ]` for open, and end with a count line.
# 3. Complete a task by id.
# 4. Delete a task by id.
# 5. Quit. Save and exit.

# Tasks are saved to a JSON file, chosen with `--file` (default `todo.json`), after every change,
# and loaded again at start-up. Bad input such as an unknown id, a non-number or a wrong menu choice
# prints a friendly message, and the menu keeps going. End of input (Ctrl+D or Ctrl+Z) behaves like Quit.

# Suggested modules: `models.py` (`Task` dataclass, `TodoList`), `storage.py` (`load`, `save`),
# `cli.py` (menu loop), `__main__.py`.

from .cli import main


if __name__ == "__main__":
    main()