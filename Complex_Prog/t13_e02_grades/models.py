from dataclasses import dataclass, field
from statistics import mean


def letter_grade(score):
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


@dataclass
class Student:
    name: str
    scores: dict = field(default_factory=dict)

    def average(self):
        return mean(self.scores.values()) if self.scores else 0.0

    def grade(self):
        return letter_grade(self.average())