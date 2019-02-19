from functools import reduce
from stations import obtener
from listar import getlista

def sumar(*lista):
    print('lista : ',lista)
    sum = lambda a, b: a+b
    return reduce(sum, lista) 

def multiplicar(*lista):
    mult = lambda a, b: a*b
    return reduce(mult, lista)


def palabras(frase):
    pl = frase.split()
    return len(pl)

def sql():

    return obtener() 

def listar(kw):

    return getlista(kw) 

comandos = {'sumar': sumar, 'multiplicar': multiplicar, 'palabras': palabras, 'listar': listar, 'sql':sql}



