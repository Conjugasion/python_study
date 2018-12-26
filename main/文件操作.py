import pickle

myList = [1, 2, 3, 4, 5, "Lucas is a good man"]
path = r"D:\Tang\python_exercise\python_study\main\file\file3.txt"
f = open(path, "wb")
# f.write(str(myList))
# f.flush()

pickle.dump(myList, f)
f.close()

# 读取
f1 = open(path, "rb")
tempList = pickle.load(f1)
print(tempList)
f1.close()