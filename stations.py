from orm_collector.manager import SessionCollector

from networktools.colorprint import bprint, gprint, rprint

import pyproj


def obtener():
    out = [] 
    s=SessionCollector()
    station = s.get_stations() 

    ecef = pyproj.Proj(proj='geocent', ellps='WGS84', datum='WGS84')
    lla = pyproj.Proj(proj='latlong', ellps='WGS84', datum='WGS84')
    
    for s in station:
                
        lon, lat, alt = pyproj.transform(ecef, lla, float(s.position_x),float(s.position_y),float(s.position_z), radians=False)
               
        stat = {"command":"enviar","code":s.code,"name":s.name, "x":lon, "y":lat, "z":alt, "check": False}
        msg = {"stream":'testws','payload':stat}
        out.append(msg)

    return out 



if __name__ == "__main__":
    
    for o in obtener():
        print(o)


