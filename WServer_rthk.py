import asyncio
# import nest_asyncio
import websockets
import datetime
import json
import os

from funciones import comandos
from listar import genlista

async def opt(websocket, path):

    while True:
        vector = []
        print("Empezando a recibir data")
        option = json.loads(await websocket.recv())
       
        print('RECIVO : ',option)
 
        opt = option.get('command')
        tipo = option.get('tipo')
        args = option.get('message')

        print("option tipo args : ", option, tipo, args)


        if tipo == 'rethink': 
            output = await comandos.get(opt)(*args)
            msgstr = json.dumps(genlista(output))

        await websocket.send(msgstr)

 
start_server = websockets.serve(opt, '10.54.218.195', '8765')

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

