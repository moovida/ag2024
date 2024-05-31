from pyqgis_scripting_ext.core import *

# necessary functions
def fromLatString(latString):
    sign = latString[0]
    latDegrees = float(latString[1:3])
    latMinutes = float(latString[4:6])
    latSeconds = float(latString[7:9])
    lat = latDegrees + latMinutes/60 + latSeconds/3600
    if sign == '-':
        lat = lat * -1
    return lat

def fromLonString(lonString):
    sign = lonString[0]
    lonDegrees = float(lonString[1:4])
    lonMinutes = float(lonString[5:7])
    lonSeconds = float(lonString[8:10])
    lon = lonDegrees + lonMinutes/60 + lonSeconds/3600
    if sign == '-':
        lon = lon * -1
    return lon
    
    
# script starts here

folder = "/Users/hydrologis/development/ag2024"
tmpFolder = f"{folder}/tmp/"

stationsPath = f"{folder}/data/stations.txt"

with open(stationsPath, 'r') as file:
    lines = file.readlines()

schema = {
    "stationdid": "int",
    "name": "string",
    "country": "string",
    "height": "double"
}
stationsLayer = HVectorLayer.new("stations", "Point", \
                                 "EPSG:4326", schema)
for line in lines:
    line = line.strip()
    
    if not line.startswith("#"):
        lineSplit = line.split(",")
        latString = lineSplit[3]
        lonString = lineSplit[4]
        lat = fromLatString(latString)
        lon = fromLonString(lonString)
        
        point = HPoint(lon, lat)
        
        attributes = [
            int(lineSplit[0]),
            lineSplit[1],
            lineSplit[2],
            lineSplit[-1]
        ]
        
        stationsLayer.add_feature(point, attributes)
        

outputPath = f"{tmpFolder}/stations.gpkg"
error = stationsLayer.dump_to_gpkg(outputPath, overwrite=True)
if error:
    print(error)

dumpedStationsLayer = HVectorLayer.open(outputPath, "stations")
HMap.add_layer(dumpedStationsLayer)
    


