import socket
import sys
import os

CHUNK_SIZE = 4096

def servidor(server_address, server_port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        server_socket.bind((server_address, server_port))

        print("Servidor esperando solicitudes...")

        while True:
            data, client_address = server_socket.recvfrom(CHUNK_SIZE)
            file_path = data.decode()
            print("Cliente conectado:", client_address)
            if os.path.isfile(file_path):
                try:
                    with open(file_path, 'rb') as file:
                        while True:
                            chunk = file.read(CHUNK_SIZE)
                            if not chunk:
                                break
                            server_socket.sendto(chunk, client_address)
                    server_socket.sendto(b'EOF', client_address)
                except Exception as e:
                    error_message = f"Error al leer el archivo: {str(e)}"
                    server_socket.sendto(error_message.encode(), client_address)
            else:
                server_socket.sendto(b"Error: El archivo especificado no existe.", client_address)
    except Exception as e:
        print("Error:", e)
    finally:
        server_socket.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python3 serv5.py <server_address> <server_port>")
        sys.exit(1)

    server_address = sys.argv[1]
    server_port = int(sys.argv[2])

    servidor(server_address, server_port)

