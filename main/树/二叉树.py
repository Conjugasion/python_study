"""
@author Lucas
@date 2019/4/9 20:54
"""


class Node(object):
    value = 100

    def __init__(self, data, lchild=None, rchild=None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild


class Tree(object):

    def __init__(self, root=None):
        self.root = root

    def preVisit(self, root):
        if root is None:
            return
        print(root.data)
        self.preVisit(root.lchild)
        self.preVisit(root.rchild)

    def inVisit(self, root):
        if root is None:
            return
        self.inVisit(root.lchild)
        print(root.data)
        self.inVisit(root.rchild)

    def postVisit(self, root):
        if root is None:
            return
        self.postVisit(root.lchild)
        self.postVisit(root.rchild)
        print(root.data)

    # 广度优先遍历
    def breadth(self, root):
        if root is None:
            return
        queue = list()
        queue.append(root)
        while queue:
            node = queue.pop(0)
            print(node.data)
            # 先压左子树入栈，再压右子树入栈
            if node.lchild:
                queue.append(node.lchild)
            if node.rchild:
                queue.append(node.rchild)

    # 深度优先遍历
    def deep(self, root):
        if root is not None:
            stack = list()
            stack.append(root)
            while stack:
                node = stack.pop(-1)
                print(node.data)
                # 先压右子树入栈，再压左子树入栈
                if node.rchild:
                    stack.append(node.rchild)
                if node.lchild:
                    stack.append(node.lchild)

    # 输出叶子节点
    def leaf(self, root):
        if root is not None:
            if (root.lchild is None) and (root.rchild is None):
                print(root.data)
            else:
                self.leaf(root.lchild)
                self.leaf(root.rchild)


if __name__ == '__main__':
    root1 = Node("A", Node("B", Node("D"), Node("E")), Node("C"))
    root2 = Node('D', Node('B', Node('A'), Node('C')), Node('E', Node('G', Node('F'))))
    print(root1.value)
    tree1 = Tree()
    tree2 = Tree()
    tree1.preVisit(root1)
    print("*******")
    tree2.preVisit(root2)
    print("*******")
    tree1.inVisit(root1)
    print("*******")
    tree1.postVisit(root1)
    print("广度优先遍历")
    tree1.breadth(root1)
    print("深度优先遍历")
    tree1.deep(root1)
    print("输出root1叶子结点")
    tree1.leaf(root1)
    print("输出root2叶子结点")
    tree2.leaf(root2)
