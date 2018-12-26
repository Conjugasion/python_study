class Person(object):

    def __init__(self, name, age, height, weight):
        print("类的构造方法")
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        pass

    def run(self):
        print("I am running")

    def eat(self, food):
        print("eat" + food)
