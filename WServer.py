import asyncio
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
        
        opt = option.get('command')
        
        args = option.get('message')

        output = comandos.get(opt)(*args)

        print("##########################")

        if option.get('command') == 'listar':

            msgstr = json.dumps(genlista(output))
        else:
            msgstr = json.dumps(output)
        
        await websocket.send(msgstr)
        
        
start_server = websockets.serve(opt, '10.54.218.167', '8765')

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
