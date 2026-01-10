import selectors
import socket
import sys
from typing import Dict
import json
import time

"""
The selectors module provides high-level I/O multiplexing, allowing efficient onitoring of multiple file descriptors (sockets, files, pipes). Essential for building scalable network servers, data pipelines, and event-driven architectures.

Key concepts:
- More efficient than polling multiple sockets in a loop
- Cross-platform abstraction (epoll on Linux, kqueue on BSD/macOS, select elsewhere)
- Perfect for handling multiple client connections or data sources simultaneously
"""



def basic_socket_server() -> None:
    """
    Example 1: Basic multi-client TCP server for data ingestion.
    
    Use case: A data collection service that receives JSON data from multiple
    ETL processes or IoT devices simultaneously.
    
    Demonstrates:
    - DefaultSelector for automatic best selector choice
    - EVENT_READ for monitoring incoming data
    - Non-blocking sockets
    - Data attribute for storing connection-specific state
    """
    sel = selectors.DefaultSelector()  # Automatically picks best implementation
    
    def accept_connection(sock: socket.socket) -> None:
        """Accept new client connections and register them."""
        conn, addr = sock.accept()
        print(f"[SERVER] New connection from {addr}")
        conn.setblocking(False)  # Critical for multiplexing
        
        # Register client socket with metadata
        sel.register(conn, selectors.EVENT_READ, data={'addr': addr, 'buffer': b''})
    
    def handle_client_data(conn: socket.socket, mask: int) -> None:
        """Process data from connected clients."""
        sock_data = sel.get_key(conn).data
        
        try:
            data = conn.recv(1024)
            if data:
                sock_data['buffer'] += data
                # Process complete JSON messages (newline-delimited)
                if b'\n' in sock_data['buffer']:
                    message = sock_data['buffer'].decode('utf-8').strip()
                    print(f"[SERVER] Received from {sock_data['addr']}: {message}")
                    sock_data['buffer'] = b''
            else:
                # Client disconnected
                print(f"[SERVER] Client {sock_data['addr']} disconnected")
                sel.unregister(conn)
                conn.close()
        except Exception as e:
            print(f"[SERVER] Error handling client: {e}")
            sel.unregister(conn)
            conn.close()
    
    # Setup server socket
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind(('localhost', 9999))
    server_sock.listen(5)
    server_sock.setblocking(False)
    
    # Register server socket to accept new connections
    sel.register(server_sock, selectors.EVENT_READ, data=None)
    print("[SERVER] Listening on localhost:9999...")
    
    try:
        # Event loop - scalable to thousands of connections
        while True:
            events = sel.select(timeout=1)  # 1-second timeout for graceful shutdown
            for key, mask in events:
                if key.data is None:
                    # Server socket ready to accept
                    accept_connection(key.fileobj)  # type: ignore[arg-type]
                else:
                    # Client socket has data
                    handle_client_data(key.fileobj, mask) # type: ignore[arg-type]
    except KeyboardInterrupt:
        print("\n[SERVER] Shutting down...")
    finally:
        sel.close()
        server_sock.close()


def bidirectional_communication() -> None:
    """
    Example 2: Bidirectional communication with EVENT_READ and EVENT_WRITE.
    
    Use case: API gateway that receives requests and forwards responses,
    or a data streaming service that both receives and sends data.
    
    Demonstrates:
    - EVENT_WRITE for monitoring when socket is ready to send
    - Managing write buffers
    - State machine pattern for connection handling
    """
    sel = selectors.DefaultSelector()
    
    class Connection:
        """Represents a client connection with buffered I/O."""
        def __init__(self, sock: socket.socket, addr: tuple):
            self.sock = sock
            self.addr = addr
            self.recv_buffer = b''
            self.send_buffer = b''
        
        def queue_response(self, message: str) -> None:
            """Queue a message to be sent to the client."""
            self.send_buffer += message.encode('utf-8') + b'\n'
    
    connections: Dict[socket.socket, Connection] = {}
    
    def accept_connection(server_sock: socket.socket) -> None:
        conn, addr = server_sock.accept()
        print(f"[BIDIR] Connected: {addr}")
        conn.setblocking(False)
        
        connection = Connection(conn, addr)
        connections[conn] = connection
        
        # Start by monitoring reads
        sel.register(conn, selectors.EVENT_READ)
    
    def service_connection(key: selectors.SelectorKey, mask: int) -> None:
        sock = key.fileobj
        conn = connections[sock]  # type: ignore[index]
        
        if mask & selectors.EVENT_READ:
            # Ready to read
            data = sock.recv(1024)  # type: ignore[assignment]
            if data:
                conn.recv_buffer += data
                if b'\n' in conn.recv_buffer:
                    message = conn.recv_buffer.decode('utf-8').strip()
                    print(f"[BIDIR] Received: {message}")
                    
                    # Echo response with timestamp
                    response = f"ACK: {message} at {time.time()}"
                    conn.queue_response(response)
                    conn.recv_buffer = b''
                    
                    # Update events to include WRITE
                    sel.modify(sock, selectors.EVENT_READ | selectors.EVENT_WRITE)
            else:
                # Connection closed
                print(f"[BIDIR] Closed: {conn.addr}")
                sel.unregister(sock)
                sock.close()  # type: ignore[arg-type]
                del connections[sock] # type: ignore[arg-type]
        
        if mask & selectors.EVENT_WRITE:
            # Ready to write
            if conn.send_buffer:
                sent = sock.send(conn.send_buffer)  # type: ignore[assignment]
                conn.send_buffer = conn.send_buffer[sent:]
            
            # If buffer empty, stop monitoring writes (efficiency)
            if not conn.send_buffer:
                sel.modify(sock, selectors.EVENT_READ)
    
    # Setup server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('localhost', 10000))
    server.listen(5)
    server.setblocking(False)
    sel.register(server, selectors.EVENT_READ, data='server')
    
    print("[BIDIR] Server running on localhost:10000...")
    
    try:
        while True:
            events = sel.select(timeout=1)
            for key, mask in events:
                if key.data == 'server':
                    accept_connection(key.fileobj) # type: ignore[arg-type]
                else:
                    service_connection(key, mask)
    except KeyboardInterrupt:
        print("\n[BIDIR] Shutting down...")
    finally:
        sel.close()
        server.close()


def multiple_data_sources() -> None:
    """
    Example 3: Monitoring multiple input sources (network + stdin).
    
    Use case: Interactive monitoring tool that processes network data streams
    while accepting user commands, or a control plane for distributed systems.
    
    Demonstrates:
    - Monitoring non-socket file descriptors (stdin)
    - Combining different I/O types
    - Pattern for command-driven data processing
    """
    sel = selectors.DefaultSelector()
    
    # Monitor stdin for user commands
    sel.register(sys.stdin, selectors.EVENT_READ, data='stdin')
    
    # Setup network socket for data ingestion
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP for simplicity
    sock.bind(('localhost', 11000))
    sock.setblocking(False)
    sel.register(sock, selectors.EVENT_READ, data='network')
    
    print("[MULTI] Monitoring stdin and UDP socket on localhost:11000")
    print("[MULTI] Type 'status' for stats, 'quit' to exit")
    
    stats = {'messages_received': 0, 'commands_processed': 0}
    
    try:
        while True:
            events = sel.select(timeout=1)
            
            for key, mask in events:
                if key.data == 'stdin':
                    # User command
                    command = sys.stdin.readline().strip()
                    stats['commands_processed'] += 1
                    
                    if command == 'quit':
                        print("[MULTI] Exiting...")
                        return
                    elif command == 'status':
                        print(f"[MULTI] Stats: {json.dumps(stats, indent=2)}")
                    else:
                        print(f"[MULTI] Unknown command: {command}")
                
                elif key.data == 'network':
                    # Network data
                    data, addr = sock.recvfrom(1024)
                    stats['messages_received'] += 1
                    print(f"[MULTI] UDP from {addr}: {data.decode('utf-8', errors='ignore')}")
    
    finally:
        sel.close()
        sock.close()


def timeout_handling() -> None:
    """
    Example 4: Connection timeout and idle detection.
    
    Use case: Production servers need to detect and close idle connections
    to prevent resource exhaustion and maintain SLA requirements.
    
    Demonstrates:
    - Using select() timeout for periodic tasks
    - Tracking connection activity timestamps
    - Implementing connection health checks
    """
    sel = selectors.DefaultSelector()
    
    class ManagedConnection:
        def __init__(self, sock: socket.socket, addr: tuple):
            self.sock = sock
            self.addr = addr
            self.last_activity = time.time()
            self.data = b''
    
    connections: Dict[socket.socket, ManagedConnection] = {}
    IDLE_TIMEOUT = 30  # seconds
    
    def check_idle_connections() -> None:
        """Close connections that have been idle too long."""
        now = time.time()
        idle_socks = [
            sock for sock, conn in connections.items()
            if now - conn.last_activity > IDLE_TIMEOUT
        ]
        
        for sock in idle_socks:
            conn = connections[sock]
            print(f"[TIMEOUT] Closing idle connection: {conn.addr}")
            sel.unregister(sock)
            sock.close()  # type: ignore[arg-type]
            del connections[sock]  # type: ignore[arg-type]
    
    # Server setup omitted for brevity (similar to previous examples)
    print(f"[TIMEOUT] Idle timeout set to {IDLE_TIMEOUT} seconds")
    print("[TIMEOUT] Periodic health checks every second")
    
    # Event loop with timeout
    # while True:
    #     events = sel.select(timeout=1)  # Returns every second even if no events
    #     
    #     for key, mask in events:
    #         # Handle events and update last_activity
    #         conn = connections[key.fileobj]
    #         conn.last_activity = time.time()
    #     
    #     # Periodic maintenance task
    #     check_idle_connections()


if __name__ == "__main__":
    print("Python selectors module examples for scalable I/O multiplexing\n")
    print("Choose an example to run:")
    print("1. Basic multi-client server (data ingestion)")
    print("2. Bidirectional communication (API gateway pattern)")
    print("3. Multiple data sources (network + stdin)")
    print("4. Timeout handling (connection management)")
    print("\nUncomment the desired example below to run it.")
    
    # Uncomment to run:
    # basic_socket_server()
    # bidirectional_communication()
    # multiple_data_sources()
    # timeout_handling()  # Note: This is a pattern demo, not runnable
    
    print("\nKey takeaways for production use:")
    print("- Use DefaultSelector for automatic platform optimization")
    print("- Always use non-blocking sockets with selectors")
    print("- Monitor EVENT_WRITE only when you have data to send")
    print("- Implement timeouts to prevent resource leaks")
    print("- Store connection state in the 'data' attribute")
    print("- Handle exceptions per connection to avoid cascade failures")