import copyreg
import pickle
from typing import Any, Tuple

"""
Python's built-in `copyreg` is useful in customizing how objects are pickled (serialized) and unpickled (deserialized) in operations such as caching, distributed processing, or saving analysis state.

Below are examples showing:
- How to register custom pickling functions for a user-defined class.
- How to troubleshoot and extend pickling for classes that are not natively serializable.
"""


class Report:
    """
    Example business intelligence class representing a report.
    """

    def __init__(self, name: str, data: dict[str, Any]) -> None:
        self.name = name
        self.data = data

    def __repr__(self) -> str:
        return f"Report(name={self.name!r}, data={self.data!r})"


def pickle_report(report: Report) -> Tuple[Any, ...]:
    """
    Custom pickling function for Report objects.

    Returns a tuple: (callable, args) so that
    callable(*args) reconstructs the object.
    """
    # Troubleshooting: Ensure all attributes are serializable.
    # If not, convert them to serializable types here.
    return unpickle_report, (report.name, report.data)


def unpickle_report(name: str, data: dict[str, Any]) -> Report:
    """
    Custom unpickling function for Report objects.
    """
    return Report(name, data)


# Register the custom pickling functions for the Report class.
copyreg.pickle(Report, pickle_report)


if __name__ == "__main__":
    # Create a Report instance
    report = Report("Sales Q1", {"region": "North", "total": 12345})

    # Serialize (pickle) the report
    pickled_report = pickle.dumps(report)
    print("Pickled Report (bytes):", pickled_report)

    # Deserialize (unpickle) the report
    loaded_report = pickle.loads(pickled_report)
    print("Unpickled Report:", loaded_report)

    # Efficient use: You can now pickle/unpickle Report objects in multiprocessing,
    # caching, or distributed systems without errors.

    # Troubleshooting tip:
    # If you get a pickling error for a custom class, define and register
    # custom pickling functions as above.

"""
Summary:
- Use copyreg.pickle(cls, pickle_func) to register custom pickling logic.
- Your pickle_func should return (unpickle_func, args).
- This is scalable for any custom class you need to serialize for BI workflows.
"""
