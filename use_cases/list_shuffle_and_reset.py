import random
from dataclasses import dataclass, field
from string.templatelib import Template
from typing import List


def safe_render(tmpl: Template) -> str:
    """
    Standard renderer for PEP 750 Template objects.
    Combines static strings and dynamic values safely.
    """
    result = []
    for i, static_part in enumerate(tmpl.strings):
        result.append(static_part)
        if i < len(tmpl.values):
            # Sanitize dynamic content to prevent markdown/terminal injection
            val = str(tmpl.values[i]).replace("*", r"\*")
            result.append(val)
    return "".join(result)


@dataclass
class StudentPicker:
    students: List[str]
    total_picks: int = 0
    total_capacity: int = field(init=False)
    pool: List[str] = field(default_factory=list, init=False)

    def __post_init__(self):
        # Set initial capacity and shuffle the first round
        self.total_capacity = len(self.students)
        self._reshuffle(initial=True)

    def _reshuffle(self, initial=False):
        """Refills the pool and increments the cumulative capacity."""
        if not initial:
            self.total_capacity += len(self.students)
            print(f"\n--- Round Exhausted. New capacity: {self.total_capacity} ---")

        self.pool = list(self.students)
        random.shuffle(self.pool)

    def pick(self) -> Template:
        """Handles the X of Y progression and returns a t-string Template."""
        if not self.pool:
            self._reshuffle()

        self.total_picks += 1
        name = self.pool.pop()

        # Correct PEP 750 syntax: uses {} for interpolation
        return t"[{self.total_picks} of {self.total_capacity}] Selected: {name}"


# --- Main Execution ---


def main():
    names = ["Alex", "Blake", "Chris", "Cameron", "Dylan", "Elliot", "Jordan", "Kai", "Jaime", "Morgan", "Riley", "Sam", "Taylor"]
    picker = StudentPicker(students=names)

    print("--- Fair Choice Selector ---")

    while True:
        try:
            user_input = (
                input("\nPress Enter to pick (or 'q' to quit): ").strip().lower()
            )
            if user_input == "q":
                break

            # Generate the template
            selection_template = picker.pick()

            # Render and display
            print(safe_render(selection_template))

        except KeyboardInterrupt:
            break

    print("\nSession closed.")


if __name__ == "__main__":
    main()
