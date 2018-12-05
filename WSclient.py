import asyncio
import websockets
from funciones import comandos
import json

async def opt():
    async with websockets.connect(
            'ws://localhost:8765') as websocket:
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
        msg = json.dumps({option:args})
        await websocket.send(msg)
        print(f"> {option}")

        greeting = await websocket.recv()
        print(f"< {greeting}")

asyncio.get_event_loop().run_until_complete(opt())
