import socket
import sys
import multiprocessing

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message)
            else:
                break
        except:
            print("An error occurred!")
            client_socket.close()
            break

def client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12345))

    nickname = input("Choose your nickname: ")
    client_socket.send(nickname.encode('utf-8'))

    receive_process = multiprocessing.Process(target=receive_messages, args=(client_socket,))
    receive_process.start()

    while True:
        try:
            message = input()
            if message == "/quit":
                client_socket.send("/quit".encode('utf-8'))
                break
            client_socket.send(f"{nickname}: {message}".encode('utf-8'))
        except:
            print("An error occurred!")
            break

    client_socket.close()
    receive_process.terminate()
    receive_process.join()

if __name__ == "__main__":
    client()

