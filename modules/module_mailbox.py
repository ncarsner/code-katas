import mailbox
from typing import List, Dict, Any, Optional

"""
Practical usage of Python's built-in `mailbox` module includes reading, searching, and extracting data from mailbox file (e.g., mbox format).

Requirements:
    - Python 3.x
    - A mailbox file in mbox format (e.g., 'sample.mbox')

References:
    - https://docs.python.org/3/library/mailbox.html
"""


def list_mailbox_subjects(mbox_path: str) -> List[str]:
    """
    List the subject lines of all messages in the given mbox file.

    Args:
        mbox_path (str): Path to the mbox file.

    Returns:
        List[str]: List of subject lines.

    Raises:
        FileNotFoundError: If the mbox file does not exist.
    """
    subjects = []
    try:
        mbox = mailbox.mbox(mbox_path)
        try:
            for message in mbox:
                subjects.append(message.get("subject", "(No Subject)"))
        finally:
            mbox.close()
    except FileNotFoundError:
        raise
    return subjects


def search_mailbox_by_sender(mbox_path: str, sender_email: str) -> List[Dict[str, Any]]:
    """
    Search for messages from a specific sender.

    Args:
        mbox_path (str): Path to the mbox file.
        sender_email (str): Email address of the sender to search for.

    Returns:
        List[Dict[str, Any]]: List of dictionaries with message metadata.

    Example:
        >>> search_mailbox_by_sender('sample.mbox', 'john.doe@example.com')
    """
    results = []
    mbox = mailbox.mbox(mbox_path)
    try:
        for message in mbox:
            if message.get("from", "").lower() == sender_email.lower():
                results.append(
                    {
                        "subject": message.get("subject", "(No Subject)"),
                        "date": message.get("date", ""),
                        "from": message.get("from", ""),
                        "to": message.get("to", ""),
                    }
                )
    finally:
        mbox.close()
    return results


def extract_message_bodies(mbox_path: str, limit: Optional[int] = None) -> List[str]:
    """
    Extract plain text bodies from messages in the mbox file.

    Args:
        mbox_path (str): Path to the mbox file.
        limit (Optional[int]): Maximum number of messages to extract.

    Returns:
        List[str]: List of message bodies.

    Note:
        This function extracts only the plain text part of each message.
    """
    bodies = []
    mbox = mailbox.mbox(mbox_path)
    try:
        for i, message in enumerate(mbox):
            if limit is not None and i >= limit:
                break
            if message.is_multipart():
                for part in message.walk():
                    if part.get_content_type() == "text/plain":
                        payload = part.get_payload(decode=True)
                        if isinstance(payload, bytes):
                            bodies.append(
                                payload.decode(
                                    part.get_content_charset("utf-8"), errors="replace"
                                )
                            )
                        else:
                            bodies.append(payload)
                        break
            else:
                payload = message.get_payload(decode=True)
                if isinstance(payload, bytes):
                    bodies.append(
                        payload.decode(
                            message.get_content_charset("utf-8"), errors="replace"
                        )
                    )
                else:
                    bodies.append(payload)
    finally:
        mbox.close()
    return bodies


def count_messages(mbox_path: str) -> int:
    """
    Count the number of messages in the mbox file.

    Args:
        mbox_path (str): Path to the mbox file.

    mbox = mailbox.mbox(mbox_path)
    try:
        return len(mbox)
    finally:
        mbox.close()
    """
    mbox = mailbox.mbox(mbox_path)
    try:
        return len(mbox)
    finally:
        mbox.close()


if __name__ == "__main__":
    mbox_file = "sample.mbox"  # Replace with your mbox file path

    # List all subjects
    try:
        subjects = list_mailbox_subjects(mbox_file)
        print(f"Subjects in mailbox ({len(subjects)} messages):")
        for subj in subjects:
            print(f"  - {subj}")
    except FileNotFoundError:
        print(f"Mailbox file '{mbox_file}' not found.")

    # Search for messages from a specific sender
    sender = "john.doe@example.com"
    messages = search_mailbox_by_sender(mbox_file, sender)
    print(f"\nMessages from {sender}: {len(messages)} found.")
    for msg in messages:
        print(f"  - Subject: {msg['subject']} | Date: {msg['date']}")

    # Extract message bodies (limit to 5 for demo)
    bodies = extract_message_bodies(mbox_file, limit=5)
    print("\nFirst 5 message bodies:")
    for i, body in enumerate(bodies, 1):
        print(f"--- Message {i} ---\n{body[:200]}...\n")

    # Count messages
    total = count_messages(mbox_file)
    print(f"Total messages in mailbox: {total}")

"""
Troubleshooting Tips:
- Ensure the mbox file exists and is accessible.
- For large mailboxes, consider processing messages in batches.
- Use try/except blocks to handle corrupt or malformed messages.
- For advanced filtering, extend the search functions with more criteria.
"""
