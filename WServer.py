import asyncio
import websockets
import sys
import datetime
import json
from funciones import comandos

async def opt(websocket, path):
    #option = await websocket.recv()

    while True:
        vector=[]
        print("Empezando a recibir data")
        option=json.loads(await websocket.recv())
        # print('option : ',option,type(option),[*option.keys()],[*option.values()])
        opt = option.get('command')
        args=[] 
        if opt in ['sumar','multiplicar']:
            args = option.get('message') 
        elif opt in ['palabras','listar']:
            # print(f"< {opt} {args}")
            args.append(option.get('message'))

        # print(f"< {opt} {args}")
        output = comandos.get(opt)(*args)
        # print(output)
        # print("############################") 
        id=0
        for kdic in output:
            # print(f"kdic : {kdic}")
            salida = {}
            for k,v in kdic.items():
                id+=1    
                if isinstance(v, datetime.date):
                    salida.update({k:str(v)[:-6]})
                else:
                    salida.update({k:v})
            # print(f"salida : {salida}")
            vector.append(salida)   
        # print("##########################") 
        # print(f" vector : {vector}")
        
        msgstr = json.dumps(vector) 

        # print(f"> yyyy {msgstr}")

        await websocket.send(msgstr)
        
start_server = websockets.serve(opt, '10.54.218.19', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

