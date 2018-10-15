import csv

lineStructure = [
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

fieldsNames = [x[0] for x in lineStructure]


file = open('test-1.txt', 'r')

outFile = open('out-file.csv', 'w', newline='')

csvWriter = csv.DictWriter(outFile, fieldnames=fieldsNames)
csvWriter.writeheader()

for row in file.readlines():
    data = dict()
    for position in lineStructure:
        data[position[0]] = row[position[1]:position[2]].strip()

    # csvWriter.writeheader()
    csvWriter.writerow(data)
    # print(data)
