"""Example module used by the MyST + Sphinx autodoc documentation."""


def add_numbers(left: float, right: float) -> float:
    """Return the sum of two numbers.

    :param left: The first value to add.
    :param right: The second value to add.
    :returns: The combined total.
    """

    return left + right


def repeat_text(text: str, times: int = 2, *, separator: str = " | ") -> str:
    """Repeat a piece of text a configurable number of times.

    :param text: The text to repeat.
    :param times: How many times the text should appear.
    :param separator: The delimiter inserted between repetitions.
    :returns: A single string containing the repeated text.
    :raises ValueError: If ``times`` is less than 1.
    """

    if times < 1:
        raise ValueError("times must be at least 1")

    return separator.join(text for _ in range(times))


class Greeter:
    """Build consistent greeting messages.

    :param greeting: Prefix used at the beginning of each greeting.
    """

    def __init__(self, greeting: str = "Hello") -> None:
        self.greeting = greeting

    def greet(self, name: str) -> str:
        """Return a greeting for one person.

        :param name: Name to include in the greeting.
        :returns: A greeting sentence.
        """

        return f"{self.greeting}, {self._normalize_name(name)}!"

    def excited_greet(self, name: str) -> str:
        """Return an enthusiastic greeting.

        :param name: Name to include in the greeting.
        :returns: A greeting sentence in uppercase.
        """

        return self.greet(name).upper()

    def _normalize_name(self, name: str) -> str:
        return name.strip().title()
