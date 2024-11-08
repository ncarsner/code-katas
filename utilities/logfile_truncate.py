import re


def process_log_file(input_file, output_file):
    with open(input_file, "r") as file:
        lines = file.readlines()

    cycle_start_pattern = re.compile(r"INFO: \*\*\* Program beginning \*\*\*")
    ticket_pattern = re.compile(r"\d{4}.*MERGE.*;")

    new_lines = []
    in_cycle = False
    cycle_tickets = []
    analysis = []

    for line in lines:
        if cycle_start_pattern.search(line):
            if cycle_tickets:
                new_lines.extend(cycle_tickets[:1])  # Add first ticket
                new_lines.extend(cycle_tickets[-1:])  # Add last ticket
                analysis.append(
                    {
                        "cycle_start": cycle_start_time,
                        "ticket_count": len(cycle_tickets),
                        "first_ticket_time": cycle_tickets[0][:19],  # Extract timestamp
                        "last_ticket_time": cycle_tickets[-1][:19],
                    }
                )
            cycle_tickets = []
            in_cycle = True
            cycle_start_time = line[:19]  # Extract timestamp
            new_lines.append(line)
        elif ticket_pattern.match(line):
            if in_cycle:
                cycle_tickets.append(line)
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)

    if cycle_tickets:
        new_lines.extend(cycle_tickets[:1])  # Add first ticket
        new_lines.extend(cycle_tickets[-1:])  # Add last ticket
        analysis.append(
            {
                "cycle_start": cycle_start_time,
                "ticket_count": len(cycle_tickets),
                "first_ticket_time": cycle_tickets[0][:19],  # Extract timestamp
                "last_ticket_time": cycle_tickets[-1][:19],
            }
        )

    with open(output_file, "w") as file:
        file.writelines(new_lines)

    return analysis


def output_analysis(analysis, analysis_file):
    with open(analysis_file, "w") as file:
        file.write("Cycle Start, Ticket Count, First Ticket Time, Last Ticket Time\n")
        for entry in analysis:
            file.write(
                f"{entry['cycle_start']}, {entry['ticket_count']}, {entry['first_ticket_time']}, {entry['last_ticket_time']}\n"
            )


# Example usage
input_file = r"C:\Users\myUser\Documents\logFile.txt"
output_file = r"C:\Users\myUser\Documents\logFile_converted.txt"
analysis_file = r"C:\Users\myUser\Documents\logFile_analysis.csv"
process_log_file(input_file, output_file)


analysis = process_log_file(input_file, output_file)
output_analysis(analysis, analysis_file)
