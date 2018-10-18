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


def write_data_to_file(row : str):
    data = decode_string(row, )

    if data.get('date'):
        name = data.get('date')

        need_to_made_header = False
        if not file_exists(name + ".csv"):
            need_to_made_header = True

        out_file = open(name + ".csv", 'a', newline='')
        csv_writer = csv.DictWriter(out_file, fieldnames=fields_names)

        if need_to_made_header:
            csv_writer.writeheader()

        csv_writer.writerow(data)


if __name__ == "__main__":
    import csv
    from os.path import exists as file_exists

    file = open('test-1.txt', 'r')

    for row in file.readlines():
        write_data_to_file(row)
