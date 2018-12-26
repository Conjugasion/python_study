from types import MethodType


class Person:
    __slots__ = ("name", "sayHello")
    pass


Lucas = Person()
Lucas.name = "Lucas"
print(Lucas.name)


def sayHello(self, age):
    print("Hello, I am " + self.name + ",I am " + str(age) + " years old")


Lucas.sayHello = MethodType(sayHello, Lucas)
Lucas.sayHello(24)


def eat(self, food):
    print("eat " + food)


Person.eat = MethodType(eat, Person)
Person.eat("apple")
Lucas.eat("Pear")
Person.age = 40
print(Lucas.age)
