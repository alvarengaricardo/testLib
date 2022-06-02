from time import sleep

def somar(a, b):
    return a + b

def multiplicar(a, b):
    #print('Multiplicando: ', a, b)
    #sleep(a)
    return a * b

def triplo(a):
    return a * 3

def fib(n):
    if n < 2:
        return n
    return fib(n - 2) + fib(n - 1)


