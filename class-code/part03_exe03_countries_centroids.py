from pyqgis_scripting_ext.core import *

folder = "/Users/hydrologis/development/ag2024"

geopackagePath = f"{folder}/data/natural_earth_vector.gpkg"
countriesName = "ne_50m_admin_0_countries"

HMap.remove_layers_by_name(["centroids"])

schema = {
    "name":"string"
}

centroidsLayer = HVectorLayer.new("centroids", "Point", \
                                "EPSG:4326", schema)
                                
countryLayer = HVectorLayer.open(geopackagePath, countriesName)

nonInCountryList = []
nameIndex = countryLayer.field_index("NAME")
for country in countryLayer.features():
    countryGeom = country.geometry
    name = country.attributes[nameIndex]
    
    centroid = countryGeom.centroid()
    
    centroidsLayer.add_feature(centroid, [name])
    
    if not centroid.intersects(countryGeom):
        nonInCountryList.append(name)
    
    
simpleStyle = HMarker("circle", 10) + HLabel("name") + HHalo()
centroidsLayer.set_style(simpleStyle)
HMap.add_layer(centroidsLayer)

print("Countries with centroids not inside the main polygon:")
for c in nonInCountryList:
    print(c)
    
