import socket
import datetime
import sys
import time

def servidor(server_address, server_port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server_socket.bind((server_address, server_port))
        server_socket.listen()
        print("Servidor esperando conexiones...")

        while True:
            connection, client_address = server_socket.accept()
            print(f"Cliente conectado desde {client_address}")

            try:
                start_time = time.time()
                while time.time() - start_time < 10:
                    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    connection.sendall(current_time.encode())
                    time.sleep(1)
            except Exception as e:
                print("Error:", e)
            finally:
                connection.close()
                print(f"Conexión cerrada con el cliente {client_address}")
    except Exception as e:
        print("Error:", e)
    finally:
        server_socket.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python3 serv6.py <server_address> <server_port>")
        sys.exit(1)

    server_address = sys.argv[1]
    server_port = int(sys.argv[2])
    servidor(server_address, server_port)
