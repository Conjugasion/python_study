class Person(object):
    name = "Lucas"
    age = 24
    height = 178
    weight = 130

    def run(self):
        print("I am running")

    def eat(self, food):
        print("eat" + food)


Lucas = Person()
Person.name = "Mark"
print(Lucas.name)
Lucas.eat("苹果")

Mark = Person()
print(Mark.name)
