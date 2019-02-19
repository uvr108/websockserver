import asyncio
import websockets
from funciones import comandos
import json


async def opt():
    async with websockets.connect(
            'ws://10.54.218.167:8765') as websocket:


        while True:

            print(f'{[*comandos.keys()]} q: salir')
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
            elif option == 'q':
                break 
            elif option == 'sql':
                args=[]
            elif option == 'listar':

                tabla = input('ingrese tabla : ')

                pluck = ['code', 'fecha', 'item', 'monto', 'obs']
                
                msg = {'table': tabla, 'option': 'select', 'pluck' : pluck } 

                kw = {'command': 'listar', 'message': msg}

                args.append(kw)
 

            msg = json.dumps({"command": option, "message": args})

            print(f"{msg}")


            await websocket.send(msg)
            print(f"> {option}")

            greeting = await websocket.recv()
            print(f"< {greeting}")

asyncio.get_event_loop().run_until_complete(opt())
