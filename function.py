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


def decodeString(string, line_structure_parameter=line_structure):

    data = dict()
    for position in line_structure_parameter:
        data[position[0]] = string[position[1]:position[2]].strip()

    return data


if __name__ == "__main__":
    import csv
    file = open('test-1.txt', 'r')

    outFile = open('out-file.csv', 'w', newline='')

    csvWriter = csv.DictWriter(outFile, fieldnames=fields_names)
    csvWriter.writeheader()

    for row in file.readlines():
        data = decodeString(row, )
        csvWriter.writerow(data)

