from rthkdb.continuos import Continuos
import rethinkdb as rdb
import datetime
import os

# rt_host = os.environ['rt_host']
# rt_port = os.environ['rt_port']
# rt_db = os.environ['rt_db']

"""
>>> import datetime
>>> fmt = '%Y.%m.%d'
>>> s = '2019.06.04'
>>> dt = datetime.datetime.strptime(s, fmt)
>>> dt
datetime.datetime(2019, 6, 4, 0, 0)
>>> tt = dt.timetuple()
>>> tt.tm_yday
155
"""

def genlista(output):
      vector = []
      # print('output [listar.pr:13]', type(output), output)
      for kdic in output:
          # print(f"kdic : {kdic}")
          salida = {}
          for k, v in kdic.items():
   
              if isinstance(v, datetime.date):
                  salida.update({k: str(v)[:-6]})
              elif isinstance(v, list):
                  salida.update({k: genlista(v)})
              else:
                  salida.update({k: v})
          vector.append(salida)
      return vector

def getlista(kw):

    r=rdb.RethinkDB()
    con = Continuos()

    if kw['message'].get('order'):
        print(f"kw XXX  : {kw['message']['order'].items()}")
    
    if kw['message'].get('order'):
        order = []
        
        for k,v in kw['message']['order'].items():
            order.append(getattr(r,v)(k))
        kw['message']['order']=order
    print(f'kw2: {kw}')
    dat = con.consultar(kw)
    del con
    return dat
    


if __name__ == "__main__":

    pass
