from pyqgis_scripting_ext.core import *
from math import cos, sin, radians

maxAngle = 360*10

cols = 7
rows = 9

n = 1
d = 0
easting = 0
northing = 0
counter = 0
points = []
elements = []
for row in range(rows):
    easting = 0
    northing -= 3
    n = 1
    d += 1
    for col in range(cols):    
            for angle in range(maxAngle):
                x = cos((n/d)*radians(angle))*(cos(radians(angle)))+easting
                y = cos((n/d)*radians(angle))*(sin(radians(angle)))+northing
                point = [x,y]
                points.append(point)
                angle += 1 
            element = HLineString.fromCoords(points)
            elements.append(element)
            easting += 3
            n+=1
            points = []
  
row = HMultiLineString(elements)
canvas = HMapCanvas()

for i in elements:
    canvas.add_geometry(i, 'black', 1)
canvas.set_extent([-10, -30, 30, 0])
canvas.show()
