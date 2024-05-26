import socket
import sys

CHUNK_SIZE = 4096

def cliente(server_address, server_port, file_path):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        client_socket.sendto(file_path.encode(), (server_address, server_port))
        with open('archivo', 'wb') as f:
            while True:
                response, _ = client_socket.recvfrom(CHUNK_SIZE)
                if response == b'EOF':
                    break
                f.write(response)
        print("Contenido recibido y guardado en 'archivo'.")
    except Exception as e:
        print("Error:", e)
    finally:
        client_socket.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Uso: python3 cli5.py <server_address> <server_port> <file_path>")
        sys.exit(1)

    server_address = sys.argv[1]
    server_port = int(sys.argv[2])
    file_path = sys.argv[3]

    cliente(server_address, server_port, file_path)
