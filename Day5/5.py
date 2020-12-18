f = open("Day5/input.txt")
data = f.readlines()

def get_seat(seat_string):
        row = int(get_linerow(seat_string[:7], 0, 127))
        column = int(get_linerow(seat_string[7:], 0, 7))
        return (row, column, row*8+column)

def get_linerow(seat_string, lower, upper):
        if lower == upper:
                return lower
        char = seat_string[0]
        midpoint = (upper+1-lower)/2 + lower
        if char == "F" or char == "L":
                return get_linerow(seat_string[1:], lower, midpoint-1)
        else:
                return get_linerow(seat_string[1:], midpoint, upper)
        return -1

highest_id = 0
pass_ids = []

for boarding_pass in data:
        seat = get_seat(boarding_pass)
        pass_ids.append(seat[2])
        if (seat[2] > highest_id):
                highest_id = seat[2]

pass_ids.sort()
my_pass = -1
expected_next = -1
print(pass_ids)
for pass_id in range(pass_ids[0], pass_ids[-1]):
        if (pass_id not in pass_ids):
                print(pass_id)





print(my_pass)

