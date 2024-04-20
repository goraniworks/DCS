import socket

def receive_data():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 8085))
    server_socket.listen(1)
    print("Waiting for connection...")
    
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Received Data: {data.decode()} ")
    finally:
        conn.close()
        server_socket.close()

if __name__ == "__main__":
    receive_data()
