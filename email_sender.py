import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import configparser

# Load configuration from config.ini
config = configparser.ConfigParser()
config.read("config.ini")

# Email details
smtp_server = config["email"]["smtp_server"]
smtp_user = config["email"]["smtp_user"]
sender_name = config["email"]["sender_name"]
to_recipients = config["email"]["to_recipients"].split(",")
cc_recipients = config["email"]["cc_recipients"].split(",")


def send_email(
    subject,
    body,
    smtp_server=smtp_server,
    smtp_user=smtp_user,
    sender_name=sender_name,
    to_emails=to_recipients,
    cc_emails=cc_recipients,
):
    msg = MIMEMultipart()
    msg["From"] = f"{sender_name} <{smtp_user}>"
    msg["To"] = ", ".join(to_emails)
    msg["Cc"] = ", ".join(cc_emails)
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP(smtp_server)
        server.starttls()
        text = msg.as_string()
        server.sendmail(smtp_user, to_recipients + cc_recipients, text)
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")


# send_email("Test Subject line", "No body content in this message.")