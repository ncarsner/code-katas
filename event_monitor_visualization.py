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
    data = {'x': [], 'y': []}
    
    now = datetime.now()
    today = now.date()
    
    # Define specific events for X (On Prem Server offline)
    def random_time_span():
        start_hour = random.randint(0, 23)
        start_minute = random.randint(0, 59)
        duration_minutes = random.randint(30, 270)
        end_hour = (start_hour + (start_minute + duration_minutes) // 60) % 24
        end_minute = (start_minute + duration_minutes) % 60
        start_time = f"{start_hour:02}:{start_minute:02}"
        end_time = f"{end_hour:02}:{end_minute:02}"
        return start_time, end_time

    x_events = [
        (today + timedelta(days=(1 - today.weekday() + 1) % 7), *random_time_span()),  # Next Tuesday
        (today + timedelta(days=(1 - today.weekday() + 1) % 7), *random_time_span()),  # Next Tuesday
        (today + timedelta(days=(3 - today.weekday() + 1) % 7), *random_time_span()),  # Next Thursday
        (today + timedelta(days=(3 - today.weekday() + 1) % 7), *random_time_span()),  # Next Thursday
        (today + timedelta(days=(5 - today.weekday() + 1) % 7), *random_time_span()),  # Next Saturday
        (today + timedelta(days=(5 - today.weekday() + 1) % 7), *random_time_span())   # Next Saturday
    ]
    
    # Define specific events for Y (Cloud Server offline)
    y_events = [
        (today + timedelta(days=(0 - today.weekday() + 1) % 7), *random_time_span()),  # Next Monday
        (today + timedelta(days=(0 - today.weekday() + 1) % 7), *random_time_span()),  # Next Monday
        (today + timedelta(days=(4 - today.weekday() + 1) % 7), *random_time_span()),  # Next Friday
        (today + timedelta(days=(4 - today.weekday() + 1) % 7), *random_time_span())   # Next Friday
    ]
    
    # Helper function to create datetime objects for events
    def create_event(date, start_time, end_time):
        start_dt = datetime.combine(date, datetime.strptime(start_time, "%H:%M").time())
        end_dt = datetime.combine(date, datetime.strptime(end_time, "%H:%M").time())
        return Event(start_dt, end_dt)
    
    # Generate events for X
    for date, start, end in x_events:
        data['x'].append(create_event(date, start, end))
    
    # Generate events for Y
    for date, start, end in y_events:
        data['y'].append(create_event(date, start, end))
    
    return data

# Visualization function
def visualize_event_occurrences(data):
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot x events
    for event in data['x']:
        ax.plot([event.start_time, event.end_time], [event.start_time.hour, event.end_time.hour], color='blue', alpha=0.6)
        ax.scatter([event.start_time, event.end_time], [event.start_time.hour, event.end_time.hour], color='blue', alpha=0.6)

    # Plot y events
    for event in data['y']:
        ax.plot([event.start_time, event.end_time], [event.start_time.hour, event.end_time.hour], color='red', alpha=0.6)
        ax.scatter([event.start_time, event.end_time], [event.start_time.hour, event.end_time.hour], color='red', alpha=0.6)

    # Formatting the plot
    ax.xaxis.set_major_locator(mdates.DayLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax.set_xlabel('Date')
    ax.set_ylabel('Hour of Day')
    ax.set_title('Event Occurrences by Hour Block')
    ax.legend(['Event X', 'Event Y'])
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()

    # Reverse the Y-axis
    ax.invert_yaxis()

    plt.show()

# Main execution
if __name__ == "__main__":
    data = generate_sample_data()
    visualize_event_occurrences(data)
