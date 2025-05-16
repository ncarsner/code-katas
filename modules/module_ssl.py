import ssl
import socket
from typing import Optional, Tuple

"""
Practical examples: secure HTTP requests, certificate validation, and creating SSL contexts for secure data transfer.
"""


def create_ssl_context(cafile: Optional[str] = None) -> ssl.SSLContext:
    """
    Create a secure SSL context for HTTPS connections.

    Args:
        cafile (Optional[str]): Path to a CA bundle file for certificate validation.
                                If None, uses system default.

    Returns:
        ssl.SSLContext: Configured SSL context.

    Example:
        context = create_ssl_context()
    """
    context = ssl.create_default_context(cafile=cafile)
    # For stricter security, disable older protocols:
    context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1
    return context


def get_certificate_info(
    hostname: str, port: int = 443, context: Optional[ssl.SSLContext] = None
) -> dict:
    """
    Retrieve and parse the SSL certificate from a remote server.

    Args:
        hostname (str): The server's hostname.
        port (int): The port to connect to (default: 443).
        context (Optional[ssl.SSLContext]): SSL context to use.

    Returns:
        dict: Certificate information.

    Example:
        cert_info = get_certificate_info('www.google.com')
    """
    if context is None:
        context = create_ssl_context()
    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert()
    return cert


def secure_socket_connection(
    hostname: str, port: int = 443, context: Optional[ssl.SSLContext] = None
) -> Tuple[ssl.SSLSocket, socket.socket]:
    """
    Establish a secure socket connection to a remote server.

    Args:
        hostname (str): The server's hostname.
        port (int): The port to connect to (default: 443).
        context (Optional[ssl.SSLContext]): SSL context to use.

    Returns:
        Tuple[ssl.SSLSocket, socket.socket]: The SSL-wrapped socket and the original socket.

    Example:
        ssl_sock, raw_sock = secure_socket_connection('www.example.com')
    """
    if context is None:
        context = create_ssl_context()
    raw_sock = socket.create_connection((hostname, port))
    ssl_sock = context.wrap_socket(raw_sock, server_hostname=hostname)
    return ssl_sock, raw_sock


def verify_server_certificate(hostname: str, cafile: Optional[str] = None) -> bool:
    """
    Verify if the server's SSL certificate is valid and trusted.

    Args:
        hostname (str): The server's hostname.
        cafile (Optional[str]): Path to a CA bundle file.

    Returns:
        bool: True if certificate is valid, False otherwise.

    Example:
        is_valid = verify_server_certificate('www.github.com')
    """
    try:
        context = create_ssl_context(cafile)
        with socket.create_connection((hostname, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname):
                pass  # If no exception, certificate is valid
        return True
    except ssl.SSLError as e:
        print(f"SSL error: {e}")
        return False
    except Exception as e:
        print(f"Connection error: {e}")
        return False


if __name__ == "__main__":
    # 1. Validate a data provider's SSL certificate before downloading data.
    host = "www.google.com"
    print(f"Validating SSL certificate for {host}...")
    if verify_server_certificate(host):
        print("Certificate is valid and trusted.")
        cert_info = get_certificate_info(host)
        print("Certificate subject:", cert_info.get("subject"))
    else:
        print("Certificate validation failed. Do not proceed with data transfer.")

    # 2. Use a secure context for custom HTTPS requests (e.g., with urllib or requests).
    # Documentation available for integrating with requests: requests.get(url, verify=context)
