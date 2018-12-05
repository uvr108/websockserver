import asyncio
import websockets
import sys
import json
from funciones import comandos

async def opt(websocket, path):
    #option = await websocket.recv()
    option=json.loads(await websocket.recv())
    opt = [*option.keys()][0] 
    args=[] 
    if opt in ['sumar','multiplicar']:
        args = [*option.values()][0] 
    elif opt == 'palabras':
        args.append(option[opt][0])

    print(f"< {opt} {args}")
    output = comandos.get(opt)(*args)

    msgstr = json.dumps({'respuesta':output}) 

    await websocket.send(msgstr)

start_server = websockets.serve(opt, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

