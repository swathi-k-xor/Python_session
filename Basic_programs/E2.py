# Read one line containing several scores separated by spaces. Write `grade(score)`: 90 and above is `A`, 80 to 89 `B`, 70 to 79 `C`, 60 to 69 `D`, below 60 `F`. A token is valid only if it is a whole number from 0 to 100; anything else (for example `-5`, `abc`, `4.5`, `101`) is printed as `<token>: invalid` and is excluded from the average. Print `<score>: <grade>` for valid scores, then `Average of valid scores: <value>` with one decimal, or `No valid scores` when there are none.

# ### Sample input

# Typed into the program (standard input):

# ```text
# 95 82 67 45 100 -5 abc 73
# ```

def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


tokens = input("Enter the score: ").split()
valid_scores = []

for token in tokens:
    if token.isascii() and token.isdecimal():
        score = int(token)
        if 0 <= score <= 100:
            print(f"{score}: {grade(score)}")
            valid_scores.append(score)
        else:
            print(f"{token}: invalid")
    else:
        print(f"{token}: invalid")

if valid_scores:
    average = sum(valid_scores) / len(valid_scores)
    print(f"Average of valid scores: {average:.1f}")
else:
    print("No valid scores")