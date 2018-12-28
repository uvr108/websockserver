from funciones import comandos
import json

import rethinkdb as r
from rethinkdb.errors import RqlRuntimeError
from rthkdb.continuos import Continuos


def main():

    print(f'{[*comandos.keys()]}')

    while 1:

        args = []
        option = input('Ingrese opcion : ')
        print(f'Su opcion es {option}')

        if option == 'salir':
            break
        elif option == 'sumar':
            lis = input('ingrese lista de numeros : ')
            args = json.loads(lis)
        elif option == 'multiplicar':
            lis = input('ingrese lista de numeros : ')
            args = json.loads(lis)
        elif option == 'palabras':
            frase = input('ingrese su frase : ')
            args.append(frase)
        elif option == 'listar':
            tabla = input('ingrese tabla : ')
            flag = None
            where = None
            between = {'initial': '2000-11-01T00:00:00+00:00', 'final': '2019-11-01T23:59:59+00:00', 'index': 'fecha'}
            order = 'obs'
            distinct = 1
            pluck = ['code', 'monto', 'obs', 'fecha', 'item']
            kw = {'table': tabla, 'command': 'select', 'between': between, 'flag': flag, 'where': where, 'order': order, 'pluck': pluck, 'distinct': distinct}
            args.append(kw)
            print(f"args : {args}")
        for res in comandos.get(option)(*args):
            print(f"res : {res}")


if __name__ == "__main__":

    main()
