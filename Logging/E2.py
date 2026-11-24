# Register a custom level `NOTICE` with number 25 (between `INFO` and `WARNING`) using `logging.addLevelName`.

# Write a handler class `ListHandler(logging.Handler)` that keeps every record it receives in a list called `records`.

# Write `emitted_at(threshold)`: it uses a logger named `levels.demo` (with `propagate = False` and one `ListHandler`), sets the logger level to `threshold` (a level name such as `"WARNING"`), logs one message at each of `DEBUG, INFO, NOTICE, WARNING, ERROR, CRITICAL` and returns the list of level names that were actually recorded.

# Write `enabled_flags(threshold)` that returns a dict mapping each of the six level names to `logger.isEnabledFor(level)` for the same logger.

# Print the level numbers, then `emitted_at` for the thresholds `DEBUG`, `NOTICE`, `WARNING` and `CRITICAL` (name left-aligned to width 9, then `-> ` and the names joined by `, `), then the `enabled_flags("ERROR")` dict.
    

import logging


NOTICE = 25
logging.addLevelName(NOTICE, "NOTICE")

LEVELS = (
    ("DEBUG", logging.DEBUG),
    ("INFO", logging.INFO),
    ("NOTICE", NOTICE),
    ("WARNING", logging.WARNING),
    ("ERROR", logging.ERROR),
    ("CRITICAL", logging.CRITICAL),
)


class ListHandler(logging.Handler):
    def __init__(self):
        super().__init__()
        self.records = []

    def emit(self, record):
        self.records.append(record)


def emitted_at(threshold):
    logger = logging.getLogger("levels.demo")
    logger.propagate = False
    logger.setLevel(threshold)

    handler = ListHandler()
    logger.addHandler(handler)
    try:
        for _, level in LEVELS:
            logger.log(level, "message at level %s", logging.getLevelName(level))
        return [record.levelname for record in handler.records]
    finally:
        logger.removeHandler(handler)


def enabled_flags(threshold):
    logger = logging.getLogger("levels.demo")
    logger.propagate = False
    logger.setLevel(threshold)
    return {
        name: logger.isEnabledFor(level)
        for name, level in LEVELS
    }


def main():
    level_numbers = logging.getLevelNamesMapping()
    names = ", ".join(
        f"{name}={level_numbers[name]}"
        for name, _ in LEVELS
    )
    print(f"Level numbers: {names}")

    for threshold in ("DEBUG", "NOTICE", "WARNING", "CRITICAL"):
        emitted = ", ".join(emitted_at(threshold))
        print(f"{threshold:<9}-> {emitted}")

    print(f"isEnabledFor at ERROR: {enabled_flags('ERROR')}")


if __name__ == "__main__":
    main()