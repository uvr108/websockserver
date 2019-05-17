from rthkdb.continuos import Continuos
import rethinkdb as r
import datetime
import os

rt_host = os.environ['rt_host']
rt_port = os.environ['rt_port']
rt_db = os.environ['rt_db']


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

    # print(f"Estoy Listando : {kw}")
     
    conn = r.connect(host=rt_host, port=rt_port, db=rt_db)
    cons = Continuos(conn)
    data = cons.ejecutar(r,kw)
    cons.__del__()
    # conn.close()
    return data
    


if __name__ == "__main__":

    pass
