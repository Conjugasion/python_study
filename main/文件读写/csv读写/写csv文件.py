import csv


def writeCsv(path, data):
    with open(path, "w") as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)


path = r"D:\Tang\python_exercise\python_study\main\文件读写\csv读写\02.csv"
writeCsv(path, ["asd", "2", ("c", 3), [123, 123, 123]])
