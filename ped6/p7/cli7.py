import socket
import select
import sys

def cliente(server_address, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_address, server_port))

    print("Conectado al servidor de chat.\nPrimero escriba un nick único\nDespués, escriba sus mensajes y presione Enter para enviar.")
    nickname = input("Ingrese su nick: ")
    client_socket.send(nickname.encode())

    while True:
        read_sockets, _, _ = select.select([sys.stdin, client_socket], [], [])
        for sock in read_sockets:
            if sock == client_socket:
                mensaje = sock.recv(1024).decode()
                if not mensaje:
                    print("Desconectado del servidor.")
                    return
                print(mensaje)
            else:
                mensaje = sys.stdin.readline().strip()
                if mensaje == "/salir":
                    client_socket.send(mensaje.encode())
                    print("Te has desconectado del chat.")
                    client_socket.close()
                    return
                client_socket.send(mensaje.encode())
                print(f"{nickname}: {mensaje}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python3 cli7.py <server_address> <server_port>")
        sys.exit(1)

    server_address = sys.argv[1]
    server_port = int(sys.argv[2])
    cliente(server_address, server_port)
