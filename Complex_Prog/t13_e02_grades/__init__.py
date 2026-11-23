# Read `data/grades.csv`, which has the columns `student,subject,score`, and build a command line
# tool with `argparse` subcommands:

# - `report` prints a table of every student and subject, with the average and letter grade, best
#   student first. Then it prints the mean, median and range for each subject and the students
#   averaging below 60.
# - `student NAME` prints one student's scores and average.
# - `top N` prints the best N students.
# - `add NAME SUBJECT SCORE` adds or updates a score and saves the CSV. A score outside 0 to 100 is rejected.

# The letter grades are A for 90 and above, B for 80 and above, C for 70 and above, D for 60 and
# above, and F below 60. Rows with a missing or invalid score are skipped, with a warning that
# gives the line number.

# Suggested modules: `models.py` (`Student`, `letter_grade`), `gradebook.py` (`GradeBook` with CSV
# load and save and statistics), `cli.py`

from .models import Student, letter_grade
from .gradebook import GradeBook

__all__ = ["Student", "letter_grade", "GradeBook"]