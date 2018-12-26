class person(object):

    def __init__(self, name, age, money):
        print("类的构造方法")
        self.name = name
        self.age = age
        self.__money = money

    def run(self):
        print("I am running")

    def __eat(self, food):
        print("eat" + food)

    def setMoney(self, money):
        self.__money = money

    def getMoney(self):
        return self.__money

    # toString
    def __str__(self) -> str:
        return "%s, %d" % (self.name, self.age)

