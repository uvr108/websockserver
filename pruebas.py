from funciones import comandos
import json

import rethinkdb as r
from rethinkdb.errors import RqlRuntimeError
from rthkdb.continuos import Continuos


def main():

    print(f'{[*comandos.keys()]}')


    args = []

    while (1):

        option = input('Ingrese opcion : ')
        print(f'Su opcion es {option}')

        if option == 'salir':
            break
        elif option == 'sumar':
            lis = input('ingrese lista de numeros : ')
            args=json.loads(lis)
        elif option == 'multiplicar':
            lis = input('ingrese lista de numeros : ')
            args=json.loads(lis) 
        elif option == 'palabras':
            frase = input('ingrese su frase : ')
            args.append(frase)
        elif option == 'listar':
            tabla = input('ingrese tabla : ')
            kw={'table':tabla}
            flag = ''
            where = {}
            indice = {'anomes':[2018,10]}
            order = 'sfile'
            distinct = None
            pluck = ['action','latitud','longitud','operador','m1_magnitud','no']
            get_all = {'flag':flag,'where': where, 'indice':indice, 'order':order,'pluck':pluck,'distinct': distinct }
            kw.update({'get_all':get_all})
            args.append(kw)

        res = comandos.get(option)(*args)
        print(f"{res}")

if __name__ == "__main__":

    main()


     
