import functools


def outer(func):
    def inner():
        print("first")
        func()

    return inner


@outer
def func1():
    print("second")


func1()


# 通用装饰器
def enhance(func):
    def enhanceSay(*args, **kwargs):
        print("**********")
        func(*args, **kwargs)

    return enhanceSay


@enhance
def say(name):
    print("%s is a good man" % (name))


say("Lucas")

# def person(name, age):
#     print("name is %s, age is %s" % (name, age))
#
#
# person("Lucas", "24")
# person1 = functools.partial(person, age="100")
# person1("Lucas")
