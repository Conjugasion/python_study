from typing import Any


class Person(object):
    static = "123"

    def __init__(self, name, age, height, weight, __money):
        print("类的构造方法")
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.__money = __money

    def run(self):
        print(self.__money)
        print("I am running")

    def eat(self, food):
        print("eat" + food)

    def say(self):
        print("My name is %s, my years old is %d" % (self.name, self.age))

    # def __del__(self):
    #     print("析构函数")

    # toString
    def __str__(self) -> str:
        return "%s, %d, %d, %d, %d" % (self.name, self.age, self.height, self.weight, self.__money)

    def setMoney(self, money):
        self.__money = money

    def getMoney(self):
        return self.__money


Lucas = Person("Lucas", 24, 178, 130, 1000000)
Lucas.run()
Lucas.setMoney(2500000)
print(Lucas.getMoney())


# print(Lucas.static)
Person.static = "123456"
# print(Person.static)
Mark = Person("Mark", 24, 177, 150, 500000)

Lucas.static = "123456789"
print(Lucas.static)
print(Mark.static)