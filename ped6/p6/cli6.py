import socket
import sys

def cliente(server_address, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((server_address, server_port))
        for _ in range(10):
            response = client_socket.recv(4096)
            print("Fecha y hora del servidor:", response.decode())

    except Exception as e:
        print("Error:", e)
    finally:
        client_socket.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python3 cli6.py <server_address> <server_port>")
        sys.exit(1)

    server_address = sys.argv[1]
    server_port = int(sys.argv[2])
    cliente(server_address, server_port)

