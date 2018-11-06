
import cProfile


def test():
    for i in range(1,100):
        f = i ** 2


if __name__ == "__main__":
    cProfile.run('test()')
