"""
@author Lucas
@date 2019/4/4 14:15
"""


def machine():
    n, m = map(int, input().split())
    machine = []
    task = []
    # 机器[工作时间，等级]
    for i in range(n):
        time, level = map(int, input().split())
        machine.append([time, level])
    # 任务[工作时间，等级]
    for i in range(m):
        time, level = map(int, input().split())
        task.append([time, level])
    # print(machine)
    # print(task)
    machineOrder = sorted(machine, key=lambda x: (x[0], x[1]))
    taskOrder = sorted(task, key=lambda x: (200 * x[0] + 3 * x[1]))
    print(machineOrder)
    print(taskOrder)

    # 倒序遍历,遍历时删除,不出错
    finishNum = 0
    money = 0
    for i in range(len(taskOrder)-1, -1, -1):
        possMachine = []
        for j in range(len(machineOrder)-1, -1, -1):
            if machineOrder[j][0] >= taskOrder[i][0] and machineOrder[j][1] >= taskOrder[i][1]:
                possMachine.append(j)
            elif machineOrder[j][0] < taskOrder[i][0]:
                break
        if possMachine:
            possDict = dict()
            for k in possMachine:
                possDict[machineOrder[k][0] - taskOrder[i][0]] = k
            nearest = possDict[min(possDict)]
            finishNum += 1
            money += 200*taskOrder[i][0] + 3*taskOrder[i][1]
            taskOrder.pop(i)
            machineOrder.pop(nearest)

    print(str(finishNum)+" "+str(money))



    # for i in range(len(taskOrderBylevel)-1, -1, -1):
    #     for j in range(len(machineOrderBylevel)-1, -1, -1):
    #         if taskOrderBylevel:
    #             nearest = -1
    #             minValue = 10000000000
    #             if machineOrderBylevel[j][0] < taskOrderBylevel[i][0] <= machineOrderBylevel[j][0]:
    #                 for k in range(len(machineOrderBylevel)-1, j, -1):
    #                     if machineOrderBylevel[k][1] >= taskOrderBylevel[i][1]:
    #                         if machineOrderBylevel[k][1] - taskOrderBylevel[i][1] < minValue:
    #                             minValue = machineOrderBylevel[k][1] - taskOrderBylevel[i][1]
    #                             nearest = k
    #                 if nearest != -1:
    #                     finishNum += 1
    #                     money += 200*taskOrderBylevel[i][0] + 3*taskOrderBylevel[i][1]
    #                     taskOrderBylevel.pop(i)
    #                     machineOrderBylevel.pop(nearest)
    #                     break
    #             elif machineOrderBylevel[j][0] == taskOrderBylevel[i][0] and machineOrderBylevel[j][1] >= taskOrderBylevel[i][1]:
    #                 nearest = j
    #                 if nearest != -1:
    #                     finishNum += 1
    #                     money += 200*taskOrderBylevel[i][0] + 3*taskOrderBylevel[i][1]
    #                     taskOrderBylevel.pop(i)
    #                     machineOrderBylevel.pop(nearest)
    #                     break








if __name__ == '__main__':
    machine()







