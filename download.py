# from Extraer.extraer import Extract 
# from Extraer.extraer import mktkey
# from datetime import timedelta, datetime, timezone
import os
# from networktools.colorprint import bprint, gprint, rprint
import asyncio
import csv
import time

# tkey puede ser un intervalo o un punto
# dEBE ESTAR DEFINIDA VAEIABLE DE ENTORNO TMP_FILEDIR
# tkey = datetime.strptime("2018-05-03T00:00:00","%Y-%m-%dT%H:%M:%S")


def bajar(station,filedir,di,df):

    pass

    """
    ext = Extract(filedir, di, df )
    for st in station: 
        print(ext.ejecuta(st))
    return ext.genera_zip(station)
    del ext
    """

def genera_csv(mostra): 

    data = mostra["message"][1]
    key = data[0].keys()

    fec = mostra["message"][0]

    print(f'fec : {fec}') 
 
    f = open('/var/ftp/pub/%s.csv' % fec, 'w')
    
    f.write(f'{"|".join(key)}\n') 
 
    for d in data:
        myList = (str(d[k]) for k in key)
        myString = '|'.join(myList )
        f.write(f'{myString}\n')

    f.close() 

    return {'filedir': '%s.csv' % fec}



if __name__ == "__main__":

    
    station = ['VALN','PVCA']
    filedir = os.environ['RDB_FILEDIR']
    di = "2019-01-07T00:00:00+00:00"
    df = "2019-01-07T01:59:59+00:00"

    print(bajar(station,filedir,di,df))
