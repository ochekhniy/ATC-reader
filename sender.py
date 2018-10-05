import socket
import time


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

PORT = 5040

sock.connect(('localhost', PORT))

counter = 0

print("Start sending")
while True:
    if counter > 20:
        break
    time.sleep(2)
    counter += 1
    print("The ", counter, " try")
    message = 'hello, world! Try number: {}'.format(counter)
    sock.send(message.encode())

sock.close()

