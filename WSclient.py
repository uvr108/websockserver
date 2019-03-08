import asyncio
import websockets
from funciones import comandos
import json
from Extraer.extraer import Extract 


async def opt():
    async with websockets.connect(
            'ws://10.54.218.195:8765') as websocket:


        while True:

            print(f'{[*comandos.keys()]} q: salir')
            option = input("Ingrese su opcion ? ")
 
            args=[]

            tipo = None

            if option == 'sumar':

                lis = input('ingrese lista de numeros : ')
                args=json.loads(lis)
                tipo="operator"

            elif option == 'multiplicar':

                lis = input('ingrese lista de numeros : ')
                args=json.loads(lis)
                tipo="operator"

            elif option == 'palabras':

                frase = input('ingrese su frase : ')
                args.append(frase)
                tipo="operator"

            elif option == 'q':

                break 

            elif option == 'sql':

                args=[]
                tipo = "sql"

            elif option == 'download':

                stations = ['VALN','LSCH']
                t1 = "2019-01-07T00:00:00+00:00"
                t2 = "2019-01-07T01:59:59+00:00"
                tipo = 'file'
                args = [stations, t1, t2]

                print("ARGS : ",args)

            elif option == 'listar':

                ######################################
                pluck = ['code', 'fecha', 'item', 'monto', 'obs']
                msg = {'table': 'presupuesto', 'option': 'select', 'pluck' : pluck }
                kw = {'command': 'listar', 'message': msg}
                ######################################
                tipo = 'rethink'
                args.append(kw)

            msg = json.dumps({"command": option, "tipo": tipo, "message": args})

            print(f"{msg}")
            await websocket.send(msg)
            print(f"> {option}")

             
            greeting = await websocket.recv()
            print(f"< {greeting}")
            
           
asyncio.get_event_loop().run_until_complete(opt())
