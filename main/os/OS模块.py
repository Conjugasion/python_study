import os
from main.hello import num1


print(os.name)
# print(os.environ)
print(os.curdir)
print(os.getcwd())
# os.mkdir("./file/OSfile")
# os.rmdir("../main/file/OSfile")
print(os.stat("./file/OSfile1"))
# os.rename("./file/OSfile", "./file/OSfile1")
# os.remove("./file/file4.txt")
# os.system("notepad")

p1 = r"D:\Tang\python_exercise\python_study\main\file\OSfile1"
p2 = "Join"
print(os.path.join(p1, p2))

print(os.path.splitext(r"D:\Tang\python_exercise\python_study\main\file\file1.txt"))

print(os.path.isfile(r"D:\Tang\python_exercise\python_study\main\file\OSfile1"))
print(os.path.isdir(r"D:\Tang\python_exercise\python_study\main\file\OSfile1"))

print(os.path.getsize(r"D:\Tang\python_exercise\python_study\main\file\OSfile1\file1.txt"))

print(os.path.dirname(r"D:\Tang\python_exercise\python_study\main\file\OSfile1\file1.txt"))
print(os.path.basename(r"D:\Tang\python_exercise\python_study\main\file\OSfile1\file1.txt"))