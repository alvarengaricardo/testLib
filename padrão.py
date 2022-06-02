from multiprocessing import Pool, freeze_support
from func import somar, multiplicar
import testLib

def main():
    with Pool() as pool:
        S = pool.starmap(testLib.testFunc,
                         [(somar, 1, 1, 2),
                          ...
                          (somar, 6, 5, 10),
                          ])
        M = pool.starmap(testLib.testFunc,
                         [(multiplicar, 1, 1, 1),
                          ...
                          (multiplicar, 2, 2, 4),
                          ])
 if __name__ == "__main__":
    testLib.init()
    freeze_support()
    main()
    testLib.end()
