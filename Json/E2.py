# Load `data/config.json` with `json.load`. Write `get_nested(data, path, default=None)` that follows a dotted path such as `"server.timeouts.read"` and returns the value, or `default` when any step of the path is missing (also when a step is not a dictionary). A value of `False` or `0` is a real value and must be returned, not the default. Print each path in the list below as `<path> = <repr of value>`, using the default shown, then print the admins joined with `, ` and their count.

# ### Sample input

# ```text
# app.name
# server.port
# server.timeouts.read
# database.pool.max
# features.beta_dashboard
# cache.ttl            (default 60)
# server.host.name     (default "n/a")
# ```
# Data: `data/config.json`.

import json


def get_nested(data, path, default=None):
    current = data

    for key in path.split("."):
        if not isinstance(current, dict) or key not in current:
            return default
        current = current[key]

    return current


if __name__ == "__main__":
    with open(r"C:\Users\Swathi.K\Downloads\Python Training -Interns\Python Training -Interns\05-json\data\config.json", encoding="utf-8") as file:
        config = json.load(file)

    lookups = [
        ("app.name", None),
        ("server.port", None),
        ("server.timeouts.read", None),
        ("database.pool.max", None),
        ("features.beta_dashboard", None),
        ("cache.ttl", 60),
        ("server.host.name", "n/a"),
    ]

    for path, default in lookups:
        value = get_nested(config, path, default)
        print(f"{path} = {value!r}")

    admins = config["admins"]
    print(f"admins: {', '.join(admins)} ({len(admins)})")