from Father import father
from Mather import mather


class child(father, mather):

    def __init__(self, money, job, height):
        father.__init__(self, money)
        mather.__init__(self, job)
        self.height = height
        self.age = 24

Mark = child(1000, "学生", 178)
print(Mark.age)
print(Mark.money)
Mark.func()
