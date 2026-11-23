import json
import os
import tempfile
from dataclasses import asdict
from pathlib import Path

from .models import Task


def load(path):
    path = Path(path)
    if not path.exists():
        return []

    with path.open(encoding="utf-8") as file:
        records = json.load(file)

    return [Task(**record) for record in records]


def save(path, tasks):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary_path = None

    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=path.parent,
            prefix=path.name + ".",
            suffix=".tmp",
            delete=False,
        ) as file:
            temporary_path = Path(file.name)
            json.dump([asdict(task) for task in tasks], file, indent=2)
            file.write("\n")

        os.replace(temporary_path, path)
    finally:
        if temporary_path is not None and temporary_path.exists():
            temporary_path.unlink()