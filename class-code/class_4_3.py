from pyqgis_scripting_ext.core import *


g1 = HPolygon.fromCoords([[0, 0], [0, 5], [5, 5], [5, 0], [0, 0]])
g2 = HPolygon.fromCoords([[5, 0], [5, 2], [7, 2], [7, 0], [5, 0]])
g3 = HPoint(4, 1)
g4 = HPoint(5, 4)
g5 = HLineString.fromCoords([[1, 0], [1, 6]])
g6 = HPolygon.fromCoords([[3, 3], [3, 6], [6, 6], [6, 3], [3, 3]])


print("polygon boundingbox:", g1.bbox())

print("polygon length:", g1.length())
print("polygon area:", g1.area())

print("line length:", g5.length())
print("line area:", g5.area())

print("point length:", g3.length())
print("point area:", g3.area())

print("distance between line and point:", g5.distance(g4))


# PREDICATES

print("intersects")
print(g1.intersects(g2))
print(g1.intersects(g3))
print(g1.intersects(g4))
print(g1.intersects(g5))
print(g1.intersects(g6))

print("touches")
print(g1.touches(g2))
print(g1.touches(g3))
print(g1.touches(g4))
print(g1.touches(g5))
print(g1.touches(g6))

print("contains")
print(g1.contains(g2))
print(g1.contains(g3))
print(g1.contains(g4))
print(g1.contains(g5))
print(g1.contains(g6))

# FUNCTIONS

print("intersection")
print(g1.intersection(g6))
print(g1.intersection(g2))
print(g1.intersection(g3))
print(g1.intersection(g5))
newGeom = g1.intersection(g6)

print("symdifference")
print(g1.symdifference(g6))
print(g1.symdifference(g2))
print(g1.symdifference(g3))
print(g1.symdifference(g5))
newGeom = g1.symdifference(g6)

print("union")
print(g1.union(g6))
print(g1.union(g2))
print(g1.union(g3))
print(g1.union(g5))
newGeom = g1.union(g6)

print("difference")
print(g6.difference(g1))
print(g1.difference(g5))
print(g1.difference(g3))
newGeom = g6.difference(g1)


print("buffers")
b1 = g3.buffer(1.0)
b2 = g3.buffer(1.0, 1)

b3 = g5.buffer(1)
b4 = g5.buffer(1, 2)

b5 = g5.buffer(1, -1, JOINSTYLE_ROUND, ENDCAPSTYLE_SQUARE)


collection = HGeometryCollection([g1, g2, g3, g4, g5, g6])
hull = collection.convex_hull()

canvas = HMapCanvas.new()

canvas.add_geometry(g1,'black', 3)
canvas.add_geometry(g2,'black', 3)
canvas.add_geometry(g3,'black', 3)
canvas.add_geometry(g4,'black', 3)
canvas.add_geometry(g5,'black', 3)
canvas.add_geometry(g6,'black', 3)
canvas.add_geometry(hull,'orange', 3)
# canvas.add_geometry(g3,'black', 3)
# canvas.add_geometry(b1,'orange', 3)
# canvas.add_geometry(b2,'red', 3)
# canvas.add_geometry(g5,'black', 3)
# canvas.add_geometry(b3,'green', 3)
# canvas.add_geometry(b4,'magenta', 3)
# canvas.add_geometry(b5,'cyan', 3)

canvas.set_extent(hull.bbox())

canvas.show()