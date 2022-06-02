from multiprocessing import Pool, freeze_support
import testLib

from classeTeste import Classe

def main():

    a = Classe(2)
    b = Classe(2.005)
    c = 5
    d = 5
    e = 7
    lista = [1, 2, 3, 4]
    flag = True

    with Pool() as pool:
        S = pool.starmap(testLib.test_equal,
                         [('foo'.upper(), 'FOO'),
                          (lista[0], 1),
                          (flag, True),
                          ])


if __name__ == "__main__":
    testLib.init()
    freeze_support()
    main()
    testLib.end()
#   testLib.about()
#   testLib.sos()

