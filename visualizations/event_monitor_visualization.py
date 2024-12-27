from datetime import datetime, timedelta
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


class Event:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time


# Sample data generation
def generate_sample_data():
    data = {"x": [], "y": []}

    now = datetime.now()
    today = now.date()

    def random_time_span():
        start_hour = random.randint(0, 23)
        start_minute = random.randint(0, 59)
        duration_minutes = random.randint(30, 270)
        end_hour = (start_hour + (start_minute + duration_minutes) // 60) % 24
        end_minute = (start_minute + duration_minutes) % 60
        start_time = f"{start_hour:02}:{start_minute:02}"
        end_time = f"{end_hour:02}:{end_minute:02}"
        return start_time, end_time

    # Define specific events for X (GREY)
    x_events = [
        # (today + timedelta(days=(1 - today.weekday() + 1) % 7), *random_time_span()),  # Next Tuesday
        # (today + timedelta(days=(3 - today.weekday() + 1) % 7), *random_time_span()),  # Next Thursday
        # (today + timedelta(days=(5 - today.weekday() + 1) % 7), *random_time_span()),  # Next Saturday
        (datetime(2024, 9, 28), "15:13", "18:41"),
        (datetime(2024, 9, 29), "8:52", "12:28"),
        (datetime(2024, 10, 1), "8:56", "18:05"),
        (datetime(2024, 10, 3), "11:40", "13:05"),
        (datetime(2024, 10, 4), "9:57", "16:26"),
        (datetime(2024, 10, 6), "9:28", "14:09"),
        (datetime(2024, 10, 10), "13:49", "18:12"),
        (datetime(2024, 10, 22), "8:42", "16:21"),
        (datetime(2024, 10, 23), "12:01", "12:11"),
        (datetime(2024, 10, 24), "9:58", "14:09"),
        (datetime(2024, 10, 25), "9:38", "17:45"),

        (datetime(2024, 11, 10), "11:36", "12:14"),

        (datetime(2024, 12, 13), "10:00", "15:37"),
        (datetime(2024, 12, 15), "8:40", "12:11"),
        (datetime(2024, 12, 20), "9:41", "14:29"),

    ]

    # Define specific events for Y (PURPLE)
    y_events = [
        # (today + timedelta(days=(0 - today.weekday() + 1) % 7), *random_time_span()),  # Next Monday
        # (today + timedelta(days=(4 - today.weekday() + 1) % 7), *random_time_span())   # Next Friday
        (datetime(2024, 9, 28), "16:43", "23:59"), # default midnight
        (datetime(2024, 9, 30), "15:19", "15:55"),
        (datetime(2024, 9, 30), "18:29", "23:59"),
        (datetime(2024, 10, 1), "7:02", "12:25"),
        (datetime(2024, 10, 1), "13:30", "17:58"),
        (datetime(2024, 10, 1), "18:23", "23:59"),
        (datetime(2024, 10, 2), "7:26", "15:37"),
        (datetime(2024, 10, 2), "18:30", "23:59"),
        (datetime(2024, 10, 3), "14:09", "14:32"),
        (datetime(2024, 10, 3), "17:58", "23:59"),
        (datetime(2024, 10, 4), "18:28", "23:59"),
        (datetime(2024, 10, 5), "13:57", "14:34"),
        (datetime(2024, 10, 9), "12:11", "12:33"),
        (datetime(2024, 10, 9), "16:09", "16:23"),
        (datetime(2024, 10, 10), "10:09", "11:46"),
        (datetime(2024, 10, 22), "8:51", "15:31"),
        (datetime(2024, 10, 22), "16:03", "16:30"),
        (datetime(2024, 10, 25), "12:23", "13:42"),

        (datetime(2024, 11, 15), "14:27", "15:06"),
        (datetime(2024, 11, 28), "11:12", "11:46"),

        (datetime(2024, 12, 13), "11:26", "12:40"),
        (datetime(2024, 12, 14), "9:29", "9:58"),
        (datetime(2024, 12, 14), "10:30", "13:18"),

        (datetime(2024, 12, 17), "6:40", "16:02"),
        (datetime(2024, 12, 18), "7:57", "11:54"),
        (datetime(2024, 12, 18), "14:47", "16:21"),
        (datetime(2024, 12, 19), "7:15", "15:46"),

    ]

    # Helper function to create datetime objects for events
    def create_event(date, start_time, end_time):
        start_dt = datetime.combine(date, datetime.strptime(start_time, "%H:%M").time())
        end_dt = datetime.combine(date, datetime.strptime(end_time, "%H:%M").time())
        return Event(start_dt, end_dt)

    # Generate events for X
    for date, start, end in x_events:
        data["x"].append(create_event(date, start, end))

    # Generate events for Y
    for date, start, end in y_events:
        data["y"].append(create_event(date, start, end))

    return data


# Visualization function
def visualize_event_occurrences(
    data, show_vertical_gridlines=True, show_horizontal_gridlines=True):
    fig, ax = plt.subplots(figsize=(10, 5))

    alpha = 1.0

    # Plot x events
    for event in data["x"]:
        ax.plot(
            [event.start_time, event.start_time],
            [event.start_time.hour, event.end_time.hour],
            color="grey",
            alpha=alpha,
        )
        ax.scatter(
            [event.start_time, event.start_time],
            [event.start_time.hour, event.end_time.hour],
            color="grey",
            alpha=alpha,
        )

    # Add background shading for weekends
    start_date = min(event.start_time for event in data["x"] + data["y"]).date()
    end_date = max(event.start_time for event in data["x"] + data["y"]).date()

    current_date = start_date
    while current_date <= end_date:
        if current_date.weekday() >= 5:
            ax.axvspan(current_date, current_date + timedelta(days=1), color='lightgrey', alpha=0.5)
        current_date += timedelta(days=1)

    # Plot y events
    for event in data["y"]:
        ax.plot(
            [event.start_time, event.start_time],
            [event.start_time.hour, event.end_time.hour],
            color="purple",
            alpha=alpha,
        )
        ax.scatter(
            [event.start_time, event.start_time],
            [event.start_time.hour, event.end_time.hour],
            color="purple",
            alpha=alpha,
        )

    # Formatting the plot
    ax.plot([], [], color="grey", alpha=alpha, label="RAV4")
    ax.plot([], [], color="purple", alpha=alpha, label="Pathfinder")
    ax.legend(loc="upper right")
    ax.xaxis.set_major_locator(mdates.DayLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
    ax.set_xlabel("Date")
    ax.set_ylabel("Hour of Day")
    ax.set_title("Event Occurrences")
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Set Y-axis to 24-hour span in 3-hour increments
    ax.set_yticks(range(0, 27, 3))
    ax.set_yticklabels([f"{i:2}:00" for i in range(0, 27, 3)])

    # Reverse the Y-axis
    ax.invert_yaxis()

    # Set gridlines visibility
    ax.grid(which="both", axis="x", visible=show_vertical_gridlines)
    ax.grid(which="both", axis="y", visible=show_horizontal_gridlines)

    plt.show()


# Main execution
if __name__ == "__main__":
    data = generate_sample_data()

    # Adjust the script to plot only the last N days' activity
    days_to_plot = 14  # Adjustable variable for the number of days to plot

    # Filter events to include only those within the last N days
    end_date = max(event.start_time for event in data["x"] + data["y"]).date()
    start_date = end_date - timedelta(days=days_to_plot)

    data["x"] = [event for event in data["x"] if start_date <= event.start_time.date() <= end_date]
    data["y"] = [event for event in data["y"] if start_date <= event.start_time.date() <= end_date]

    # Visualize the filtered events
    visualize_event_occurrences(data, show_vertical_gridlines=False, show_horizontal_gridlines=True)
