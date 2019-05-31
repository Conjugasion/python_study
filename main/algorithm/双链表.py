"""
@author Lucas
@date 2019/4/15 20:42
"""


# 双链表
class Node(object):
    def __init__(self, value, prior=None, next=None):
        self.value = value
        self.prior = prior
        self.next = next


class MyLinkedList(object):
    def __init__(self):
        self.head = 0

    def initList(self, data):
        self.head = Node(value=data[0])
        p = self.head

        for i in data[1:]:
            p.next = Node(value=i, prior=p)
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
            node = Node(value, prior=None, next=self.head)
            self.head = node
        else:
            j = 0
            p = self.head
            while True:
                if j == index - 1:
                    break
                p = p.next
                j += 1
            node = Node(value, prior=p, next=p.next)
            p.next.prior = node
            p.next = node


if __name__ == '__main__':
    list1 = MyLinkedList()
    list1.initList([3, 1, 2])
    list1.getList()
    print("插入")
    list1.insert(1, 4)
    list1.getList()











