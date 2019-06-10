import asyncio
import websockets
import datetime
import json
import os

from funciones import comandos
from listar import genlista

sk_host = os.environ['sk_host']
sk_port = os.environ['sk_port'] 

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
        print("kw : ", kw)


        if tipo == 'rethink':

            output = await comandos.get(opt)({'message':kw})
            # print(f'output : {str(output)}')
            msgstr = json.dumps(genlista(output))

        await websocket.send(msgstr)

 
start_server = websockets.serve(opt, sk_host, sk_port)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

