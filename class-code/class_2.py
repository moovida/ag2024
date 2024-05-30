folder = "/Users/hydrologis/development/ag2024"
tmpFolder = f"{folder}/tmp"

mylist = ["merano", "Bolzano", "Trento"]

print(mylist)
print("The elements start at position 0: ", mylist[0])

mylist.append("Postdam")
print(mylist)
mylist.remove("Postdam")
print(mylist)
mylist.pop(0)
print(mylist)

mylist = ["merano", "Bolzano", "Trento"]
doIHaveBolzano = "Bolzano" in mylist
print(doIHaveBolzano)
doIHavePotsdam = "Potsdam" in mylist
print(doIHavePotsdam)

for item in mylist:
    print(item)

colors = ["red", "green", "blue", "purple"]
ratios = [0.2, 0.3, 0.1, 0.4]

for index in range(len(colors)):
    color = colors[index]
    ratio = ratios[index]
    
    print(f"{color} -> {ratio}")


for i in range(10):
    if i == 5:
        break
    print(f"A) {i}")
print("-------")

for i in range(10):
    if i == 5:
        continue
    print(f"B) {i}")
print("-------")

for i in range(0, 10, 2):
    print(f"C) {i}")
print("-------")

for i in range(10, 0, -2):
    print(f"D) {i}")
    

mylist = ["Merano", "Bolzano", "Trento"]
print(f"My original list: {mylist}")
mylist.sort()
print(f"My sorted list: {mylist}")
mylist.sort(reverse = True)
print(f"My rev-sorted list: {mylist}")


mylist = ["banana", "Orange", "Kiwi", "cherry"]
mylist.sort()
print(f"A mixed case list, sorted: {mylist}")
mylist.sort(key = str.lower)
print(f"A mixed case list, properly sorted: {mylist}")

numlist = ["002", "01", "3", "004"]
numlist.sort()
print(numlist)

numlist = ["002", "01", "3", "004"]

def toInt(string):
    return int(string)
    
numlist.sort(key = toInt)
print(numlist)

abc = ["a", "b", "c"]
cde = ["c", "d", "e"]

newabcde = abc + cde
print(newabcde)


print(";".join(newabcde))
print("|".join(newabcde))

numlist = [1.0, 2.0, 3.5, 6, 11, 34, 12]
print(max(numlist))
print(min(numlist))
#del(sum)
print(sum(numlist))

avg = sum(numlist)/len(numlist)
print(avg)
# calculate the average of a list 
# using a for loop

mysum = 0
count = 0
for item in numlist:
    #mysum = mysum + item
    mysum += item
    #count = count + 1
    count += 1
avg = mysum/count
print(avg)

townsProvincesMap = {
    "merano": "BZ",
    "bolzano": "BZ",
    "trenot": "TN" }
print(townsProvincesMap)
print(townsProvincesMap["merano"])

townsProvincesMap["potsdam"] = "BR"
print(townsProvincesMap)
townsProvincesMap.pop("potsdam")
print(townsProvincesMap)

if townsProvincesMap.get("Merano") is None:
    print("key doesn't exist")
else:
    print("key exists")

print(townsProvincesMap.get("Merano", "unknown"))


for key, value in townsProvincesMap.items():
    print(key, "is in the province of", value)
    
print(townsProvincesMap.keys())
print(townsProvincesMap.values())

keys = list(townsProvincesMap.keys())
keys.sort()
print(keys)
for key in keys:
    print(key, "is in the province of", townsProvincesMap[key])
    
    
filePath = f"{tmpFolder}/data.txt"
data = """# stationid, datetime, temperature
1, 2023-01-01 00:00, 12.3

2, 2023-01-01 00:00, 11.3
3, 2023-01-01 00:00, 10.3"""

with open(filePath, 'w') as file:
    file.write(data)

with open(filePath, 'a') as file:
    file.write("\n1, 2023-01-02 00:00, 9.3")
    file.write("\n2, 2023-01-02 00:00, 8.3")
    
with open(filePath, 'r') as file:
    lines = file.readlines()

print("--------------------")
stationsCount = {}
for line in lines:
    line = line.strip()
    if line.startswith("#") or len(line) == 0:
        continue
    lineSplit = line.split(",")
    stationId = lineSplit[0]
    
    counter = stationsCount.get(stationId, 0)
    counter += 1
    stationsCount[stationId] = counter
    
    print(stationsCount)
    

    
    
    











