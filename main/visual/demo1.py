"""
@author Lucas
@date 2019/1/18 15:08

"""
import matplotlib.pyplot as plt
import numpy as np


def func1():
    x = np.linspace(0, 10, 10)
    plt.plot(x, x ** 2)
    plt.show()


def func2():
    x = np.arange(0, 10, 1)
    plt.plot(x, x ** 2)
    plt.plot(x, x / 2)
    plt.grad()
    plt.show()


def func3():
    x = np.arange(-np.pi, np.pi, 0.01)
    plt.plot(x, np.sin(x))
    plt.plot(x, np.cos(x))
    plt.grid(True)
    plt.show()


def func4():
    x = np.arange(-20, 20, 0.01)
    # 一行三列,第一个视图
    # 对象
    axes1 = plt.subplot(2, 3, 1)
    axes1.plot(x, np.sin(x))
    axes1.set_title("asdsd")
    # 网格线
    axes1.grid(color='r', linestyle='--', linewidth=2)

    axes2 = plt.subplot(1, 3, 2)
    axes2.plot(x, np.cos(x))

    axes3 = plt.subplot(1, 3, 3)
    axes3.plot(x, np.sin(x))
    plt.show()


def func5():
    # 坐标轴限制
    y = np.arange(0, 10, 1)
    print(y)
    plt.plot(y)
    plt.xlim(-2, 12)
    plt.xlim(2, 8)
    plt.show()


def func6():
    # 标题
    plt.title("line", fontsize=20, loc="left")
    x = np.arange(0, 10, 2)
    print(x)
    y = x ** 2 + 5
    plt.plot(x, y)
    plt.ylabel("y")
    plt.xlabel("x", size=20)
    plt.show()


def func7():
    x1 = np.random.randn(1000)
    x2 = np.random.randn(1000)
    x3 = np.random.randn(1000)
    # 累加和
    plt.plot(x1.cumsum(), label="x1", c='red')
    plt.plot(x2.cumsum(), label="x2", linestyle='-.')
    plt.plot(x3.cumsum(), label="x3", marker='^')
    plt.legend()
    # plt.savefig("func7.jpg")
    plt.show()


def func8():
    x = np.arange(0, 10, 1)
    print(type(x))
    plt.plot(x, x, x, 2 * x, x, x / 2)
    plt.legend(['slow', 'normal', 'fast'])
    plt.show()


def func9():
    x = np.arange(0, 10, 1)
    plt.plot(x, x, marker='o', label="y=x")
    plt.legend()
    plt.show()


def func10():
    # 坐标轴刻度
    x = np.random.randn(100)
    plt.plot(x.cumsum())
    plt.title("line", fontsize=20, loc="left")
    plt.xticks(np.linspace(0, 100, 5), list('ABCDE'))
    plt.yticks(np.linspace(-10, 10, 3), ['min', 0, 'max'], fontsize=20)

    plt.show()


def func11():
    # 直方图
    x = np.random.randint(0, 10, 10)
    print(x)
    plt.hist(x, density=True)
    plt.show()


def func12():
    # 条形图
    x = np.linspace(0, 5, 5)
    y = np.random.randint(0, 20, size=5)
    print(y)
    plt.bar(x, y)
    plt.show()


def func13():
    # 饼图
    x = np.array([0.7, 0.2, 0.1])
    plt.pie(x, labels=["dog", "cat", "other"], autopct='%1.2f%%')
    plt.show()


def func14():
    # 散点图
    x = np.random.randn(1000)
    y = np.random.randn(1000)
    plt.scatter(x, y, s=10)
    plt.show()


if __name__ == '__main__':
    func14()
