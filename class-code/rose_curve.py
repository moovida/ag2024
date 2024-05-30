from pyqgis_scripting_ext.core import *
from math import cos, sin, radians

n = 3
d = 2
k = n/d
iterations = 20

startAngle = 0
endAngle = iterations * 360
delta = 1

coords = []
for angle in range(startAngle, endAngle, delta):
    r = cos(k * radians(angle))
    x = r * cos(radians(angle))
    y = r * sin(radians(angle))
    coords.append([x, y])

line = HLineString.fromCoords(coords)
canvas = HMapCanvas.new()
canvas.add_geometry(line)
canvas.set_extent(line.bbox())
canvas.show()
