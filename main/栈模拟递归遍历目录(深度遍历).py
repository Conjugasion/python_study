import os


def getAllDir(path):
    stack = []
    stack.append(path)
    while len(stack) != 0:
        dirPath = stack.pop()
        fileList = os.listdir(dirPath)
        for filename in fileList:
            fileAbsPath = os.path.join(dirPath, filename)
            if os.path.isdir(fileAbsPath):
                print("目录: ", filename)
                stack.append(fileAbsPath)
            else:
                print("普通文件: ", filename)
    # print(type(stack))


path = r"D:\Tang\python_exercise\python_study"
getAllDir(path)