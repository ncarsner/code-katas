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

    @abstractmethod
    def perform_task(self) -> str:
        """
        Abstract method to be implemented by subclasses to define specific tasks performed by the employee.
        """
        pass


class Manager(Employee):
    def job_description(self) -> str:
        return "Oversees team operations and manages projects."

    def perform_task(self) -> str:
        return "Conducting team meetings and setting project goals."


class ProjectManager(Employee):
    def job_description(self) -> str:
        return "Plans, executes, and closes projects."

    def perform_task(self) -> str:
        return "Creating project timelines and assigning tasks."


class ProductOwner(Employee):
    def job_description(self) -> str:
        return "Defines product vision and prioritizes product backlog."

    def perform_task(self) -> str:
        return "Prioritizing backlog items and communicating with stakeholders."


class BusinessAnalyst(Employee):
    def job_description(self) -> str:
        return "Analyzes business needs and documents requirements."

    def perform_task(self) -> str:
        return "Gathering requirements and preparing documentation."


class Developer(Employee):
    def job_description(self) -> str:
        return "Writes and maintains code for applications."

    def perform_task(self) -> str:
        return "Writing code and fixing bugs."


class Designer(Employee):
    def job_description(self) -> str:
        return "Creates visual designs and user interfaces."

    def perform_task(self) -> str:
        return "Designing wireframes and creating prototypes."


class QAEngineer(Employee):
    def job_description(self) -> str:
        return "Tests software to ensure quality and functionality."

    def perform_task(self) -> str:
        return "Writing test cases and performing regression testing."


class BusinessEntity(Employee):
    def job_description(self) -> str:
        return "Conducts user acceptance testing and provides feedback."

    def perform_task(self) -> str:
        return "Reviewing application functionality and providing feedback."


def employee_responsibilities(employees: List[Employee]) -> None:
    """Function calling the job_description method on a list of employees.

    :param employees: List of Employee objects
    """
    for employee in employees:
        print(
            f"{employee.__class__.__name__} is responsible for: {employee.job_description()}"
        )


def employee_tasks(employees: List[Employee]) -> None:
    """Function calling the perform_task method on a list of employees.

    :param employees: List of Employee objects
    """
    print()
    for employee in employees:
        print(
            f"{employee.__class__.__name__} performs tasks like: {employee.perform_task()}"
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

    employee_tasks(employees)
