import asyncio
import websockets
from funciones import comandos
import json
import rethinkdb as r
from rethinkdb.errors import RqlRuntimeError
from rthkdb.continuos import Continuos

async def opt():
    async with websockets.connect(
            'ws://127.0.0.1:8765') as websocket:


        while (1):

            print(f'{[*comandos.keys()]}')

            option = input("Ingrese su opcion ? ")
 
            args=[]

            if option == 'sumar':
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
                where = {'action':'NEW'}
                indice = {'anomes':[2018,10]}
                order = 'sfile'
                distinct = None
                pluck = ['action','latitud','longitud','operador','m1_magnitud','no']
                get_all = {'flag':flag,'where': where, 'indice':indice, 'order':order,'pluck':pluck,'distinct': distinct }
                kw.update({'get_all':get_all})
                args.append(kw)
            elif option == 'salir':
               break

            msg = json.dumps({"command":option, "message":args})
            await websocket.send(msg)
            print(f"> {option}")

            greeting = await websocket.recv()
            print(f"< {greeting}")

asyncio.get_event_loop().run_until_complete(opt())
