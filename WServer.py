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


        if tipo == 'sql':
            output = await comandos.get(opt)(*args)
            msgstr = json.dumps(genlista(output))

        elif tipo == 'file':
           
            print('ARGS : ',args)
            
            # nest_asyncio.apply()
           
            station = args[0] 
            filedir = os.environ['RDB_FILEDIR']
            di = args[1]
            df = args[2]
 
            output = await comandos.get(opt)(station,filedir,di,df)
            msgstr =  json.dumps(output) 
        
        await websocket.send(msgstr)

 
start_server = websockets.serve(opt, '10.54.218.195', '8765')

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

