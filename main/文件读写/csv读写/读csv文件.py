import csv


def readCsv(path):
    infoList = []
    with open(path, "r", encoding="UTF-8-sig") as f:
        allFileInfo = csv.reader(f)
        # print(allFileInfo)
        # 按行打印
        for row in allFileInfo:
            infoList.append(row)
    return infoList


if __name__ == '__main__':
    path = r"D:\Tang\python_exercise\python_study\main\文件读写\csv读写\01.csv"
    info = readCsv(path)
    for row in info:
        print(row)
