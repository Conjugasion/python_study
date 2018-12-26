from person import person


class student(person):
    def __init__(self, name, age, money, grade):
        # 调用父类中的__init__
        super(student, self).__init__(name, age, money)
        # person.__init__(self, name, age, money)
        self.grade = grade

    def run(self, place):
        print("I am running in " + place)

    def showMoney(self):
        return self.getMoney()

    def exam(self):
        print("正在考试")
