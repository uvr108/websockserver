import asyncio
import websockets
from funciones import comandos
import json


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

                flag = ''
                where = {}
                order = 'code'
                distinct = None
                fecha_ini = '2000-11-01T00:00:00+00:00'
                fecha_fin = '2019-11-01T23:59:59+00:00'
                between = {'initial': fecha_ini, 'final': fecha_fin, 'index': 'fecha'}
                pluck = ['code', 'fecha', 'monto', 'item', 'obs']
                kw = {'table': tabla, 'command': 'select', 'flag': flag, 'where': where, 'order': order, 'pluck': pluck, 'between': between,
                                    'distinct': distinct}

                kw = {'command': 'listar', 'message': kw}

                args.append(kw)

            else:
               break

            msg = json.dumps({"command": option, "message": args})

            print(f"{msg}")


            await websocket.send(msg)
            print(f"> {option}")

            greeting = await websocket.recv()
            print(f"< {greeting}")

asyncio.get_event_loop().run_until_complete(opt())
