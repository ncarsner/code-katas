from string import digits
from random import choice


def one_time_passcode(length=6):
    return "".join([choice(digits) for _ in range(length)])


# Initialize the passcode queue constants
QUEUE_SIZE = 20
PASSCODE_LENGTH = 6
REFILL_THRESHOLD = QUEUE_SIZE // 2

# Initialize the passcode queue
passcode_queue = [one_time_passcode(PASSCODE_LENGTH) for _ in range(QUEUE_SIZE)]

if __name__ == "__main__":
    while True:
        print(f"Queue: {passcode_queue}")
        input("\nPress Enter for the next code...\n")

        # Distribute the next passcode
        sent_code = passcode_queue.pop()
        print(f"Sent code: {sent_code}")

        if len(passcode_queue) < REFILL_THRESHOLD:
            print("\nRefilling the passcode queue...")
            while len(passcode_queue) < QUEUE_SIZE:
                # Add new passcodes to the front of the queue
                passcode_queue.insert(0, one_time_passcode(PASSCODE_LENGTH))
