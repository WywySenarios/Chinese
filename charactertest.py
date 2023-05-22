# read the file
f = open("C:/Python/Chinese/characters.txt", "rb")
rawData = f.read().decode("UTF-8")
data = rawData.split("\r\n")
while True:  # remove all empty inputs
    try:
        data.remove("")
    except:
        break

# split data into indexes

characters = []
accentedPinyin = []
numberedPinyin = []
translation = []

for index in range(len(data)):
    if data[index][0] == "#":
        continue

    if index % 4 == 0:
        numberedPinyin.append(data[index])
    elif index % 4 == 1:
        translation.append(data[index])
    elif index % 4 == 2:
        characters.append(data[index])
    else:
        accentedPinyin.append(data[index])

print(characters)
print(accentedPinyin)
print(numberedPinyin)
print(translation)

input("Acknowledged... ")