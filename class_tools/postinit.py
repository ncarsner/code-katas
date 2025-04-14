from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional
import random

user_list = ["Alex", "Blake", "Chris", "Dylan", "Elliott", None]


@dataclass
class Report:
    """
    A class to represent a BI report.

    Attributes:
        title (str): The title of the report.
        created_by (str): The name of the person who created the report.
        created_at (datetime): The timestamp when the report was created.
        filters (Optional[List[str]]): A list of filters applied to the report.
    """

    title: str
    created_by: str = field(default_factory=lambda: "System User")
    created_at: datetime = field(init=False)  # Automatically set in __post_init__
    filters: Optional[List[str]] = None

    def __post_init__(self):
        """
        Automatically sets the created_at timestamp and validates the title.
        """
        # Set the created_at timestamp to the current time
        self.created_at = datetime.now()

        # Validate that the title is not empty
        if not self.title.strip():
            raise ValueError("The title of the report cannot be empty.")

        # Initialize filters as an empty list if None is provided
        if self.filters is None:
            self.filters = []

        # Log the initialization for debugging purposes
        print(
            f"Report '{self.title}' created by {self.created_by} at {self.created_at}."
        )


if __name__ == "__main__":
    # Create a new report
    try:
        created_by = random.choice(user_list)
        report = Report(
            title="Monthly Sales Report",
            created_by=(
                created_by
                if created_by is not None
                else Report.__dataclass_fields__["created_by"].default_factory()
            ),
        )
        print(report)

        # Add filters to the report
        report.filters.append("Region: North America")
        report.filters.append("Date: Last 30 Days")
        print(f"Updated filters: {report.filters}")
    except ValueError as e:
        print(f"Error: {e}")
