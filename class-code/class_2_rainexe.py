
folder = "/Users/hydrologis/development/ag2024/"
dataPath = f"{folder}/data/01_exe_rain_data_1year.txt"

# read the data into a lines list
with open(dataPath, 'r') as file:
    lines = file.readlines()

# print out first 5 lines
date2ValuesListMap = {}
for line in lines:
    line = line.strip()
    if line.startswith("#") or len(line) == 0:
        continue
    
    # parse each line to extract the date (str) and value (num)
    lineSplit = line.split(",")
    date = lineSplit[0]
    value = float(lineSplit[1])

    # extract the year-month from the date
    month = date[:-2]
    #print(month, ": ", value)

    # aggregate the values by month, i.e. collect all values
    # for each date in a list
    values = date2ValuesListMap.get(month, [])
    values.append(value)
    date2ValuesListMap[month] = values
    
for month, values in date2ValuesListMap.items():
    #print(month, values)
    cumRain = sum(values)
    print(f"Cumulated rain for month {month} is {cumRain}")
    

