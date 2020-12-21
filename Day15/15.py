data = "2,0,6,12,1,3"
data = [int(x) for x in data.split(',')]
last_turn_spoken = {}
turn_number = 1
latest_number = 0
for n in data[:-1]:
    last_turn_spoken[n] = turn_number
    turn_number += 1
    #print(n)

latest_number = data[-1]
while turn_number < 30000000:
    if turn_number % 1000000 == 0:
        print(turn_number)
    new_number = 0
    #print(last_turn_spoken)
    if latest_number in last_turn_spoken:
        new_number = turn_number-last_turn_spoken[latest_number]

    last_turn_spoken[latest_number] = turn_number
    #print(latest_number)
    latest_number = new_number
    turn_number += 1

print(latest_number)


