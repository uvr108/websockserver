import asyncio
import websockets
import datetime
import json
import os

from funciones import comandos
from listar import genlista

wsk_host = os.environ['wsk_host']
wsk_port = os.environ['wsk_port'] 

async def opt(websocket, path):

    while True:
        vector = []
        print("Empezando a recibir data")
        option = json.loads(await websocket.recv())
       
        # print('RECIVO : ',option)
 
        opt = option.get('command')
        tipo = option.get('tipo')
        kw = option.get('message')

        # print("opt : ", opt)
        # print("tipo : " , tipo)
        # print("kw : ", kw)

        output = await comandos.get(opt)({'message':kw})

        if tipo == 'rethink':

            msgstr = json.dumps(genlista(output))

        elif tipo == 'csv':

            msgstr = json.dumps(output)

        await websocket.send(msgstr)

 
start_server = websockets.serve(opt, wsk_host, wsk_port)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

