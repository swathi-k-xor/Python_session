# `percent_to_grade(score)` returns `A` for 90 and above, `B` for 80 and above, `C` for 70 and above, `D` for 60 and above and `F` otherwise. Scores outside 0 to 100 raise `ValueError`; a score that is not a number raises `TypeError`. `average(scores)` returns the mean of a list and raises `ValueError` for an empty list. `has_passed(score, pass_mark=50)` is true at or above the pass mark.

# Write tests that check each function with several inputs, especially the boundary values (the number just at, and just below, each limit). Then test the errors with `pytest.raises`:

# 1. `percent_to_grade(101)` raises `ValueError`.
# 2. `percent_to_grade(-1)` raises `ValueError` and the message contains `between 0 and 100` (use `match=`).
# 3. `percent_to_grade("eighty")` raises `TypeError`; capture the exception with `as excinfo` and assert that `str(excinfo.value)` is `score must be a number`.
# 4. `average([])` raises `ValueError` mentioning `no scores`.
# 5. `average([80, 120])` raises `ValueError` (a bad score inside the list).
# 6. A valid call such as `percent_to_grade(50)` does not raise (a test with no `assert` that simply must not crash).

# ### Behaviours to test

# | Input | Expected |
# |-------|----------|
# | 95, 85, 75, 65, 30 | A, B, C, D, F |
# | 90, 80, 70, 60 | A, B, C, D (lower boundaries) |
# | 89.99, 79, 69, 59 | B, C, D, F (just below) |
# | 0 and 100 | F and A |
# | `average([80, 90, 100])`, `average([50])`, `average([1, 2])` | 90, 50, 1.5 |
# | `has_passed(50)`, `has_passed(49)`, `has_passed(70, pass_mark=75)` | True, False, False |
# | 101, -1, "eighty", `[]`, `[80, 120]` | the errors listed above |

"""Grade helpers for a small training course. This is the code under test: do not change it."""


def _check_score(score):
    if isinstance(score, bool) or not isinstance(score, (int, float)):
        raise TypeError("score must be a number")
    if score < 0 or score > 100:
        raise ValueError("score must be between 0 and 100")


def percent_to_grade(score):
    """Return A (90+), B (80+), C (70+), D (60+) or F for a score from 0 to 100."""
    _check_score(score)
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


def average(scores):
    """Return the mean of a non-empty list of scores."""
    if not scores:
        raise ValueError("no scores to average")
    for score in scores:
        _check_score(score)
    return sum(scores) / len(scores)


def has_passed(score, pass_mark=50):
    """Return True when the score is at or above the pass mark."""
    _check_score(score)
    return score >= pass_mark