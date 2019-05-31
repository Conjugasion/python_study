"""
@author Lucas
@date 2019/4/2 19:00
"""


# 基数排序
def radixSort(a):
    length = 1
    for i in range(len(a)):
        a[i] = str(a[i])
        if length < len(a[i]):
            length = len(a[i])
    # 左边补齐0
    for i in range(len(a)):
        if len(a[i]) < length:
            a[i] = (length-len(a[i])) * "0" + a[i]

    for j in range(length):
        dict1 = {"0": [], "1": [], "2": [], "3": [], "4": [], "5": [], "6": [], "7": [], "8": [], "9": []}
        for i in a:
            if i[-j-1] == "0":
                dict1["0"].append(i)
            elif i[-j-1] == "1":
                dict1["1"].append(i)
            elif i[-j-1] == "2":
                dict1["2"].append(i)
            elif i[-j-1] == "3":
                dict1["3"].append(i)
            elif i[-j-1] == "4":
                dict1["4"].append(i)
            elif i[-j-1] == "5":
                dict1["5"].append(i)
            elif i[-j-1] == "6":
                dict1["6"].append(i)
            elif i[-j-1] == "7":
                dict1["7"].append(i)
            elif i[-j-1] == "8":
                dict1["8"].append(i)
            else:
                dict1["9"].append(i)
        a.clear()
        for key in dict1:
            a += dict1[key]

    for i in range(len(a)):
        a[i] = int(a[i])


if __name__ == '__main__':
    a = [2222, 555, 90, 7, 37, 3123, 156, 41, 65, 123]
    radixSort(a)
    print(a)
