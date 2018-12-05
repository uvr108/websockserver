from functools import reduce

def sumar(*lista):
    return sum(lista) 

def multiplicar(*lista):
    mult = lambda a,b:a*b
    return reduce(mult,lista)    

def palabras(frase):
    pl = frase.split()
    return len(pl)


comandos = { 'sumar': sumar, 'multiplicar': multiplicar, 'palabras': palabras }



