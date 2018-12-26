class Person():

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 0 or age > 100:
            print("please input correct age！")
        else:
            self.__age = age


per = Person("Lucas", 24)
per.age = 20
print(per.age)

