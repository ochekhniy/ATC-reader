import socket
import sys
import os

HOST = ''  # Symbolic name, meaning all available interfaces
PORT = 5040  # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

localDirectory = os.path.dirname(__file__)

# Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

print('Socket bind complete')

# Start listening on socket
s.listen(10)
print('Socket now listening')

# now keep talking with the client
while 1:
    # wait to accept a connection - blocking call
    conn, addr = s.accept()
    print('Connected with ' + addr[0] + ':' + str(addr[1]))
    while True:
        data = conn.recv(1024)
        if not data:
            break

        file = open(os.path.join(localDirectory, 'test.txt'), 'a+')
        file.writelines(str(data.upper())+'\n')
        file.close()

        print(data.upper())

s.close()
