from abc import ABC, abstractmethod
from typing import List


class Employee(ABC):
    """Abstract base class representing an employee."""

    @abstractmethod
    def job_description(self) -> str:
        """
        Abstract method to be implemented by subclasses to define the job responsibilities.
        """
        pass


class Manager(Employee):
    def job_description(self) -> str:
        return "Oversees team operations and manages projects."


class ProjectManager(Employee):
    def job_description(self) -> str:
        return "Plans, executes, and closes projects."


class ProductOwner(Employee):
    def job_description(self) -> str:
        return "Defines product vision and prioritizes product backlog."


class BusinessAnalyst(Employee):
    def job_description(self) -> str:
        return "Analyzes business needs and documents requirements."


class Developer(Employee):
    def job_description(self) -> str:
        return "Writes and maintains code for applications."


class Designer(Employee):
    def job_description(self) -> str:
        return "Creates visual designs and user interfaces."


class QAEngineer(Employee):
    def job_description(self) -> str:
        return "Tests software to ensure quality and functionality."


class BusinessEntity(Employee):
    def job_description(self) -> str:
        return "Conducts user acceptance testing and provides feedback."


def employee_responsibilities(employees: List[Employee]) -> None:
    """Function calling the job_description method on a list of employees.

    :param employees: List of Employee objects
    """
    for employee in employees:
        print(
            f"{employee.__class__.__name__} is responsible for: {employee.job_description()}"
        )


if __name__ == "__main__":
    employees: List[Employee] = [
        Manager(),
        ProjectManager(),
        ProductOwner(),
        BusinessAnalyst(),
        Developer(),
        Designer(),
        QAEngineer(),
        BusinessEntity(),
    ]
    employee_responsibilities(employees)
