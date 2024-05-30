from math import cos, sin, radians
from pyqgis_scripting_ext.core import *


n = 8
d = 7
iterations = max(n,d)
maxAngle = 360*iterations

# define an angle
coords = []
for angle in range(0, maxAngle, 1):
    radAngle = radians(angle)
    k = n/d
    r = cos(k*radAngle)
    x = r*cos(radAngle)
    y = r*sin(radAngle)
    
    #print(x, y)
    coords.append([x,y])
    
line = HLineString.fromCoords(coords)


canvas = HMapCanvas.new()
canvas.add_geometry(line)
canvas.set_extent(line.bbox())
canvas.show()
    


