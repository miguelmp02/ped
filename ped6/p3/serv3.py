import os
import sys

class Servidor:
    def __init__(self, fifo_path):
        self.fifo_path = fifo_path

    def iniciar_servidor(self):
        try:
            os.mkfifo(self.fifo_path)
        except FileExistsError:
            pass
        try:
            with open(self.fifo_path, 'r') as fifo:
                file_path = fifo.readline().strip()

                if os.path.isfile(file_path):
                    with open(file_path, 'r') as file:
                        content = file.read()
                else:
                    content = "Error: El archivo especificado no existe."

            with open(self.fifo_path, 'w') as fifo:
                fifo.write(content)
        except Exception as e:
            sys.stderr.write("Error: " + str(e))
        finally:
            os.remove(self.fifo_path) 

def servidor_main():
    fifo_path = "/tmp/ped6"
    servidor = Servidor(fifo_path)
    servidor.iniciar_servidor()

if __name__ == "__main__":
    servidor_main()

