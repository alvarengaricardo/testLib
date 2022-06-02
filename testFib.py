from multiprocessing import Pool, freeze_support
from func import fib
import testLib

def main():

    with Pool() as pool:

        a = pool.starmap(testLib.test_func,
                         [(fib, 15, '', 610),
                          ])


if __name__ == "__main__":
    testLib.init()
    freeze_support()
    main()
    testLib.end()

'''
 F = pool.starmap(testLib.testFunc,
                         [(fib, 15, '', 610),
                          (fib, 20, '', 6765),
                          (fib, 25, '', 75025),
                          (fib, 30, '', 832040),
                          (fib, 35, '', 9227465),
                          (fib, 36, '', 14930352),
                          (fib, 37, '', 24157817),
                          (fib, 38, '', 39088169),
                          (fib, 39, '', 63245986),
                          (fib, 40, '', 102334155),
                          ])

'''