"""
@author Lucas
@date 2019/4/15 19:20
"""


# 单链表
class Node(object):

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class MyLinkList(object):

    def __init__(self):
        self.head = 0

    def initList(self, data):
        self.head = Node(data[0])
        p = self.head
        for i in data[1:]:
            node = Node(i)
            p.next = node
            p = p.next

    def getList(self):
        p = self.head
        while True:
            print(p.value)
            if p.next is None:
                break
            p = p.next

    def insert(self, index, value):
        if index == 0:
            node = Node(value, self.head)
            self.head = node
        else:
            j = 0
            p = self.head
            while True:
                if j == index - 1:
                    break
                p = p.next
                j += 1
            node = Node(value, p.next)
            p.next = node

    def delete(self, index):
        if index == 0:
            self.head = self.head.next
        else:
            j = 0
            p = self.head
            while True:
                if j == index - 1:
                    break
                p = p.next
                j += 1
            p.next = p.next.next

    def length(self):
        length = 1
        p = self.head
        while True:
            if p.next is None:
                break
            p = p.next
            length += 1
        print(length)


if __name__ == '__main__':
    list1 = MyLinkList()
    list1.initList([3, 1, 2, 0])
    # list1.getList()
    list1.insert(1, 4)
    list1.getList()
    print("********")
    list1.delete(2)
    list1.getList()
    print("长度")
    list1.length()






