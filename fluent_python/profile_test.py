def func1():
    for i in range(1000):
        print("i love python")


def func2():
    for i in range(10):
        print("i love c++")
    func3()


def func3():
    for i in range(100):
        print("i love java")


def main():
    func1()
    func2()


if __name__ == "__main__":
    main()
