from ortools.sat.python import cp_model

def main():
    # Staff names
    staff = ['Alex', 'Blake', 'Chris', 'Dylan', 'Elliott',]
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

    # Display the results
    print(f'Solver status: {status}')  # Add this line to print the solver status
    if status == cp_model.FEASIBLE or status == cp_model.OPTIMAL:
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        print('Schedule:')
        print('         ' + '  '.join(days))
        print('         ' + '  '.join(['---'] * num_days))
        for s in range(num_staff):
            print(f'{staff[s]}: ', end='')
            for d in range(num_days):
                if solver.Value(schedule[(s, d)]) == 1:
                    print('R', end=' ')
                else:
                    print('O', end=' ')
            print()
    else:
        print('No solution found.')
        print(f'Solver status: {status}')

if __name__ == '__main__':
    main()