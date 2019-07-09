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

    data = mostra["message"]
    key = data[0].keys()

    fec = time.time()
 
    f = open('/var/ftp/pub/%s.csv' % fec, 'w')
    
    f.write(f'{"|".join(key)}\n') 
 
    for d in data:
        myList = (str(d[k]) for k in key)
        myString = '|'.join(myList )
        f.write(f'{myString}\n')

    f.close() 

    

    """
    di = 'mostra'

    fieldname = ['zona','fecha_origen','sfile','latitud','longitud','no','cont_5','cont_10','cont_15','cont_20'] 

    with open('/var/ftp/pub/%s.csv' % di, 'w') as csvfile:

       writer = csv.DictWriter(csvfile, fieldnames=fieldname)

       writer.writeheader()
       writer.writerow(data)

       # for d in data:
       #     print(d)
       #     writer.writerow(data[d])
       # salida = "%s.csv" % data
 
    csvfile.close()    

    """

    """
        return {'creating':'archive'}


        print("zip  %s/%s/%s.zip  : " % (filedir,di))
 
        zf = zipfile.ZipFile("%s/%s.zip" % (filedir, di), mode='w')

        dir_ = '%s/%s' % (filedir, di)
 
        for d in data: 
            print('adding %s_%s.csv' % (dir_, d))
            zf.write('%s_%s.csv' % (dir_, d), basename('%s_%s.csv' % (dir_, d)))
    
        print('closing')
        zf.close()
        return "%s.zip" % di

    """

    return {'filedir': '%s.csv' % fec}



if __name__ == "__main__":

    
    station = ['VALN','PVCA']
    filedir = os.environ['RDB_FILEDIR']
    di = "2019-01-07T00:00:00+00:00"
    df = "2019-01-07T01:59:59+00:00"

    print(bajar(station,filedir,di,df))
