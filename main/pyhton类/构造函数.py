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
        print(self.__class__("Jack", 24, 178, 130))

    def eat(self, food):
        print("eat" + food)

    def say(self):
        print("My name is %s, my years old is %d" % (self.name, self.age))


Lucas = Person("Lucas", 24, 178, 130)
print(Lucas.name, Lucas.age, Lucas.height, Lucas.weight)
Lucas.run()
Lucas.say()
Mark = Person("Mark", 24, 177, 150)
print(Mark.name, Mark.age, Mark.height, Mark.weight)
Mark.say()
