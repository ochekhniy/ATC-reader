import socket
import time


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

PORT = 5040

sock.connect(('localhost', PORT))

counter = 0

print("Start sending")
while True:
    if counter > 5:
        break
    time.sleep(2)
    counter += 1
    print("The ", counter, " try")
    sock.send('041018 1252  322546758           2393288 00032   0 80128 82030 9'.encode())
    sock.send('041018 1252  322354885              6293 00039     81822 80205 9'.encode())

sock.close()

