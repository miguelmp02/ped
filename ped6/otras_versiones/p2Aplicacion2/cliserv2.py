import os
import setproctitle
import time

def servidor(cli2, serv2):
    setproctitle.setproctitle("serv2")
    # Hijo
    os.close(serv2)
    path = os.read(cli2, 1024).decode().strip()
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
    
    os.close(cli2)
    time.sleep(10)

def cliente(cli2, serv2):
    setproctitle.setproctitle("cli2")
    # Padre
    os.close(cli2)
    path = input("Ingrese el path completo del archivo: ")
    os.write(serv2, path.encode())
    os.close(serv2)
    time.sleep(10)

if __name__ == "__main__":
    cli2, serv2 = os.pipe()

    if os.fork() != 0:
        cliente(cli2, serv2)
    else:
        servidor(cli2, serv2)

