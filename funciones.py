from functools import reduce
from rthkdb.continuos import Continuos
import rethinkdb as r
import os

rt_host=os.environ['rt_host']
rt_port=os.environ['rt_port']
rt_db=os.environ['rt_db']

def sumar(*lista):
    # print('lista : ',lista)
    return sum(lista) 

def multiplicar(*lista):
    mult = lambda a,b:a*b
    return reduce(mult,lista)    

def palabras(frase):
    pl = frase.split()
    return len(pl)

def listar(kw):
   
    cons=Continuos()
    conn = r.connect(host=rt_host, port=rt_port, db=rt_db)
    data = cons.ejecutar(r,**kw)
    conn.close()
    cons.__del__()
    return data

comandos = { 'sumar': sumar, 'multiplicar': multiplicar, 'palabras': palabras, 'listar': listar }



