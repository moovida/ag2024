

def fileSummary(path, idFieldName, avgFieldName):
    with open(path, 'r') as file:
        lines = file.readlines()
        
        
    idIndex = None
    analyzeIndex = None
    hSum = 0
    count = 0
    uniqueIdsList = []
    for line in lines:
        line = line.strip()
        if line.startswith("#"):
            # we have the header
            fields = line.strip("#").split(",")
            
            for index, field in enumerate(fields):
                field = field.strip()
                if field == idFieldName:
                    idIndex = index
                elif field == avgFieldName:
                    analyzeIndex = index
        else:
            # HERE DATA STARTS
            lineSplit = line.split(",")
            value = float(lineSplit[analyzeIndex])
            if value != -9999:
                hSum += value
                count += 1
            
            idValue = lineSplit[idIndex]
            if idValue not in uniqueIdsList:
                uniqueIdsList.append(idValue)
            
    
    
    avg = hSum/count
    print(f"File info: {path}")
    print("=======================")
    print(f"Distinct count of field {idFieldName}: {len(uniqueIdsList)}")
    print(f"Average value of field {avgFieldName}: {avg}")
    print("Fields:")
    for field in fields:
        print(f" -> {field.strip()}")
        
    
    

folder = "/Users/hydrologis/development/ag2024"
fileSummary(f"{folder}/data/station_data.txt", "STAID", "RR")
print("******************************")
fileSummary(f"{folder}/data/stations.txt", "CN", "HGHT")
    

    










