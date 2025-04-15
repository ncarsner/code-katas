from dataclasses import dataclass, field
from typing import List, Optional
from datetime import date


@dataclass
class Task:
    """
    Represents a task assigned to an employee.
    """
    id: int
    description: str
    due_date: Optional[date]
    completed: bool = False

    def mark_completed(self) -> None:
        """
        Marks the task as completed.
        """
        self.completed = True


@dataclass
class Employee:
    """
    Represents an employee in a business intelligence team.
    """
    id: int
    name: str
    role: str
    start_date: date
    salary: float
    skills: List[str] = field(default_factory=list)
    tasks: List[Task] = field(default_factory=list)

    def add_skill(self, skill: str) -> None:
        """
        Adds a new skill to the employee's skill set.
        """
        if skill not in self.skills:
            self.skills.append(skill)
        else:
            print(f"{self.name} already has the skill: {skill}")

    def assign_task(self, task: Task) -> None:
        """
        Assigns a task to the employee.
        """
        self.tasks.append(task)

    def list_tasks(self) -> None:
        """
        Lists all tasks assigned to the employee.
        """
        print(f"Tasks for {self.name}:")
        for task in self.tasks:
            status = "Completed" if task.completed else "Pending"
            print(f"- {task.description} (Due: {task.due_date}, Status: {status})")


@dataclass
class Project:
    """
    Represents a project in the business intelligence department.
    """
    id: int
    name: str
    start_date: date
    end_date: Optional[date]
    team: List[Employee] = field(default_factory=list)

    def add_employee(self, employee: Employee) -> None:
        """
        Adds an employee to the project team.
        """
        if employee not in self.team:
            self.team.append(employee)
        else:
            print(f"{employee.name} is already part of the project team.")

    def calculate_total_salary(self) -> int:
        """
        Calculates the total salary of all employees in the project team.
        """
        return sum(emp.salary for emp in self.team)


if __name__ == "__main__":
    # Create employees
    emp1 = Employee(
        id=1,
        name="Alex",
        role="Data Analyst",
        start_date=date(2020, 5, 1),
        salary=95_000,
    )
    emp2 = Employee(
        id=2,
        name="Blake",
        role="BI Developer",
        start_date=date(2019, 3, 15),
        salary=110_000,
    )

    # Add skills to employees
    emp1.add_skill("SQL")
    emp1.add_skill("Python")
    emp2.add_skill("ETL")
    emp2.add_skill("Power BI")

    # Assign tasks to employees
    task1 = Task(id=1, description="Prepare monthly sales report", due_date=date(2023, 10, 15))
    task2 = Task(id=2, description="Develop ETL pipeline for new data source", due_date=date(2023, 10, 20))
    emp1.assign_task(task1)
    emp2.assign_task(task2)

    # List tasks for each employee
    emp1.list_tasks()
    emp2.list_tasks()

    # Create a project and add employees
    project = Project(
        id=101, name="Sales Dashboard", start_date=date(2023, 1, 1), end_date=None
    )
    project.add_employee(emp1)
    project.add_employee(emp2)

    # Calculate total salary for the project team
    total_salary = project.calculate_total_salary()
    print(f"Appropriation for project team: ${total_salary:,}")
