from pyqgis_scripting_ext.core import *

folder = "/Users/hydrologis/development/ag2024"

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

# here the script starts

lon = 11.34999
lat = 46.49809
stationsFile = f"{folder}/data/stations.txt"
centerPoint = HPoint(lon, lat)

with open(stationsFile, 'r') as file:
    lines = file.readlines()
    
minDistance = 9999
nearestStationName = "none"
nearestDistancePoint = None
for line in lines[1:]:
    line = line.strip()
    
    lineSplit = line.split(",")
    name = lineSplit[1].strip()
    latString = lineSplit[3]
    lonString = lineSplit[4]
    
    latDec = fromLatString(latString)
    lonDec = fromLonString(lonString)
    #print(name, latDec, lonDec)
    point = HPoint(lonDec, latDec)
    
    distance = point.distance(centerPoint)
    if distance < minDistance:
        minDistance = distance
        nearestStationName = name
        nearestDistancePoint = point
        
print(nearestStationName, " -> ", nearestDistancePoint)
    
    
    
    
