folder = "/Users/hydrologis/development/ag2024/"
csvPath = f"{folder}/data/01_exe2_data.csv"

with open(csvPath, "r") as file:
    lines = file.readlines()
    
for line in lines:
    line = line.strip()
    lineSplit = line.split(";")
    print(lineSplit)
    
    analogString = lineSplit[0]
    analogSplit = analogString.split(":")
    x1 = float(analogSplit[1])
    
    maxvoltageString = lineSplit[1]
    y2 = float(maxvoltageString[11:])
    
    maxanalogString = lineSplit[2]
    x2 = float(maxanalogString.split(":")[1])
    
    # x2/x1 = y2/y1
    y1 = y2 * x1/x2
    
    print(x1, x2, y1, y2)
    
    




