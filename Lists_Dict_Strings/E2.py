# Names typed by users are messy. Write `clean_name(raw)` that removes leading and trailing spaces, collapses repeated inner spaces to one space, and converts to title case. Write `initials(name)` that returns the initials separated by dots, for example `"Anna Maria Smith"` gives `"A.M.S."`. For each raw name print the cleaned name (with `repr`, so quotes are visible) and its initials.

# ### Sample input

# ```python
# names = ["  aNNa   maRIA  smith ", "o'brien   john", "MARY-JANE watson", "li   wei"]
# ```

def clean_name(raw):
    # Remove extra spaces and convert to title case
    return " ".join(raw.split()).title()


def initials(name):
    # Get first letter of each word and join with dots
    return ".".join(part[0] for part in name.split()) + "."


names = [" aNNa maRIA smith ", "o'brien john", "MARY-JANE watson", "li wei","Swathi C K"]

for raw in names:
    cleaned = clean_name(raw)
    print(f"{cleaned!r} -> {initials(cleaned)}")