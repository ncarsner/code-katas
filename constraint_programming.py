from ortools.sat.python import cp_model
# import json
from decorators import log_to_json

"""Discrete optimization problem solutions using constraint programming within Python.
    https://pganalyze.com/blog/a-practical-introduction-to-constraint-programming-using-cp-sat"""

"""Problem Statement:
    Alex, Blake, and Chris each have $20.
    They want to pool their money to purchase a gift worth $50.

Constraints:
    Alex will put in at least as much money as Blake.
        a >= b
    Chris only has $5 bills, so Chris' contribution will be a multiple of that.
        c % 5 == 0
    None want to contribute the exact same amount as any other.
        a != b
        a != c
        b != c
    Objective: How much should each of them contribute?"""

a = b = c = 0
a + b + c == 50
a >= b
c % 5 == 0
a != b
a != c
b != c


"""Problem Statement:
    A store owner needs to create the weekly work schedule for its employees.
    The store is open from 8AM to 8PM every day.
    Each day is divided into three shifts of 4 hours: morning, afternoon, and evening.
    There are two roles in the store: cashier and restocker.

    - Some employees are qualified to do either role, but others can only be a cashier, or a restocker.
    - There has to be a cashier scheduled at all times, but restocking only takes about 4 hours every day.
        Hence, for the restocking task we only need to schedule an employee for a single shift every day.
        This can be any shift, but two restocking shifts cannot be scheduled consecutively.
        If a restocking is scheduled on the evening shift on Tuesday, for example,
            we cannot schedule the Wednesday restocking on the morning shift.
    - An employee that is qualified in both roles can still only be assigned to one role per shift.
    - Employees cannot work more than 8 hours (2 shifts) per day.
        If they do work 2 shifts in a day, they must be consecutive.
"""

model = cp_model.CpModel()

employees = {"Phil": ["Restocker"],
             "Emma": ["Cashier", "Restocker"],
             "David": ["Cashier", "Restocker"],
             "Rebecca": ["Cashier"],
}

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

shifts = ["Morning", "Afternoon", "Evening"]

roles = ["Cashier", "Restocker"]

schedule = {
    e: {
        r: {
            d: {s: model.NewBoolVar(f"schedule_{e}_{r}_{d}_{s}") for s in shifts}
            for d in days
        }
        for r in roles
    }
    for e in employees
}

# Function to print the schedule in a grid-style layout
def print_schedule(schedule):
    header = "Employee".ljust(10) + "Role".ljust(10) + "Day".ljust(10) + "Morning".ljust(10) + "Afternoon".ljust(10) + "Evening".ljust(10)
    print(header)
    print("-" * len(header))
    
    for employee, roles in schedule.items():
        for role, days in roles.items():
            for day, shifts in days.items():
                row = f"{employee}".ljust(10) + f"{role}".ljust(10) + f"{day}".ljust(10)
                for shift in ["Morning", "Afternoon", "Evening"]:
                    row += f"{shifts[shift].Name()}".ljust(10)
                print(row)

print_schedule(schedule)