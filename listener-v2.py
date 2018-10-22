line_structure = [
    ('date', 0, 6, 4),
    ('time', 7, 11, 4),
    ('calling-num', 12, 22, 10),
    ('dialed-num', 23, 40, 17),
    ('sec-dur', 41, 46, 5),
    ('code-dial', 47, 50, 3),
    ('code-used', 51, 54, 3),
    ('out-crt-id', 54, 56, 2),
    ('in-trk-code', 57, 60, 3),
    ('in-crt-id', 60, 62, 2),
    ('cond-code', 63, 64, 1),
    ('return', 64, 65, 1),
    ('line-feed', 65, 66, 1)
]

fields_names = [x[0] for x in line_structure]


def decode_string(string, line_structure_parameter=line_structure):

    decoded = dict()
    for position in line_structure_parameter:
        decoded[position[0]] = string[position[1]:position[2]].strip()

    return decoded


def write_data_to_file(row: str, directory: str):
    data = decode_string(row, )

    if data.get('date'):
        name = data.get('date')

        need_to_made_header = False
        if not file_exists(name + ".csv"):
            need_to_made_header = True

        out_file = open(os.path.join(directory, name + ".csv"), 'a', newline='')
        csv_writer = csv.DictWriter(out_file, fieldnames=fields_names)

        if need_to_made_header:
            csv_writer.writeheader()

        csv_writer.writerow(data)


HOST = ''  # Symbolic name, meaning all available interfaces
PORT = 5040  # Arbitrary non-privileged port


if __name__ == "__main__":
    import socket
    import sys
    import os
    import csv
    from os.path import exists as file_exists

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    localDirectory = os.path.dirname(__file__)

    # Bind socket to local host and port
    try:
        s.bind((HOST, PORT))
    except socket.error as msg:
        sys.exit()

    s.listen(10)

    while 1:
        # wait to accept a connection - blocking call
        conn, address = s.accept()
        # print('Connected with ' + address[0] + ':' + str(address[1]))

        while True:
            data = conn.recv(64).decode()
            if not data:
                break
            # print(data)
            write_data_to_file(data, localDirectory)
            data = ''

    s.close()
