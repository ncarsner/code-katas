import threading
from queue import Queue, PriorityQueue, Empty, Full
from typing import Any, Callable, Tuple

"""
Practical use of Python's built-in `queue` module includes task management, producer-consumer patterns, and thread-safe data processing, using FIFO queues, LIFO stacks, and priority queues to manage tasks and data processing in a BI context.
"""


def task_queue_example(tasks: list[str]) -> None:
    """
    Demonstrates a simple FIFO queue for managing BI data processing tasks.

    Args:
        tasks (list[str]): List of task names to process.

    Usage:
        task_queue_example(['extract', 'transform', 'load'])
    """
    q: Queue[str] = Queue()
    for task in tasks:
        q.put(task)
        print(f"Task '{task}' added to queue.")

    while not q.empty():
        current_task = q.get()
        print(f"Processing task: {current_task}")
        q.task_done()
    print("All tasks processed.\n")


def producer_consumer_example(
    data: list[Any], worker: Callable[[Any], None], num_workers: int = 2
) -> None:
    """
    Demonstrates a producer-consumer pattern using Queue for thread-safe data processing.

    Args:
        data (list[Any]): Data items to process.
        worker (Callable[[Any], None]): Function to process each data item.
        num_workers (int): Number of consumer threads.

    Usage:
        producer_consumer_example([1,2,3], lambda x: print(x*2))
    """
    q: Queue[Any] = Queue()

    def producer():
        for item in data:
            q.put(item)
            print(f"Produced: {item}")
        for _ in range(num_workers):
            q.put(None)  # Sentinel values to signal consumers to exit

    def consumer():
        while True:
            item = q.get()
            if item is None:
                break
            worker(item)
            q.task_done()

    threads = [threading.Thread(target=consumer) for _ in range(num_workers)]
    for t in threads:
        t.start()
    producer()
    q.join()
    for t in threads:
        t.join()
    print("Producer-consumer processing complete.\n")


def priority_queue_example(tasks: list[Tuple[int, str]]) -> None:
    """
    Demonstrates a PriorityQueue for BI task prioritization.

    Args:
        tasks (list[Tuple[int, str]]): List of (priority, task_name) tuples.

    Usage:
        priority_queue_example([(2, 'load'), (1, 'extract'), (3, 'transform')])
    """
    pq: PriorityQueue[Tuple[int, str]] = PriorityQueue()
    for priority, task in tasks:
        pq.put((priority, task))
        print(f"Task '{task}' with priority {priority} added.")

    while not pq.empty():
        priority, task = pq.get()
        print(f"Processing task '{task}' with priority {priority}")
        pq.task_done()
    print("All prioritized tasks processed.\n")


def troubleshooting_queue():
    """
    Shows how to handle common queue exceptions: Empty and Full.
    """
    q: Queue[int] = Queue(maxsize=2)
    try:
        q.put(1, timeout=1)
        q.put(2, timeout=1)
        # This will raise Full after 1 second
        q.put(3, timeout=1)
    except Full:
        print("Queue is full! Cannot add more items.")

    try:
        # Remove all items
        q.get(timeout=1)
        q.get(timeout=1)
        # This will raise Empty after 1 second
        q.get(timeout=1)
    except Empty:
        print("Queue is empty! No items to retrieve.\n")


if __name__ == "__main__":
    # FIFO task queue
    task_queue_example(["extract", "transform", "load"])

    # Producer-consumer with threads
    producer_consumer_example(
        data=[f"record_{i}" for i in range(5)],
        worker=lambda x: print(f"Processed {x}"),
        num_workers=2,
    )

    # Priority queue for task scheduling
    priority_queue_example([(2, "load"), (1, "extract"), (3, "transform")])

    # Troubleshooting queue exceptions
    troubleshooting_queue()
