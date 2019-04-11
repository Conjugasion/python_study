"""
@author Lucas
@date 2019/4/5 20:52
"""


def live():
    n = int(input())
    d1 = []
    p1 = []
    d = str(input()).split(" ")
    for i in d:
        d1.append(int(i))
    # print(d1)
    p = str(input()).split(" ")
    for i in p:
        p1.append(int(i))
    # print(m1)

    money = 0
    fight = 0
    for x in range(len(d1)):
        if x == 0:
            money += p1[0]
            fight += d1[0]
        if x <= len(d1) - 3:
            if fight < d1[x+2]:
                money += p1[x+1]
                fight += d1[x+1]
        if x == len(d1) - 2:
            if fight < d1[x+1]:
                money += p1[x]
                fight += d1[x]
    print(money)




if __name__ == '__main__':
    live()
