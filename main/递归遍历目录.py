import os


def getAllDir(path):
    fileList = os.listdir(path)
    for filename in fileList:
        fileAbsPath = os.path.join(path, filename)
        if os.path.isdir(fileAbsPath):
            print("目录: ", filename)
            getAllDir(fileAbsPath)
        else:
            print("普通文件: ", filename)


path = r"D:\Tang\python_exercise\python_study"
getAllDir(path)