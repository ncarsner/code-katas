import os
from typing import List, Optional

import win32com.client

# import win32com.client.dynamic
# import win32com.client.gencache
# import win32com.client.constants

"""
This module provides functions to create Excel reports, send emails via Outlook, and list files in a folder using the pywin32 library.
"""


def create_excel_report(data: List[List[str]], file_path: str) -> None:
    """
    Create an Excel file and write data to it using pywin32.

    Args:
        data: 2D list of rows and columns to write to Excel.
        file_path: Path to save the Excel file.

    Raises:
        Exception: If Excel automation fails.

    Example:
        create_excel_report([["Name", "Sales"], ["Alex", 100]], "C:/Reports/sales.xlsx")
    """
    excel = win32com.client.Dispatch("Excel.Application")
    excel.Visible = False  # Set to True for debugging
    try:
        wb = excel.Workbooks.Add()
        ws = wb.Worksheets(1)
        for row_idx, row in enumerate(data, 1):
            for col_idx, value in enumerate(row, 1):
                ws.Cells(row_idx, col_idx).Value = value
        wb.SaveAs(file_path)
        wb.Close()
    except Exception as e:
        raise Exception(f"Excel automation failed: {e}")
    finally:
        excel.Quit()


def send_outlook_email(
    subject: str, body: str, to: List[str], attachments: Optional[List[str]] = None
) -> None:
    """
    Send an email via Outlook using pywin32.

    Args:
        subject: Email subject.
        body: Email body (plain text).
        to: List of recipient email addresses.
        attachments: Optional list of file paths to attach.

    Raises:
        Exception: If Outlook automation fails.

    Example:
        send_outlook_email(
            subject="Monthly Report",
            body="Please find attached.",
            to=["user@example.com"],
            attachments=["C:/Reports/sales.xlsx"]
        )
    """
    outlook = win32com.client.Dispatch("Outlook.Application")
    try:
        mail = outlook.CreateItem(0)  # 0: olMailItem
        mail.Subject = subject
        mail.Body = body
        mail.To = ";".join(to)
        if attachments:
            for file in attachments:
                if os.path.exists(file):
                    mail.Attachments.Add(file)
                else:
                    print(f"Attachment not found: {file}")
        mail.Send()
    except Exception as e:
        raise Exception(f"Outlook automation failed: {e}")


def list_files_in_folder(folder_path: str, file_extension: Optional[str] = None) -> List[str]:
    """
    List files in a folder using Windows Scripting Host via pywin32.

    Args:
        folder_path: Path to the folder.
        file_extension: Optional file extension filter (e.g., '.xlsx').

    Returns:
        List of file paths.

    Example:
        files = list_files_in_folder("C:/Reports", ".xlsx")
    """
    shell = win32com.client.Dispatch("Scripting.FileSystemObject")
    files = []
    try:
        folder = shell.GetFolder(folder_path)
        for file in folder.Files:
            if not file_extension or file.Name.lower().endswith(file_extension.lower()):
                files.append(file.Path)
    except Exception as e:
        raise Exception(f"File system automation failed: {e}")
    return files


if __name__ == "__main__":
    # 1. Create an Excel report
    data = [["Employee", "Sales"], ["Alex", 1200], ["Blake", 950]]
    excel_path = os.path.abspath("sales_report.xlsx")
    create_excel_report(data, excel_path)
    print(f"Excel report created at {excel_path}")

    # 2. Send an Outlook email with the report attached
    send_outlook_email(
        subject="Weekly Sales Report",
        body="Please find the attached sales report.",
        to=["recipient@example.com"],
        attachments=[excel_path],
    )
    print("Outlook email sent.")

    # 3. List all Excel files in the current directory
    excel_files = list_files_in_folder(os.getcwd(), ".xlsx")
    print("Excel files in current directory:", excel_files)

"""
Troubleshooting Tips:
- Ensure Excel and Outlook are installed and configured on your machine.
- Run Python as the same user that has access to Office applications.
- If you get permission errors, try running your script as Administrator.
- For debugging, set excel.Visible = True to see Excel operations.
- pywin32 may require 32-bit Python if Office is 32-bit.
"""
