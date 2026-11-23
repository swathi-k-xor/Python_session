from dataclasses import dataclass


@dataclass
class Task:
    id: int
    title: str
    priority: str
    done: bool = False


class TodoList:
    PRIORITIES = {"high": 0, "medium": 1, "low": 2}

    def __init__(self, tasks=None):
        self.tasks = list(tasks) if tasks is not None else []
        self._next_id = max((task.id for task in self.tasks), default=0) + 1

    def add(self, title, priority="medium"):
        if priority not in self.PRIORITIES:
            raise ValueError("priority must be high, medium or low")

        task = Task(self._next_id, title, priority)
        self._next_id += 1
        self.tasks.append(task)
        return task

    def list_tasks(self):
        return sorted(
            self.tasks,
            key=lambda task: (
                task.done,
                self.PRIORITIES[task.priority],
                task.id,
            ),
        )

    def complete(self, task_id):
        task = self._find_task(task_id)
        task.done = True
        return task

    def delete(self, task_id):
        task = self._find_task(task_id)
        self.tasks.remove(task)
        return task

    def _find_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        raise ValueError(f"no task with id {task_id}")

    def __len__(self):
        return len(self.tasks)