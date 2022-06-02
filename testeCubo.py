from multiprocessing import Pool, freeze_support
from classeTeste import Cubo
import testLib

def main():

    c1 = Cubo(1)
    c2 = Cubo(2)
    c3 = Cubo(3)

    print(c1.volume)

    with Pool() as pool:
        S = pool.starmap(testLib.testEqual,
                         [(c1.volume, 1),
                          (c2.volume, 8),
                          (c3.volume, 27),
                          ])


if __name__ == "__main__":
    testLib.init()
    freeze_support()
    main()
    testLib.end()


