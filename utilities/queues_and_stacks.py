from collections import deque
import time
import random


# Stack for urgent tasks (LIFO)
class UrgentTaskStack:
    def __init__(self):
        self.stack = []

    def add_task(self, task):
        self.stack.append(task)

    def get_task(self):
        return self.stack.pop() if self.stack else None

    def is_empty(self):
        return len(self.stack) == 0


# Queue for scheduled daily reports (FIFO)
class DailyReportQueue:
    def __init__(self):
        self.queue = deque()

    def schedule_report(self, report):
        self.queue.append(report)

    def get_next_report(self):
        return self.queue.popleft() if self.queue else None

    def is_empty(self):
        return len(self.queue) == 0


# Simulate business intelligence process
def process_reports_and_tasks():
    urgent_stack = UrgentTaskStack()
    daily_queue = DailyReportQueue()

    # Example daily schedule (could be loaded from config/db)
    daily_schedule = [
        "Sales Report",
        "Inventory Report",
        "Customer Feedback",
        "Website Analytics",
    ]

    # Schedule today's reports
    for report in daily_schedule:
        daily_queue.schedule_report(report)

    # Simulate urgent tasks arriving asynchronously
    urgent_tasks = [
        "Fix Data Pipeline",
        "Update Stakeholder Dashboard",
        "Re-run Failed Report",
    ]
    for task in urgent_tasks:
        if random.choice([True, False]):
            urgent_stack.add_task(task)

    print("Starting business intelligence process...\n")

    while not daily_queue.is_empty() or not urgent_stack.is_empty():
        # Always process urgent tasks first
        if not urgent_stack.is_empty():
            task = urgent_stack.get_task()
            print(f"Processing URGENT task: {task}")
            time.sleep(0.5)  # Simulate processing time
        elif not daily_queue.is_empty():
            report = daily_queue.get_next_report()
            print(f"Processing scheduled report: {report}")
            time.sleep(0.5)  # Simulate processing time

    print("\nAll tasks and reports processed for today.")


if __name__ == "__main__":
    process_reports_and_tasks()
