# Write a class decorator `singleton(cls)` so that calling a decorated class always returns the
# same instance (the first call creates it; arguments of later calls are ignored). The decorator must also add a function
# attribute `reset()` that forgets the instance, which is useful in tests.

# Then write `AppConfig` decorated with `@singleton`:

# - `__init__(self, env="dev")` stores `env` and an empty dictionary `values`.
# - `set(key, value)` and `get(key, default=None)` read and write `values`.

# The driver shows two "different" constructions returning the same object, shared state, and what `reset()` does.

# ### Sample input

# Your solution must work with this driver code, placed at the bottom of your file:

# ```python
# a = AppConfig(env="prod")
# b = AppConfig(env="test")
# print(a is b)
# print(b.env)
# a.set("debug", False)
# print(b.get("debug"))
# print(b.get("missing", "n/a"))
# AppConfig.reset()
# c = AppConfig(env="test")
# print(c is a, c.env, c.get("debug", "gone"))
# print(type(c).__name__)
# ```

from functools import wraps


def singleton(cls):
    instances = {}

    @wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    def reset():
        instances.pop(cls, None)

    get_instance.reset = reset
    return get_instance


@singleton
class AppConfig:
    def __init__(self, env="dev"):
        self.env = env
        self.values = {}

    def set(self, key, value):
        self.values[key] = value

    def get(self, key, default=None):
        return self.values.get(key, default)


if __name__ == "__main__":
    a = AppConfig(env="prod")
    b = AppConfig(env="test")
    print(a is b)
    print(b.env)
    a.set("debug", False)
    print(b.get("debug"))
    print(b.get("missing", "n/a"))
    AppConfig.reset()
    c = AppConfig(env="test")
    print(c is a, c.env, c.get("debug", "gone"))
    print(type(c).__name__)