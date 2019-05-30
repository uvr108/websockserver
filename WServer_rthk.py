import asyncio
import websockets
import datetime
import json
import os

from funciones import comandos
from listar import genlista

sk_host = os.environ['sk_host']
sk_port = 9999 

async def opt(websocket, path):

    while True:
        vector = []
        print("Empezando a recibir data")
        option = json.loads(await websocket.recv())
       
        # print('RECIVO : ',option)
 
        opt = option.get('command')
        tipo = option.get('tipo')
        args = option.get('message')

        # print("option : ", option)
        # print("tipo : " , tipo)
        # print("args : ", args)


        if tipo == 'rethink':
            kw = args[0] 
            # print(f'kw [WServer_rthk:33]', type(kw),kw)
            
            output = await comandos.get(opt)(kw)
            # for o in output:
            #     print('WServer:36',type(output),o)
            msgstr = json.dumps(genlista(output))
            # print('msgstr [listar.py:37]', msgstr)

        await websocket.send(msgstr)

 
start_server = websockets.serve(opt, sk_host, sk_port)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

