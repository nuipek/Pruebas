import pycrs

if __name__ == '__main__':
    esri_wkt = 'PROJCS["World_Robinson",GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137,298.257223563]],PRIMEM["Greenwich",0],UNIT["Degree",0.017453292519943295]],PROJECTION["Robinson"],PARAMETER["False_Easting",0],PARAMETER["False_Northing",0],PARAMETER["Central_Meridian",0],UNIT["Meter",1]]'
    crs = pycrs.parse.from_esri_wkt(esri_wkt)
    epsg = pycrs.utils.wkt_to_epsg(crs.to_esri_wkt())
    print(crs)
    print(isinstance(crs, pycrs.CS))
    # value = crs.to_epsg_code()
    pass