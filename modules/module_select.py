import select
import socket
from typing import List


def create_server_socket(host: str, port: int) -> socket.socket:
    """
    Creates a non-blocking server socket.

    Args:
        host (str): The hostname or IP address to bind the server to.
        port (int): The port number to bind the server to.

    Returns:
        socket.socket: A non-blocking server socket.
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(5)
    server_socket.setblocking(False)
    return server_socket


def handle_client_data(client_socket: socket.socket) -> None:
    """
    Reads data from a client socket and processes it.

    Args:
        client_socket (socket.socket): The client socket to read data from.
    """
    try:
        data = client_socket.recv(1024)
        if data:
            print(f"Received data: {data.decode('utf-8')}")
            client_socket.sendall(b"Data received")
        else:
            print("Client disconnected")
            client_socket.close()
    except Exception as e:
        print(f"Error handling client data: {e}")
        client_socket.close()


def run_select_server(host: str, port: int) -> None:
    """
    Runs a scalable server using the select module to handle multiple clients.

    Args:
        host (str): The hostname or IP address to bind the server to.
        port (int): The port number to bind the server to.
    """
    server_socket = create_server_socket(host, port)
    print(f"Server started on {host}:{port}")

    # Lists to track sockets
    inputs: List[socket.socket] = [server_socket]
    outputs: List[socket.socket] = []
    message_queues: dict = {}

    try:
        while True:
            # Use select to monitor sockets for I/O readiness
            readable, writable, exceptional = select.select(inputs, outputs, inputs)

            # Handle readable sockets
            for s in readable:
                if s is server_socket:
                    # Accept new connection
                    client_socket, client_address = s.accept()
                    print(f"New connection from {client_address}")
                    client_socket.setblocking(False)
                    inputs.append(client_socket)
                    message_queues[client_socket] = b""
                else:
                    # Handle client data
                    handle_client_data(s)
                    inputs.remove(s)
                    del message_queues[s]

            # Handle writable sockets
            for s in writable:
                if s in message_queues and message_queues[s]:
                    try:
                        s.send(message_queues[s])
                        message_queues[s] = b""
                    except Exception as e:
                        print(f"Error sending data: {e}")
                        inputs.remove(s)
                        outputs.remove(s)
                        del message_queues[s]

            # Handle exceptional sockets
            for s in exceptional:
                print(f"Handling exceptional condition for {s.getpeername()}")
                inputs.remove(s)
                if s in outputs:
                    outputs.remove(s)
                s.close()
                del message_queues[s]

    except KeyboardInterrupt:
        print("Server shutting down...")
    finally:
        server_socket.close()


if __name__ == "__main__":
    # Run the server on localhost and port 8080
    run_select_server("127.0.0.1", 8080)
