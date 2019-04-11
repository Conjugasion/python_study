"""
@author Lucas
@date 2019/4/3 14:35
"""


def card():
    n = int(input())
    array = sorted(list(map(int, input().split(" "))), reverse=True)

    niuniu = 0
    yangyang = 0
    for i in range(len(array)):
        if i % 2 == 0:
            niuniu += array[i]
        else:
            yangyang += array[i]
    print(niuniu - yangyang)


if __name__ == '__main__':
    card()

