
from multiprocessing import Pool, freeze_support
from func import somar
import testLib

def main():
    with Pool() as pool:
        S = pool.starmap(testLib.test_func,
                         [(somar, 1, 1, 2),
                          (somar, 1, 2, 3),
                          (somar, 1, 3, 4),
                          (somar, 1, 4, 5),
                          (somar, 1, 5, 6),
                          (somar, 2, 1, 3),
                          (somar, 2, 2, 4),
                          (somar, 2, 3, 5),
                          (somar, 2, 4, 6),
                          (somar, 2, 5, 7),
                          ])


if __name__ == "__main__":
    testLib.init()
    freeze_support()
    main()
    testLib.end()


