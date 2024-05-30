from pyqgis_scripting_ext.core import *

folder = "/Users/hydrologis/development/ag2024"
tmpFolder = f"{folder}/tmp/"

countries = ["italy", "austria", "germany"]
geopackagePath = f"{folder}/data/natural_earth_vector.gpkg"
countriesName = "ne_10m_admin_0_countries"

meteoPath = f"{folder}/data/22yr_T10MX"

colorTable = {
    -10: "cyan",
    0: "blue",
    5: "darkgreen",
    8: "green",
    10: "limegreen",
    12: "yellow",
    13: "olive",
    14: "orange",
    15: "darkorange",
    16: "saddlebrown",
    18: "orangered",
    20: "red",
    22: "darkred",
    25: "brown",
    50: "firebrick"
}

countriesLayer = HVectorLayer.open(geopackagePath, countriesName)
osm = HMap.get_osm_layer()


with open(meteoPath, 'r') as file:
    lines = file.readlines()

cellDataList = []
isData = False
for line in lines:
    line = line.strip()
   
    if "lat" in line.lower() and "lon" in line.lower() and "jan" in line.lower():
        isData = True
        continue
    
    if line.startswith("#") or len(line) == 0:
        continue        
        
    if isData:
        lineSplit = line.split(" ")
        lat = float(lineSplit[0])
        lon = float(lineSplit[1])
        value = float(lineSplit[-1])
        
        ll = [lon, lat]
        ul = [lon, lat+1]
        ur = [lon+1, lat+1]
        lr = [lon+1, lat]
        cellPolygonCoords = [ll, ul, ur, lr, ll]
        cellPolygon = HPolygon.fromCoords(cellPolygonCoords)
        
        # get the color
        selectedColor = None
        for lowerLimit, color in colorTable.items():
            if value < lowerLimit:
               selectedColor = color
               break 
        
        cellData = {
            "geom": cellPolygon,
            "value": value,
            "color": color
            }
        cellDataList.append(cellData)
        
print(f"Found {len(cellDataList)} cells in file.")
        
print(f"Get the border of {','.join(countries)}")
countriesFeatures = countriesLayer.features()
nameIndex = countriesLayer.field_index("NAME")
countryGeom = None
for feature in countriesFeatures:
    fCountry = feature.attributes[nameIndex].lower()
    
    if fCountry in countries:
        if not countryGeom:
            countryGeom = feature.geometry
        else:
            countryGeom = countryGeom.union(feature.geometry)


cellsToKeepList = []
if countryGeom:
    print("Now joining datasets...")
    for cellData in cellDataList:
        try:
            cellGeom = cellData["geom"]
            if countryGeom.intersects(cellGeom):
                cellsToKeepList.append(cellData)
        except:
            print(cellData["value"])
            
    print(f"Found {len(cellsToKeepList)} cells intersecting {countries}.")
    
    
    # create intersection geometries
    for cellData in cellsToKeepList:
        cellGeom = cellData["geom"]
        newCellGeom = countryGeom.intersection(cellGeom)
        cellData["geom"] = newCellGeom
    
    # now draw on canvas
    canvas = HMapCanvas.new()
    canvas.set_layers([osm])
    
    crsHelper = HCrs()
    crsHelper.from_srid(4326)
    crsHelper.to_srid(3857)
    
    for cellData in cellsToKeepList:
        cellGeom = cellData["geom"]
        color = cellData["color"]
        cellGeom3857 = crsHelper.transform(cellGeom)
        
        canvas.add_geometry(cellGeom3857, color, 2)
    
    wsen = crsHelper.transform(countryGeom).bbox()
    canvas.set_extent(wsen)
    canvas.show()
    
    
else:
    print(f"ERROR: country {country} not found.")







