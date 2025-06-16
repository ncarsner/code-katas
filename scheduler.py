import random

from ortools.sat.python import cp_model

def main():
    # Staff names
    staff = ['Alex', 'Blake', 'Chris', 'Cameron', 'Dylan', 'Elliott', 'Hunter']
    random.shuffle(staff)  # Shuffle staff names for randomness
    num_staff = len(staff)
    num_days = 5

    # Create the model
    model = cp_model.CpModel()

    # Create variables
    schedule = {}
    for s in range(num_staff):
        for d in range(num_days):
            schedule[(s, d)] = model.NewBoolVar(f'schedule_{s}_{d}')

    # Each person works remotely exactly 2 days per week
    for s in range(num_staff):
        model.Add(sum(schedule[(s, d)] for d in range(num_days)) == 2)

    # No consecutive remote days
    for s in range(num_staff):
        for d in range(num_days - 1):
            model.Add(schedule[(s, d)] + schedule[(s, d + 1)] <= 1)
    # No remote on Friday and Monday
    for s in range(num_staff):
        model.Add(schedule[(s, 4)] + schedule[(s, 0)] <= 1)

    # Create the solver and solve
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    # Display the results in an easy-to-read table
    print(f'Solver status: {status}')
    if status == cp_model.FEASIBLE or status == cp_model.OPTIMAL:
        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
        col_width = len(days[0])  # width for each day column (" R " or " O ")
        staff_col_width = 7
        staff_col_width = max(staff_col_width, max(len(name) for name in staff)) + 1
        header = f'{"Staff":<{staff_col_width}}| ' + ' | '.join(f'{d:^{col_width}}' for d in days) + ' |'
        print('\n' + header)
        print('-' * len(header))
        for s in range(num_staff):
            row = f'{staff[s]:<{staff_col_width}}| '
            for d in range(num_days):
                cell = ' R ' if solver.Value(schedule[(s, d)]) == 1 else ' O '
                row += cell + ' | '
            print(row)
        print("\nLegend: R = Remote, O = Onsite")
    else:
        print('No solution found.')
        print(f'Solver status: {status}')

if __name__ == '__main__':
    main()