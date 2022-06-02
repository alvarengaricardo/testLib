'''
Funções de teste com saida em arquivo.
'''

import os
import testLibAux

def test_func(ff, a, b, expected):
    if b != '':
        received = ff(a, b)
    else:
        received = ff(a)
    line = testLibAux.line2(ff, a, b, expected, received)
    if received == expected:
        line = line + 'Pass'
        ft = open('filetot.txt', 'a')
        ft.write(line + '\n')
        fp = open('filepass.txt', 'a')
        fp.write(line + '\n')
        print(line)
    else:
        line = line + 'Fail'
        ft = open('filetot.txt', 'a')
        ft.write(line + '\n')
        ff = open('filefail.txt', 'a')
        ff.write(line + '\n')
        print(line)


def test_not_func(ff, a, b, expected):
    if b != '':
        received = ff(a, b)
    else:
        received = ff(a)
    line = testLibAux.line2(ff, a, b, expected, received)
    if received != expected:
        line = line + 'Pass'
        ft = open('filetot.txt', 'a')
        ft.write(line + '\n')
        fp = open('filepass.txt', 'a')
        fp.write(line + '\n')
        print(line)
    else:
        line = line + 'Fail'
        ft = open('filetot.txt', 'a')
        ft.write(line + '\n')
        ff = open('filefail.txt', 'a')
        ff.write(line + '\n')
        print(line)


def test_equal(a, b):
    line = testLibAux.line(a, b)
    if a == b:
        line = line + 'Pass'
        ft = open('filetot.txt', 'a')
        ft.write(line + '\n')
        fp = open('filepass.txt', 'a')
        fp.write(line + '\n')
        print(line)
    else:
        line = line + 'Fail'
        ft = open('filetot.txt', 'a')
        ft.write(line + '\n')
        ff = open('filefail.txt', 'a')
        ff.write(line + '\n')
        print(line)


def test_not_equal(a, b):
    line = testLibAux.line(a, b)
    if a != b:
        line = line + 'Pass'
        ft = open('filetot.txt', 'a')
        ft.write(line + '\n')
        fp = open('filepass.txt', 'a')
        fp.write(line + '\n')
        print(line)
    else:
        line = line + 'Fail'
        ft = open('filetot.txt', 'a')
        ft.write(line + '\n')
        ff = open('filefail.txt', 'a')
        ff.write(line + '\n')
        print(line)


def test_is(a, b):
    line = testLibAux.line(a, b)
    if a is b:
        line = line + 'Pass'
        ft = open('filetot.txt', 'a')
        ft.write(line + '\n')
        fp = open('filepass.txt', 'a')
        fp.write(line + '\n')
        print(line)
    else:
        line = line + 'Fail'
        ft = open('filetot.txt', 'a')
        ft.write(line + '\n')
        ff = open('filefail.txt', 'a')
        ff.write(line + '\n')
        print(line)


def test_is_not(a, b):
    line = testLibAux.line(a, b)
    if a is not b:
        line = line + 'Pass'
        ft = open('filetot.txt', 'a')
        ft.write(line + '\n')
        fp = open('filepass.txt', 'a')
        fp.write(line + '\n')
        print(line)
    else:
        line = line + 'Fail'
        ft = open('filetot.txt', 'a')
        ft.write(line + '\n')
        ff = open('filefail.txt', 'a')
        ff.write(line + '\n')
        print(line)


def test_in(a, b):
    line = testLibAux.line(a, b)
    if a in b:
        line = line + 'Pass'
        ft = open('filetot.txt', 'a')
        ft.write(line + '\n')
        fp = open('filepass.txt', 'a')
        fp.write(line + '\n')
        print(line)
    else:
        line = line + 'Fail'
        ft = open('filetot.txt', 'a')
        ft.write(line + '\n')
        ff = open('filefail.txt', 'a')
        ff.write(line + '\n')
        print(line)


def test_not_in(a, b):
    line = testLibAux.line(a, b)
    if a not in b:
        line = line + 'Pass'
        ft = open('filetot.txt', 'a')
        ft.write(line + '\n')
        fp = open('filepass.txt', 'a')
        fp.write(line + '\n')
        print(line)
    else:
        line = line + 'Fail'
        ft = open('filetot.txt', 'a')
        ft.write(line + '\n')
        ff = open('filefail.txt', 'a')
        ff.write(line + '\n')
        print(line)


def test_almost_equal(a, b, c):
    # testa se o arredondamendo de a-b com c casas decimais é zero
    line = testLibAux.line(a, b)
    if round(a - b, c) == 0:
        line = line + 'Pass'
        ft = open('filetot.txt', 'a')
        ft.write(line + '\n')
        fp = open('filepass.txt', 'a')
        fp.write(line + '\n')
        print(line)
    else:
        line = line + 'Fail'
        ft = open('filetot.txt', 'a')
        ft.write(line + '\n')
        ff = open('filefail.txt', 'a')
        ff.write(line + '\n')
        print(line)


def test_not_almost_equal(a, b, c):
    line = testLibAux.line(a, b)
    if round(a - b, c) != 0:
        line = line + 'Pass'
        ft = open('filetot.txt', 'a')
        ft.write(line + '\n')
        fp = open('filepass.txt', 'a')
        fp.write(line + '\n')
        print(line)
    else:
        line = line + 'Fail'
        ft = open('filetot.txt', 'a')
        ft.write(line + '\n')
        ff = open('filefail.txt', 'a')
        ff.write(line + '\n')
        print(line)

def test_greater(a, b):
    line = testLibAux.line(a, b)
    if a > b:
        line = line + 'Pass'
        ft = open('filetot.txt', 'a')
        ft.write(line + '\n')
        fp = open('filepass.txt', 'a')
        fp.write(line + '\n')
        print(line)
    else:
        line = line + 'Fail'
        ft = open('filetot.txt', 'a')
        ft.write(line + '\n')
        ff = open('filefail.txt', 'a')
        ff.write(line + '\n')
        print(line)


def test_greater_equal(a, b):
    line = testLibAux.line(a, b)
    if a >= b:
        line = line + 'Pass'
        ft = open('filetot.txt', 'a')
        ft.write(line + '\n')
        fp = open('filepass.txt', 'a')
        fp.write(line + '\n')
        print(line)
    else:
        line = line + 'Fail'
        ft = open('filetot.txt', 'a')
        ft.write(line + '\n')
        ff = open('filefail.txt', 'a')
        ff.write(line + '\n')
        print(line)

def test_less(a, b):
    line = testLibAux.line(a, b)
    if a < b:
        line = line + 'Pass'
        ft = open('filetot.txt', 'a')
        ft.write(line + '\n')
        fp = open('filepass.txt', 'a')
        fp.write(line + '\n')
        print(line)
    else:
        line = line + 'Fail'
        ft = open('filetot.txt', 'a')
        ft.write(line + '\n')
        ff = open('filefail.txt', 'a')
        ff.write(line + '\n')
        print(line)


def test_less_equal(a, b):
    line = testLibAux.line(a, b)
    if a <= b:
        line = line + 'Pass'
        ft = open('filetot.txt', 'a')
        ft.write(line + '\n')
        fp = open('filepass.txt', 'a')
        fp.write(line + '\n')
        print(line)
    else:
        line = line + 'Fail'
        ft = open('filetot.txt', 'a')
        ft.write(line + '\n')
        ff = open('filefail.txt', 'a')
        ff.write(line + '\n')
        print(line)



'''
Funções abaixo com problema de implementação, Bool não é iterável

def test_true(a, b):
    line = testLibAux.line(a)
    if bool(a):
        line = line + 'Pass'
        ft = open('filetot.txt', 'a')
        ft.write(line + '\n')
        fp = open('filepass.txt', 'a')
        fp.write(line + '\n')
        print(line)
    else:
        line = line + 'Fail'
        ft = open('filetot.txt', 'a')
        ft.write(line + '\n')
        ff = open('filefail.txt', 'a')
        ff.write(line + '\n')
        print(line)

def test_false(a):
    line = testLibAux.line(a)
    if not bool(a):
        line = line + 'Pass'
        ft = open('filetot.txt', 'a')
        ft.write(line + '\n')
        fp = open('filepass.txt', 'a')
        fp.write(line + '\n')
        print(line)
    else:
        line = line + 'Fail'
        ft = open('filetot.txt', 'a')
        ft.write(line + '\n')
        ff = open('filefail.txt', 'a')
        ff.write(line + '\n')
        print(line)
'''

## Estrutura função de teste
'''
def "funcao"(a, b):
    line = testLibAux.line(a, b)
    if "condicao":
        line = line + 'Pass'
        ft = open('filetot.txt', 'a')
        ft.write(line + '\n')
        fp = open('filepass.txt', 'a')
        fp.write(line + '\n')
        print(line)
    else:
        line = line + 'Fail'
        ft = open('filetot.txt', 'a')
        ft.write(line + '\n')
        ff = open('filefail.txt', 'a')
        ff.write(line + '\n')
        print(line)

'''


## Funções não de teste


'''
    ft = open('filetot.txt', 'w')
    fp = open('filepass.txt', 'w')
    ff = open('filefail.txt', 'w')
    ft.close()
    fp.close()
    ff.close()
    
'''


def end():
    if os.path.exists('filetot.txt'):
        with open('filetot.txt') as f:
            tl = len(f.readlines())
            print('Total: ' + str(tl))
            ft = open('filetot.txt', 'a')
            ft.write('\n')
            ft.write('Total: ' + str(tl))
            ft.close()
    if os.path.exists('filepass.txt'):
        with open('filepass.txt') as f:
            tl = len(f.readlines())
            print('Passed: ' + str(tl))
            fp = open('filepass.txt', 'a')
            fp.write('\n')
            fp.write('Passed: ' + str(tl))
            fp.close()
    if os.path.exists('filefail.txt'):
        with open('filefail.txt') as f:
            tl = len(f.readlines())
            print('Failed: ' + str(tl))
            ff = open('filefail.txt', 'a')
            ff.write('\n')
            ff.write('Failed: ' + str(tl))
            ff.close()

def init():
    if os.path.exists('filetot.txt'):
        os.remove('filetot.txt')
        print("removido filetot.txt")
    else:
        print("filetot.txt does not exist")

    if os.path.exists('filepass.txt'):
        os.remove('filepass.txt')
        print("removido filefail.txt")
    else:
        print("filepass.txt does not exist")

    if os.path.exists('filefail.txt'):
        os.remove('filefail.txt')
        print("removido filefail.txt")
    else:
        print("filefail.txt does not exist")

def about():
    print("Framework de Teste desenvolvido como dissertação de Mestrado")
    print("Autor: Ricardo Ribeiro de Alvarenga")
    print("ITA - Instituto Tecnologico de Aeronáutica")


# nome provisório, melhorar isso
def sos():
    print("Aqui será exibida a relação de funções implementadas, seus objetivos e parâmetros.")
