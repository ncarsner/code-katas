import socket

"""
Create a simple TCP server and client.
Practical use case: transferring data between systems or querying remote services.

The example includes:
1. A TCP server that listens for incoming connections and processes data.
2. A TCP client that connects to the server and sends data.

Both examples include type hints, docstrings, and comments for clarity.
"""


# Constants for server configuration
HOST = "127.0.0.1"  # Localhost (change to server IP for remote connections)
PORT = 65432  # Port to listen on (ensure it's not in use)


def start_server(host: str = HOST, port: int = PORT) -> None:
    """
    Starts a TCP server that listens for incoming connections and processes data.

    Args:
        host (str): The IP address to bind the server to.
        port (int): The port to bind the server to.

    Example:
        Run this function in one script to start the server, then use the `start_client` function
        in another script to connect to it.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Server listening on {host}:{port}...")

        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)  # Receive up to 1024 bytes
                    if not data:
                        break
                    print(f"Received data: {data.decode('utf-8')}")
                    conn.sendall(data)  # Echo the data back to the client


def start_client(
    host: str = HOST, port: int = PORT, message: str = "Hello, Server!") -> None:
    """
    Starts a TCP client that connects to the server and sends a message.

    Args:
        host (str): The server's IP address to connect to.
        port (int): The server's port to connect to.
        message (str): The message to send to the server.

    Example:
        Use this function to send data to a running server started with `start_server`.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        print(f"Connected to server at {host}:{port}")
        client_socket.sendall(message.encode("utf-8"))
        data = client_socket.recv(1024)
        print(f"Received response from server: {data.decode('utf-8')}")


if __name__ == "__main__":
    pass
    # Example usage:
    # Uncomment one of the following lines to run the server or client.

    # To start the server:
    # start_server()

    # To start the client:
    # start_client(message="This is a test message for business intelligence.")
