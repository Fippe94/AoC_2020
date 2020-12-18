f = open("Day3/input.txt")

data = f.readlines()

x = 0
length = len(data[0])-1
count = 0

slopes = [1,3,5,7]
res = []

for slope in slopes:
        for line in data:
                if line[x % length] == '#':
                        count += 1
                x += slope
        res.append(count)
        count = 0
        x = 0

skip = True
for line in data:
        skip ^= True
        if skip:
                continue
        if line[x % length] == '#':
                count += 1
        x += 1
res.append(count)

result = 1
for r in res:
        result *= r
        
print(res)
print(result)


