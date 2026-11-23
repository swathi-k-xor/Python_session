# Build a small notification service.

# - An abstract base class `Notifier` with an abstract method `send(recipient, message)` returning a string.
# - A dictionary `NOTIFIERS = {}` and a decorator factory `register(kind)` that stores a class in it.
# - Three concrete notifiers, registered as `"email"`, `"sms"` and `"push"`:
#   - `EmailNotifier.send` returns `EMAIL to <recipient>@example.com: <message>`
#   - `SmsNotifier.send` returns `SMS to <recipient>: <first 20 characters of the message>`
#   - `PushNotifier.send` returns `PUSH to <recipient>: <message in upper case>`
# - `create_notifier(kind)` returns a new notifier instance. An unknown kind raises
#   `ValueError(f"Unknown notifier: {kind} (choose from ...)")`, where the choices are the sorted registered names
#   separated by `, `.

# Adding a fourth notifier must need no change to `create_notifier`.

# ### Sample input

# Your solution must work with this driver code, placed at the bottom of your file:

# ```python
# for kind in ["email", "sms", "push"]:
#     print(create_notifier(kind).send("ana", "Your order has shipped today"))
# print(sorted(NOTIFIERS))
# try:
#     create_notifier("fax")
# except ValueError as err:
#     print("Error:", err)
# ```

from abc import ABC, abstractmethod
NOTIFIERS = {}
def register(kind):
    def decorator(cls):
        NOTIFIERS[kind] = cls
        return cls

    return decorator


class Notifier(ABC):
    @abstractmethod
    def send(self, recipient, message):
        pass


@register("email")
class EmailNotifier(Notifier):
    def send(self, recipient, message):
        return f"EMAIL to {recipient}@example.com: {message}"


@register("sms")
class SmsNotifier(Notifier):
    def send(self, recipient, message):
        return f"SMS to {recipient}: {message[:20]}"


@register("push")
class PushNotifier(Notifier):
    def send(self, recipient, message):
        return f"PUSH to {recipient}: {message.upper()}"


def create_notifier(kind):
    try:
        notifier_class = NOTIFIERS[kind]
    except KeyError:
        choices = ", ".join(sorted(NOTIFIERS))
        raise ValueError(
            f"Unknown notifier: {kind} (choose from {choices})"
        ) from None

    return notifier_class()


if __name__ == "__main__":
    for kind in ["email", "sms", "push"]:
        print(create_notifier(kind).send("ana", "Your order has shipped today"))

    print(sorted(NOTIFIERS))

    try:
        create_notifier("fax")
    except ValueError as err:
        print("Error:", err)