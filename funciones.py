from functools import reduce
# from stations import obtener
from listar import getlista
from download import bajar,genera_csv 

import asyncio
import os
import nest_asyncio

nest_asyncio.apply()

async def sumar(*lista):
    sum = lambda a, b: a+b
    return reduce(sum, lista) 


async def multiplicar(*lista):
    mult = lambda a, b: a*b
    return reduce(mult, lista)


async def palabras(frase):
    pl = frase.split()
    return len(pl)
"""
async def sql():

    return obtener() 
"""
async def listar(kw):
    return getlista(kw) 

async def download(station,filedir,di,df):
    
    return bajar(station,filedir,di,df)

async def download_mostra(mostra):

    return genera_csv(mostra)

""" comandos = {'sumar': sumar, 'multiplicar': multiplicar, 'palabras': palabras, 'listar': listar, 'sql':sql, 'download': download } """
comandos = {'sumar': sumar, 'multiplicar': multiplicar, 'palabras': palabras, 'listar': listar, 'download': download, 'download_mostra': download_mostra }


if __name__ == "__main__":


    #####################################
    v = [1,2,3,4]
    #####################################
    # args = [stations, t1, t2]

    station = ['VALN','PVCA']
    filedir = os.environ['RDB_FILEDIR']
    di = "2019-01-07T00:00:00+00:00"
    df = "2019-01-07T01:59:59+00:00"


    ######################################
    pluck = ['yr', 'jl', 'data']
    msg = {'table': 'ratio', 'option': 'select', 'limit':1,  'pluck' : pluck } 
    kw = {'command': 'listar', 'message': msg}
    ######################################

    loop = asyncio.get_event_loop()

    tasks = [  
        # asyncio.ensure_future(sumar(*v)),
        # asyncio.ensure_future(multiplicar(*v)),
        # asyncio.ensure_future(palabras('Hola Uli Como Estas')),
        # asyncio.ensure_future(sql()),
        asyncio.ensure_future(listar(kw)),
        # asyncio.ensure_future(download(station,filedir,di,df))
        ]
    loop.run_until_complete(asyncio.wait(tasks))  
    loop.close()







