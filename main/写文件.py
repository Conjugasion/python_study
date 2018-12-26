path = r"D:\Tang\python_exercise\python_study\main\file\file2.txt"
f = open(path, "w", encoding="utf-8", errors="ignore")
f.write("Mark is a bad man")
# f.flush()
# while True:
#     pass
f.close()