import collections
import os


def getAllDir(path):
    queue = collections.deque()
    queue.append(path)
    while len(queue) != 0:
        dirPath = queue.popleft()
        fileList = os.listdir(dirPath)
        for fileName in fileList:
            fileAbsPath = os.path.join(dirPath, fileName)
            if os.path.isdir(fileAbsPath):
                print("目录: ", fileName)
                queue.append(fileAbsPath)
            else:
                print("文件: ", fileName)


path = r"D:\Tang\python_exercise\python_study"
getAllDir(path)
