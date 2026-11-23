import csv
import math
from pathlib import Path
from statistics import mean, median

from .models import Student


class GradeBook:
    def __init__(self, path):
        self.path = Path(path)
        self.students = {}
        self.warnings = []
        self._load()

    @property
    def subjects(self):
        return sorted({
            subject
            for student in self.students.values()
            for subject in student.scores
        })

    def _load(self):
        with self.path.open(encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)

            for line_number, row in enumerate(reader, start=2):
                name = (row.get("student") or "").strip()
                subject = (row.get("subject") or "").strip()
                raw_score = (row.get("score") or "").strip()

                try:
                    score = float(raw_score)
                except ValueError:
                    self.warnings.append(
                        f"Warning: line {line_number}: "
                        f"skipped bad score {raw_score!r} for {name}"
                    )
                    continue

                if not math.isfinite(score) or not 0 <= score <= 100:
                    self.warnings.append(
                        f"Warning: line {line_number}: "
                        f"skipped bad score {raw_score!r} for {name}"
                    )
                    continue

                student = self.students.setdefault(name, Student(name))
                student.scores[subject] = score

    def get_student(self, name):
        return self.students.get(name)

    def ranked_students(self):
        return sorted(
            self.students.values(),
            key=lambda student: (-student.average(), student.name),
        )

    def subject_statistics(self, subject):
        scores = [
            student.scores[subject]
            for student in self.students.values()
            if subject in student.scores
        ]
        if not scores:
            return None

        return mean(scores), median(scores), min(scores), max(scores), len(scores)

    def add_score(self, name, subject, score):
        if not math.isfinite(score) or not 0 <= score <= 100:
            raise ValueError(f"score must be 0-100, got {score}")

        student = self.students.setdefault(name, Student(name))
        student.scores[subject] = score

    def save(self):
        with self.path.open("w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["student", "subject", "score"])
            writer.writeheader()

            for student in sorted(self.students.values(), key=lambda item: item.name):
                for subject in sorted(student.scores):
                    writer.writerow({
                        "student": student.name,
                        "subject": subject,
                        "score": f"{student.scores[subject]:g}",
                    })