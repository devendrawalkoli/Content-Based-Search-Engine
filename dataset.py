import os

cat = []
data = []

with os.scandir('dataset') as entries:
    for entry in entries:
        # print(entry.name)
        cat.append(entry.name)

t = 0
for i in range(0, len(cat)):
    data.append([])
    with os.scandir('dataset/' + str(cat[i])) as entries:
        for k in entries:
            data[i].append(k)
            t = t+1

#DirEntry to string conversion

sp = (data[0][0])
new = str(sp)
new = new[:-2]
new = new[-14:]

print(new)
print(t)
