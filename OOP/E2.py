# Write a custom exception `InsufficientFundsError` that inherits from `ValueError`, and a class `BankAccount`
# created with `owner` and an optional starting `balance` (default `0`).

# - `deposit(amount)` adds to the balance. If `amount <= 0` raise `ValueError("Deposit must be positive")`.
# - `withdraw(amount)` subtracts from the balance. If `amount <= 0` raise `ValueError("Withdrawal must be positive")`.
#   If `amount` is more than the balance raise `InsufficientFundsError(f"Cannot withdraw {amount}, balance is {balance}")`.
# - Every successful operation is recorded in `self.history` as a tuple `("deposit", amount)` or `("withdraw", amount)`.
# - `statement()` returns a multi-line string: a header `Statement for <owner>`, one line per history entry
#   (kind left-aligned in 10 characters, amount right-aligned in 8 characters), and a final `Balance: <n>` line.

# ### Sample input

# Your solution must work with this driver code, placed at the bottom of your file:

# ```python
# acc = BankAccount("Maria")
# acc.deposit(200)
# acc.withdraw(75)
# try:
#     acc.withdraw(500)
# except InsufficientFundsError as err:
#     print("Error:", err)
# try:
#     acc.deposit(-5)
# except ValueError as err:
#     print("Error:", err)
# print(acc.statement())
# ```

class InsufficientFundsError(ValueError):
    pass


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")

        self.balance += amount
        self.history.append(("deposit", amount))

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Cannot withdraw {amount}, balance is {self.balance}"
            )

        self.balance -= amount
        self.history.append(("withdraw", amount))

    def statement(self):
        lines = [f"Statement for {self.owner}"]
        for kind, amount in self.history:
            lines.append(f"{kind:<10}{amount:>8}")
        lines.append(f"Balance: {self.balance}")
        return "\n".join(lines)


if __name__ == "__main__":
    acc = BankAccount("Maria")
    acc.deposit(200)
    acc.withdraw(75)

    try:
        acc.withdraw(500)
    except InsufficientFundsError as err:
        print("Error:", err)

    try:
        acc.deposit(-5)
    except ValueError as err:
        print("Error:", err)

    print(acc.statement())
