"""
@author Lucas
@date 2019/2/27 22:29
"""
n = int(input())
h = list(map(int, input().split(" ")))
m = int(input())
w = list(map(int, input().split(" ")))

h.sort(reverse=True)
w.sort(reverse=True)
num = 0
while w and h:
    flag = False
    delEleW = ""
    delEleH = ""
    for i in w:
        for j in h:
            if i >= j:
                delEleW = i
                delEleH = j
                num += 1
                flag = True
                break
        break
    if flag:
        w.remove(delEleW)
        h.remove(delEleH)
    else:
        break
print(num)

