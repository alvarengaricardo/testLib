'''
Experimento OK
'''
from multiprocessing import Pool, freeze_support
from time import perf_counter
from func import somar, multiplicar
#from testLib import testAssert
import testLib
import classeTeste

c1 = classeTeste.Cubo(1)
print(c1.volume)

c2 = classeTeste.Cubo(2)
print(c2.volume)

def main():
    with Pool() as pool:
        C = pool.starmap(testLib.testAssert,
                         [(classeTeste.Cubo, 1, 1, 2),
                          (somar, 1, 2, 3),
                          (somar, 1, 3, 4),
                          (somar, 1, 4, 5),
                          (somar, 1, 5, 6),
                          (somar, 2, 1, 3),
                          (somar, 2, 2, 4),
                          (somar, 2, 3, 5),
                          (somar, 2, 4, 6),
                          (somar, 2, 5, 7),
                          (somar, 3, 1, 4),
                          (somar, 3, 2, 5),
                          (somar, 3, 3, 6),
                          (somar, 3, 4, 7),
                          (somar, 3, 5, 8),
                          (somar, 4, 1, 5),
                          (somar, 4, 2, 6),
                          (somar, 4, 3, 7),
                          (somar, 4, 4, 8),
                          (somar, 4, 5, 9),
                          (somar, 5, 1, 6),
                          (somar, 5, 2, 7),
                          (somar, 5, 3, 8),
                          (somar, 5, 4, 9),
                          (somar, 5, 5, 10),
                          (somar, 6, 1, 7),
                          (somar, 6, 2, 8),
                          (somar, 6, 3, 9),
                          (somar, 6, 4, 10),
                          (somar, 6, 5, 10),
                          ])
        M = pool.starmap(testLib.testAssert,
                         [(multiplicar, 1, 1, 1),
                          (multiplicar, 2, 2, 4),
                          ])


if __name__ == "__main__":
    start = perf_counter()
    testLib.init()
    freeze_support()
    main()
    testLib.end()
    finish = perf_counter()
    print(f'Finished in {round(finish - start, 3)} second(s)')

