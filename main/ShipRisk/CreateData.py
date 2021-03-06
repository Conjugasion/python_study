"""
  @author Lucas
  @date 2020/4/3 11:25

"""
import random

'''
挪威DNV 0.99、劳埃德LR 0.97、德国GL、美国ABS、日本NK
法国BV、意大利RINA、中国CCS、、韩国KR、俄罗斯RS
其他

                                             100, 85,70,55
classification = [DNV:(0.99,0.01,0,0), RINA:(0.1,0.8,0.1,0)]
'''


def createData(classification):
    result = {}
    for key, value in classification.items():
        grade = 0

        for i in range(0, 100):
            r = 1 - random.random()  # (0, 1]
            if r <= value[0]:
                grade += 100
            elif value[0] < r <= value[0] + value[1]:
                grade += 85
            elif value[0] + value[1] < r <= value[0] + value[1] + value[2]:
                grade += 70
            else:
                grade += 55
        result[key] = round(grade / 100, 1)
    print(result)


if __name__ == '__main__':
    # createData({"挪威DNV": (0.99, 0.01, 0, 0), "劳埃德LR": (0.95, 0.05, 0, 0), "德国GL": (0.93, 0.07, 0, 0),
    #             "美国ABS": (0.9, 0.1, 0, 0),
    #             "日本NK": (0.88, 0.12, 0, 0), "法国BV": (0.84, 0.16, 0, 0), "意大利RINA": (0.80, 0.2, 0, 0),
    #             "中国CCS": (0.75, 0.25, 0, 0),
    #             "韩国KR": (0.72, 0.24, 0.04, 0), "俄罗斯RS": (0.72, 0.24, 0.04, 0), "其他": (0, 0.7, 0.25, 0.05)})

    createData({"6": (0.9, 0.1, 0, 0), "7": (0.7, 0.3, 0, 0), "8": (0.5, 0.3, 0.2, 0), "9": (0.3, 0.3, 0.3, 0.1),
                "10": (0.1, 0.2, 0.4, 0.3),
                "11": (0.6, 0.3, 0.1, 0), "12": (0.4, 0.5, 0.1, 0), "13": (0.3, 0.6, 0.1, 0), "14": (0.2, 0.6, 0.2, 0),
                "15": (0.2, 0.5, 0.3, 0),
                "16": (0.1, 0.3, 0.6, 0), "17": (0, 0.6, 0.4, 0), "18": (0, 0.4, 0.6, 0), "19": (0, 0.2, 0.7, 0.1),
                "20": (0, 0, 0.2, 0.8)})
