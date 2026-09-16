import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List

"""
Practical use of the built-in `smtplib` module includes methods to automate email notifications. Ensure you have access to an SMTP server (e.g., Gmail, Outlook) before running this code. You may need to adjust security settings on your email account to allow SMTP access, such as "Allow less secure apps" with Gmail or use an app password.
"""


def send_email(
    smtp_server: str,
    port: int,
    sender_email: str,
    sender_password: str,
    recipient_emails: List[str],
    subject: str,
    body: str,
    is_html: bool = False,
) -> None:
    """
    Sends an email using the specified SMTP server.

    Args:
        smtp_server (str): The SMTP server address (e.g., 'smtp.gmail.com').
        port (int): The port to use (e.g., 587 for TLS).
        sender_email (str): The sender's email address.
        sender_password (str): The sender's email password or app password.
        recipient_emails (List[str]): A list of recipient email addresses.
        subject (str): The subject of the email.
        body (str): The body of the email.
        is_html (bool): Whether the email body is in HTML format. Defaults to False.

    Raises:
        Exception: If there is an error during the email sending process.
    """
    try:
        # Create the email message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = ", ".join(recipient_emails)
        message["Subject"] = subject

        # Attach the email body
        if is_html:
            message.attach(MIMEText(body, "html"))
        else:
            message.attach(MIMEText(body, "plain"))

        # Connect to the SMTP server
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()  # Upgrade the connection to secure TLS
            server.login(sender_email, sender_password)  # Log in to the SMTP server
            server.sendmail(
                sender_email, recipient_emails, message.as_string()
            )  # Send the email

        print(f"Email successfully sent to {', '.join(recipient_emails)}.")

    except Exception as e:
        print(f"Failed to send email: {e}")
        raise


if __name__ == "__main__":
    # SMTP server configuration
    SMTP_SERVER = "smtp.gmail.com"
    PORT = 587

    # Sender credentials
    SENDER_EMAIL = "your_email@gmail.com"
    SENDER_PASSWORD = "your_password"  # Use an app password for Gmail

    # Email details
    RECIPIENT_EMAILS = ["recipient1@example.com", "recipient2@example.com"]
    SUBJECT = "Monthly Sales Report"
    BODY = """
    <h1>Monthly Sales Report</h1>
    <p>Dear Team,</p>
    <p>Please find attached the sales report for this month.</p>
    <p>Best regards,<br>Business Intelligence Team</p>
    """
    IS_HTML = True

    # Send the email
    send_email(
        smtp_server=SMTP_SERVER,
        port=PORT,
        sender_email=SENDER_EMAIL,
        sender_password=SENDER_PASSWORD,
        recipient_emails=RECIPIENT_EMAILS,
        subject=SUBJECT,
        body=BODY,
        is_html=IS_HTML,
    )
