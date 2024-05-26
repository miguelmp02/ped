import os
import datetime
import pytz
import setproctitle

def get_fecha_hora():
    tiempo = pytz.timezone('Europe/Madrid')
    current_time = datetime.datetime.now(tiempo)
    return current_time.strftime('%Y-%m-%d %H:%M:%S')

def servidor(read_pipe, write_pipe):
    setproctitle.setproctitle("serv2")
    os.close(read_pipe)
    fecha_hora = get_fecha_hora()
    os.write(write_pipe, fecha_hora.encode())
    os.close(write_pipe)

def cliente(read_pipe, write_pipe):
    setproctitle.setproctitle("cli2")
    os.close(write_pipe)
    fecha_hora = os.read(read_pipe, 100).decode()
    if fecha_hora:
        print("Fecha y hora recibida del servidor:", fecha_hora)
    os.close(read_pipe)

if __name__ == "__main__":
    read_pipe, write_pipe = os.pipe()

    pid = os.fork()
    if pid != 0:
        cliente(read_pipe, write_pipe)
    else:
        servidor(read_pipe, write_pipe)

