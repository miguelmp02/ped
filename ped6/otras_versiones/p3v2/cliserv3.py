import os
import setproctitle
import time

def servidor():
    setproctitle.setproctitle("serv3")
    # Hijo
    fifo_cliente = "/tmp/fifo_cliente_6"
    fifo_servidor = "/tmp/fifo_servidor_6"

    if not os.path.exists(fifo_cliente):
        os.mkfifo(fifo_cliente)

    if not os.path.exists(fifo_servidor):
        os.mkfifo(fifo_servidor)

    with open(fifo_servidor, 'r') as servidor_fifo:
        path = servidor_fifo.read().strip()
        response = ""

        if os.path.exists(path):
            try:
                with open(path, 'r') as file:
                    response = file.read()
                    print(response)
            except Exception as e:
                response = f"Error al leer el archivo: {str(e)}"
        else:
            response = "Error: El archivo no existe."

    time.sleep(10)

def cliente():
    setproctitle.setproctitle("cli3")
    # Padre
    fifo_cliente = "/tmp/fifo_cliente_6"
    fifo_servidor = "/tmp/fifo_servidor_6"

    if not os.path.exists(fifo_cliente):
        os.mkfifo(fifo_cliente)

    if not os.path.exists(fifo_servidor):
        os.mkfifo(fifo_servidor)

    path = input("Ingrese el path completo del archivo: ")

    with open(fifo_servidor, 'w') as servidor_fifo:
        servidor_fifo.write(path)

    time.sleep(10)

if __name__ == "__main__":
    if os.fork() != 0:
        cliente()
    else:
        servidor()

