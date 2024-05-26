import os
import sys

class Cliente:
    def __init__(self, fifo_path):
        self.fifo_path = fifo_path

    def enviar_solicitud(self, file_path):
        try:
            with open(self.fifo_path, 'w') as fifo:
                fifo.write(file_path)
        except Exception as e:
            sys.stderr.write("Error: " + str(e))

    def recibir_respuesta(self):
        try:
            with open(self.fifo_path, 'r') as fifo:
                content = fifo.read()
                return content
        except Exception as e:
            sys.stderr.write("Error: " + str(e))
            return None

def cliente_main():
    fifo_path = "/tmp/ped6"
    cliente = Cliente(fifo_path)
    file_path = input("Introduce la ruta completa del archivo: ")
    cliente.enviar_solicitud(file_path)

    content = cliente.recibir_respuesta()
    if content:
        print("Contenido del archivo:")
        print(content)

if __name__ == "__main__":
    cliente_main()

