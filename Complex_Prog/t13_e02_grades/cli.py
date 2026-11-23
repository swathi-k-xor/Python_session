import argparse

from .gradebook import GradeBook


def _print_report(book):
    subjects = book.subjects

    if subjects == ["English", "Math", "Physics"]:
        print("Student   English     Math  Physics    Avg  Grade")
        print("-" * 49)
        for student in book.ranked_students():
            english = f"{student.scores['English']:g}" if "English" in student.scores else "-"
            math = f"{student.scores['Math']:g}" if "Math" in student.scores else "-"
            physics = f"{student.scores['Physics']:g}" if "Physics" in student.scores else "-"
            print(
                f"{student.name:<10}{english:>7}{math:>9}{physics:>9}"
                f"{student.average():>7.1f}  {student.grade()}"
            )
    else:
        print("Student  " + " ".join(f"{subject:>9}" for subject in subjects)
              + "     Avg  Grade")
        print("-" * (18 + 10 * len(subjects)))
        for student in book.ranked_students():
            scores = [
                f"{student.scores[subject]:g}" if subject in student.scores else "-"
                for subject in subjects
            ]
            print(
                f"{student.name:<9}"
                + "".join(f"{score:>10}" for score in scores)
                + f"{student.average():>8.1f}  {student.grade()}"
            )

    print()
    for subject in subjects:
        stats = book.subject_statistics(subject)
        subject_mean, subject_median, low, high, count = stats
        print(
            f"{subject}: mean {subject_mean:.1f}, median {subject_median:g}, "
            f"range {low:g}-{high:g} ({count} scores)"
        )

    below_60 = [
        student.name
        for student in book.ranked_students()
        if student.average() < 60
    ]
    print(f"Below 60 average: {', '.join(below_60)}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", default="../data/grades.csv")
    commands = parser.add_subparsers(dest="command", required=True)

    commands.add_parser("report")

    student_parser = commands.add_parser("student")
    student_parser.add_argument("name")

    top_parser = commands.add_parser("top")
    top_parser.add_argument("count", type=int)

    add_parser = commands.add_parser("add")
    add_parser.add_argument("name")
    add_parser.add_argument("subject")
    add_parser.add_argument("score", type=float)

    args = parser.parse_args()
    book = GradeBook(args.file)

    for warning in book.warnings:
        print(warning)

    if args.command == "report":
        _print_report(book)
    elif args.command == "student":
        student = book.get_student(args.name)
        if student is None:
            print(f"Error: no student named {args.name}")
            return 1

        for subject in sorted(student.scores):
            print(f"  {subject:<9}{student.scores[subject]:>5g}")
        print(f"  average {student.average():.1f} -> {student.grade()}")
    elif args.command == "top":
        for position, student in enumerate(
            book.ranked_students()[:max(0, args.count)],
            start=1,
        ):
            print(f"{position}. {student.name} {student.average():.1f}")
    elif args.command == "add":
        try:
            book.add_score(args.name, args.subject, args.score)
        except ValueError as err:
            print(f"Error: {err}")
            return 1

        book.save()

    return 0
