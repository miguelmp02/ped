import socket
import sys
import time
import setproctitle

def cliente(socket_path):
    setproctitle.setproctitle("cli4")

    try:
        client_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        client_socket.connect(socket_path)
        start_time = time.time()
        while time.time() - start_time < 10:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            print("Fecha y hora recibida del servidor:", data)
            time.sleep(1)
        client_socket.close()
        
    except KeyboardInterrupt:
        print("\nCliente detenido.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python3 cli4.py <socket_path>")
        sys.exit(1)

    socket_path = sys.argv[1]
    cliente(socket_path)
