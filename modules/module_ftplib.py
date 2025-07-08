from ftplib import FTP, error_perm
from typing import List

"""
This module provides a simple client wrapper for common FTP operations such as listing files, downloading, uploading, deleting files, and managing directories.
"""


class FTPClient:
    """
    A simple FTP client wrapper for common FTP operations.
    """

    def __init__(
        self, host: str, username: str, password: str, port: int = 21, timeout: int = 30
    ) -> None:
        """
        Initialize and connect to the FTP server.

        Args:
            host (str): FTP server address.
            username (str): FTP username.
            password (str): FTP password.
            port (int, optional): FTP port. Defaults to 21.
            timeout (int, optional): Connection timeout in seconds. Defaults to 30.
        """
        self.ftp = FTP()
        self.ftp.connect(host, port, timeout)
        self.ftp.login(user=username, passwd=password)
        print(f"Connected to FTP server: {host}")

    def list_files(self, path: str = ".") -> List[str]:
        """
        List files and directories in the given path.

        Args:
            path (str, optional): Directory path. Defaults to current directory.

        Returns:
            List[str]: List of file and directory names.
        """
        files = self.ftp.nlst(path)
        print(f"Files in '{path}': {files}")
        return files

    def download_file(self, remote_path: str, local_path: str) -> None:
        """
        Download a file from the FTP server.

        Args:
            remote_path (str): Path to the file on the FTP server.
            local_path (str): Local path to save the file.
        """
        with open(local_path, "wb") as f:
            self.ftp.retrbinary(f"RETR {remote_path}", f.write)
        print(f"Downloaded '{remote_path}' to '{local_path}'")

    def upload_file(self, local_path: str, remote_path: str) -> None:
        """
        Upload a file to the FTP server.

        Args:
            local_path (str): Path to the local file.
            remote_path (str): Path on the FTP server to save the file.
        """
        with open(local_path, "rb") as f:
            self.ftp.storbinary(f"STOR {remote_path}", f)
        print(f"Uploaded '{local_path}' to '{remote_path}'")

    def delete_file(self, remote_path: str) -> None:
        """
        Delete a file from the FTP server.

        Args:
            remote_path (str): Path to the file on the FTP server.
        """
        try:
            self.ftp.delete(remote_path)
            print(f"Deleted '{remote_path}' from server.")
        except error_perm as e:
            print(f"Permission error or file not found: {e}")

    def make_directory(self, remote_path: str) -> None:
        """
        Create a new directory on the FTP server.

        Args:
            remote_path (str): Directory path to create.
        """
        try:
            self.ftp.mkd(remote_path)
            print(f"Created directory '{remote_path}'")
        except error_perm as e:
            print(f"Could not create directory: {e}")

    def change_directory(self, remote_path: str) -> None:
        """
        Change the current working directory on the FTP server.

        Args:
            remote_path (str): Directory path to change to.
        """
        self.ftp.cwd(remote_path)
        print(f"Changed working directory to '{remote_path}'")

    def close(self) -> None:
        """
        Close the FTP connection.
        """
        self.ftp.quit()
        print("FTP connection closed.")

    def __enter__(self) -> "FTPClient":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.close()


if __name__ == "__main__":
    # Replace with your FTP server credentials
    HOST = "ftp.example.com"
    USERNAME = "your_username"
    PASSWORD = "your_password"

    # Use context manager for automatic connection closing
    with FTPClient(HOST, USERNAME, PASSWORD) as client:
        # List files in root directory
        client.list_files()

        # Download a file
        # client.download_file('remote/report.csv', 'local_report.csv')

        # Upload a file
        # client.upload_file('local_data.csv', 'remote/data.csv')

        # Create a new directory
        # client.make_directory('new_folder')

        # Change directory
        # client.change_directory('new_folder')

        # Delete a file
        # client.delete_file('remote/old_report.csv')

"""
Troubleshooting Tips:
- Ensure the FTP server address, username, and password are correct.
- Check your network/firewall settings if you cannot connect.
- Use passive mode if you have issues with firewalls/NAT (self.ftp.set_pasv(True)).
- Handle exceptions for production code for robustness.

Efficiency Tips:
- Use context managers to ensure connections are closed.
- For large files, consider chunked downloads/uploads.
- Use list_files to automate data ingestion pipelines.
"""
