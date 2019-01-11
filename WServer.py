import asyncio
import websockets
import datetime
import json
from funciones import comandos


async def opt(websocket, path):
    # option = await websocket.recv()

    def genlista(output):
        vector = []
        for kdic in output:
            # print(f"kdic : {kdic}")
            salida = {}
            for k, v in kdic.items():

                if isinstance(v, datetime.date):
                    salida.update({k: str(v)[:-6]})
                elif isinstance(v, list):
                    salida.update({k: genlista(v)})
                else:
                    salida.update({k: v})
                    # print(f"salida : {salida}")
            vector.append(salida)
        return vector


    while True:
        vector = []
        print("Empezando a recibir data")
        option = json.loads(await websocket.recv())
        # print('option : ', option, type(option), [*option.keys()], [*option.values()])
        opt = option.get('command')
        args = []
        if opt in ['sumar', 'multiplicar']:
            args = option.get('message') 
        elif opt in ['palabras', 'listar']:
            # print(f"< {opt} {args}")
            args.append(option.get('message'))

        # print(f"< {opt} {args}")
        output = comandos.get(opt)(*args)
        # print(output)
        # print("##########################")

        # for lista in genlista(output):
        #   print(f"lista : {lista}")

        msgstr = json.dumps(genlista(output))

        # print(f"> yyyy {msgstr}")

        await websocket.send(msgstr)
        
start_server = websockets.serve(opt, '127.0.0.1', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

