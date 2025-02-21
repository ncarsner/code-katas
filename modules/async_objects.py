import asyncio
import random
from string import ascii_letters as lets


async def random_call(task_id: int, queue: asyncio.Queue):
    """
    Asynchronously generates a random string of characters, sleeps for a random duration,
    and processes a secondary function based on the string's ordinal value sum.

    :param task_id: The task number for tracking execution order.
    :param queue: An async queue to store results in order.
    """
    # Generate a random string of length between 5 and 10
    random_string = "".join(random.choice(lets) for _ in range(random.randint(5, 10)))

    # Sleep for a random duration between 2 and 5 seconds
    sleep_duration = random.uniform(2, 5)

    print(f"Task {task_id:02d} ({random_string}): Sleep: {sleep_duration:.2f} seconds.")

    # Sleep asynchronously
    await asyncio.sleep(sleep_duration)

    # Process the secondary function
    result = await process_secondary(task_id, random_string, sleep_duration)

    # Store result in queue to maintain order
    await queue.put(result)


async def process_secondary(task_id: int, random_string: str, sleep_duration: float):
    """
    Processes a secondary function that evaluates the ordinal sum of the random string
    relative to the sleep duration.

    :param task_id: The task number for tracking execution order.
    :param random_string: The generated string from rando_call.
    :param sleep_duration: The time (in seconds) the program slept.
    """
    # Compute the sum of ordinal values of the characters
    ordinal_sum = sum(ord(char) for char in random_string)

    # Compare ordinal sum with sleep duration (converted to milliseconds)
    sleep_ms = sleep_duration * 1000
    comparison = ">" if ordinal_sum > sleep_ms else "<="

    return f"Task {task_id:02d} ({random_string}): Ordinal sum = {ordinal_sum} {comparison} Sleep: ({sleep_ms:.1f} ms)."


async def main():
    """
    Main asynchronous function: initiate 10 parallel processes of and maintain ordered output.
    """
    queue = asyncio.Queue()
    tasks = [random_call(i + 1, queue) for i in range(10)]

    # Gather all tasks and wait for completion
    await asyncio.gather(*tasks)

    # Print results in the order tasks were assigned
    print()
    while not queue.empty():
        print(await queue.get())


# Run the async event loop
if __name__ == "__main__":
    asyncio.run(main())
