import matplotlib.pyplot as plt
import numpy as np


def plot_1():
    # plt.plot([1, 5, 7],[2,3,4], 'bo-')

    x = range(2, 7)
    y = range(5)
    plt.plot(x, y, 'k^--')

    plt.show()


def plot_2():
    for x in range(-10, 11):
        y = x**2
        plt.plot(x, y, 'ro')
    plt.show()


def plot_3():
    x = np.arange(-10, 11, 0.5)
    plt.plot(x, x**2, 'ro')
    plt.show()


def plot_4():  # 여러 그래프 겹쳐 그릴 때
    x = np.arange(0.1, 5, 0.1)

    plt.plot(x, np.log(x), 'r')
    plt.plot(x, -np.log(x), 'g')
    plt.plot(-x, np.log(x), 'b')
    plt.plot(-x, -np.log(x), 'y')
    plt.show()


def plot_5():
    x = np.arange(0.1, 5, 0.1)

    plt.subplot(2, 2, 1)
    plt.plot(x, np.log(x), 'r')

    plt.subplot(2, 2, 2)
    plt.plot(x, -np.log(x), 'g')

    plt.figure(figsize=[5, 10])
    plt.subplot(2, 2, 3)
    plt.plot(-x, np.log(x), 'b')

    plt.subplot(2, 2, 4)
    plt.plot(-x, -np.log(x), 'y')
    plt.show()


def plot_6():
    men = [34, 21, 43, 50, 47]
    women = [43, 53, 28, 39, 41]

    x = np.arange(len(men))

    plt.bar(x, men, width=0.45)
    plt.bar(x+0.45, women, width=0.45)
    plt.xticks(x+0.22, ['a', 'b', 'c', 'd', 'e'])
    plt.show()


# plot_1()
# plot_2()
# plot_3()
# plot_4()
# plot_5()
plot_6()
