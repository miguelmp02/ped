import socket
import select
import sys
import multiprocessing

def handle_client(client_socket, client_address, clients, nicknames):
    nickname = nicknames[client_socket]
    client_socket.send(f"Welcome to the chat, {nickname}!".encode('utf-8'))
    broadcast(f"{nickname} has joined the chat!", client_socket, clients, include_sender=True)
    
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                if message == "/quit":
                    break
                broadcast_message = f"{nickname}: {message}"
                print(broadcast_message)
                broadcast(broadcast_message, client_socket, clients)
            else:
                break
        except:
            break
    
    print(f"Client {nickname} disconnected")
    broadcast(f"{nickname} has left the chat.", client_socket, clients)
    client_socket.close()
    clients.remove(client_socket)
    del nicknames[client_socket]

def broadcast(message, sender_socket, clients, include_sender=False):
    for client in clients:
        if client != sender_socket or include_sender:
            try:
                client.send(message.encode('utf-8'))
            except:
                client.close()
                clients.remove(client)

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('0.0.0.0', 12345))
    server_socket.listen(5)
    print("Server started on port 12345")

    clients = []
    nicknames = {}

    try:
        while True:
            read_sockets, _, _ = select.select([server_socket] + clients, [], [])
            for sock in read_sockets:
                if sock == server_socket:
                    client_socket, client_address = server_socket.accept()
                    client_socket.send("NICK".encode('utf-8'))
                    nickname = client_socket.recv(1024).decode('utf-8')

                    if nickname in nicknames.values():
                        client_socket.send("Nickname already taken. Try another one.".encode('utf-8'))
                        client_socket.close()
                    else:
                        clients.append(client_socket)
                        nicknames[client_socket] = nickname
                        print(f"Nickname is {nickname}")
                        process = multiprocessing.Process(target=handle_client, args=(client_socket, client_address, clients, nicknames))
                        process.start()
                else:
                    try:
                        message = sock.recv(1024).decode('utf-8')
                        if message:
                            broadcast(message, sock, clients, include_sender=True)
                    except:
                        sock.close()
                        clients.remove(sock)
    except KeyboardInterrupt:
        print("Server shutting down.")
        for client in clients:
            client.send("Server shutting down. Disconnecting...".encode('utf-8'))
            client.close()
        server_socket.close()

if __name__ == "__main__":
    server()

