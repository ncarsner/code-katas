from typing import List, Dict
import csv


class Report:
    """
    A class to represent a business intelligence report.
    This class demonstrates the use of classmethods to create and manage reports.
    """

    def __init__(self, name: str, data: List[Dict[str, float]]):
        """
        Initialize a Report instance.

        :param name: The name of the report.
        :param data: A list of dictionaries containing report data.
        """
        self.name = name
        self.data = data

    @classmethod
    def from_csv(cls, name: str, csv_path: str) -> "Report":
        """
        Create a Report instance from a CSV file.

        :param name: The name of the report.
        :param csv_path: The file path to the CSV file.
        :return: A Report instance.
        """

        data = []
        try:
            with open(csv_path, mode="r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Convert all numeric values to float for consistency
                    data.append(
                        {
                            key: (
                                float(value)
                                if value.replace(".", "", 1).isdigit()
                                else value
                            )
                            for key, value in row.items()
                        }
                    )
        except FileNotFoundError:
            raise FileNotFoundError(f"CSV file not found at path: {csv_path}")
        except Exception as e:
            raise ValueError(f"Error reading CSV file: {e}")

        return cls(name, data)

    @classmethod
    def from_template(cls, name: str, template: str) -> "Report":
        """
        Create a Report instance from a predefined template.

        :param name: The name of the report.
        :param template: The name of the template (e.g., 'sales', 'inventory').
        :return: A Report instance.
        """
        templates = {
            "sales": [{"month": "January", "revenue": 0.0, "expenses": 0.0}],
            "inventory": [{"item": "Sample Item", "quantity": 0, "price": 0.0}],
        }

        if template not in templates:
            raise ValueError(
                f"Template '{template}' not found. Available templates: {list(templates.keys())}"
            )

        return cls(name, templates[template])

    def summarize(self) -> Dict[str, float]:
        """
        Summarize the report data by calculating totals for numeric fields.

        :return: A dictionary containing the summary of numeric fields.
        """
        summary = {}
        for row in self.data:
            for key, value in row.items():
                if isinstance(value, (int, float)):
                    summary[key] = summary.get(key, 0) + value
        return summary

    def display(self) -> None:
        """
        Display the report data in a readable format.
        """
        print(f"Report: {self.name}")
        for row in self.data:
            print(row)


def main():
    # Create a report from a CSV file
    try:
        sales_report = Report.from_csv("Monthly Sales", "sales_data.csv")
        sales_report.display()
        print("Summary:", sales_report.summarize())
    except Exception as e:
        print(f"Error: {e}")

    # Create a report from a predefined template
    inventory_report = Report.from_template("Inventory Report", "inventory")
    inventory_report.display()
    print("Summary:", inventory_report.summarize())


if __name__ == "__main__":
    main()
