import socket
import select
import sys

def broadcast_message(sock, mensaje, server_socket, clientes):
    for client_socket in clientes:
        if client_socket != server_socket and client_socket != sock:
            try:
                client_socket.send(mensaje.encode())
            except:
                client_socket.close()
                if client_socket in clientes:
                    clientes.remove(client_socket)

def servidor(server_address, server_port):
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((server_address, server_port))
    server_socket.listen()
    print("Servidor esperando conexiones...")

    clientes = []
    nicknames = {}

    try:
        while True:
            read_sockets, _, _ = select.select([server_socket] + clientes, [], [])

            for sock in read_sockets:
                if sock == server_socket:
                    client_socket, client_address = server_socket.accept()
                    print(f"Cliente {client_address} conectado.")
                    client_socket.send("Ingrese su nick: ".encode())
                    clientes.append(client_socket)
                else:
                    try:
                        mensaje = sock.recv(1024).decode().strip()
                        if mensaje:
                            if sock not in nicknames:
                                if mensaje in nicknames.values():
                                    sock.send("Nick ya en uso. Pruebe con otro.".encode())
                                    clientes.remove(sock)
                                    sock.close()
                                else:
                                    nicknames[sock] = mensaje
                                    sock.send(f"Bienvenido al chat, {mensaje}!\n".encode())
                                    broadcast_message(sock, f"{mensaje} se ha unido al chat.", server_socket, clientes)
                            else:
                                nick = nicknames[sock]
                                if mensaje == "/salir":
                                    broadcast_message(sock, f"{nick} ha dejado el chat.", server_socket, clientes)
                                    del nicknames[sock]
                                    clientes.remove(sock)
                                    sock.close()
                                else:
                                    broadcast_message(sock, f"{nick}: {mensaje}", server_socket, clientes)
                        else:
                            if sock in nicknames:
                                nick = nicknames[sock]
                                broadcast_message(sock, f"{nick} ha dejado el chat.", server_socket, clientes)
                                del nicknames[sock]
                            clientes.remove(sock)
                            sock.close()
                    except:
                        continue

    except KeyboardInterrupt:
        print("\nServidor detenido.")
        for sock in clientes:
            sock.send("Servidor detenido. Desconectando...".encode())
            sock.close()
    finally:
        server_socket.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python3 serv7.py <server_address> <server_port>")
        sys.exit(1)

    server_address = sys.argv[1]
    server_port = int(sys.argv[2])
    servidor(server_address, server_port)
