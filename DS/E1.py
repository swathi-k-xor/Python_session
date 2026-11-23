# A stack is last in, first out (LIFO): the last item you push is the first one you pop. Write a
# class `Stack` that stores its items in a Python list, with these methods:

# - `push(item)` adds an item to the top.
# - `pop()` removes and returns the top item. It raises `IndexError` if the stack is empty.
# - `peek()` returns the top item without removing it. It raises `IndexError` if the stack is empty.
# - `is_empty()` returns `True` or `False`.
# - `len(stack)` works, because you implement `__len__`.

# Then write `is_balanced(text)`. It uses your `Stack` to check that every `(`, `[` and `{` in
# `text` is closed by the matching bracket in the right order. Other characters are ignored.

# ### Sample input

# ```python
# s = Stack()
# for n in [10, 20, 30]:
#     s.push(n)
# print("size:", len(s))
# print("peek:", s.peek())
# print("pop:", s.pop())
# print("size after pop:", len(s))
# for text in ["(a + b) * [c]", "{[()]}", "(]", "((x)"]:
#     print(f"{text!r} balanced: {is_balanced(text)}")
# ```

class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def __len__(self):
        return len(self._items)


def is_balanced(text):
    stack = Stack()
    opening = {"(": ")", "[": "]", "{": "}"}
    closing = {")": "(", "]": "[", "}": "{"}

    for character in text:
        if character in opening:
            stack.push(character)
        elif character in closing:
            if stack.is_empty() or stack.pop() != closing[character]:
                return False

    return stack.is_empty()


if __name__ == "__main__":
    s = Stack()
    for n in [10, 20, 30]:
        s.push(n)

    print("size:", len(s))
    print("peek:", s.peek())
    print("pop:", s.pop())
    print("size after pop:", len(s))

    for text in ["(a + b) * [c]", "{[()]}", "(]", "((x)"]:
        print(f"{text!r} balanced: {is_balanced(text)}")