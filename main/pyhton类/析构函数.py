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

    def say(self):
        print("My name is %s, my years old is %d" % (self.name, self.age))

    def __del__(self):
        print("析构函数")


Lucas = Person("Lucas", 24, 178, 130)
del Lucas

