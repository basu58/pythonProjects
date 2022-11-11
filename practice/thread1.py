import os
import threading


def square(num):
    print(threading.current_thread().name)
    print(os.getpid())
    print(num ** 2)


def cube(num):
    print(threading.current_thread().name)
    print(os.getpid())
    print(num ** 3)


if __name__ == "__main__":
    print(threading.current_thread().name)
    print(os.getpid())
    t1 = threading.Thread(target=square, args=(10,))
    t2 = threading.Thread(target=cube, args=(10,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('done')
