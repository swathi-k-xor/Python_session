# Write a class `Book` that is created with `title`, `author` and `pages`. It must also have an attribute
# `current_page` that starts at `0`.

# - `describe()` returns a string like `'Dune' by Frank Herbert (412 pages)` (title in single quotes).
# - `read(count)` moves `current_page` forward by `count` pages but never past the last page.
# - `progress()` returns the percentage read, rounded to one decimal place (`current_page / pages * 100`).

# ### Sample input

# Your solution must work with this driver code, placed at the bottom of your file:

# ```python
# book = Book("Dune", "Frank Herbert", 412)
# print(book.describe())
# print(book.progress())
# book.read(103)
# print(book.current_page)
# print(book.progress())
# book.read(500)
# print(book.current_page)
# print(book.progress())
# ```


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 0

    def describe(self):
        return f"'{self.title}' by {self.author} ({self.pages} pages)"

    def read(self, count):
        self.current_page = min(self.current_page + count, self.pages)

    def progress(self):
        return round(self.current_page / self.pages * 100, 1)


if __name__ == "__main__":
    book = Book("Dune", "Frank Herbert", 412)
    print(book.describe())
    print(book.progress())
    book.read(103)
    print(book.current_page)
    print(book.progress())
    book.read(500)
    print(book.current_page)
    print(book.progress())