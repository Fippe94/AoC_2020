f = open("Day13/input.txt")
data = f.readlines()

earliest_timestamp = int(data[0])
buses = [int(x) for x in data[1].split(',') if x != 'x']

time = earliest_timestamp
found = False
while (not found):
    for bus in buses:
        if time % bus == 0:
            print((time - earliest_timestamp) * bus)
            found = True
            break
    time += 1




