import os
import socket
import sys
import datetime
import time
import setproctitle

def servidor(socket_path):
    setproctitle.setproctitle("serv4")

    try:
        if os.path.exists(socket_path):
            os.remove(socket_path)
        server_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        server_socket.bind(socket_path)
        server_socket.listen()

        print("Servidor esperando conexiones...")

        while True:
            connection, _ = server_socket.accept()
            print("Cliente conectado.")
            start_time = time.time()
            while time.time() - start_time < 10:
                fecha_hora = obtener_fecha_hora()
                try:
                    connection.sendall(fecha_hora.encode())
                    time.sleep(1)
                except:
                    break
            connection.close()

    except KeyboardInterrupt:
        print("\nServidor detenido.")
    finally:
        server_socket.close()
        if os.path.exists(socket_path):
            os.remove(socket_path)

def obtener_fecha_hora():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python3 serv4.py <socket_path>")
        sys.exit(1)

    socket_path = sys.argv[1]
    servidor(socket_path)

