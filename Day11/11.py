f = open("Day11/input.txt")
data = f.readlines()
data = [x.strip() for x in data]
rows = len(data)
columns = len(data[0])
print(rows)
print(columns)

def same_map(map1, map2):
    for row in range(len(map1)):
        if map1[row] != map2[row]:
            return False
    return True
    

def print_map(data):
    for row in data:
        print(row)
    print()

def count_adjacent_occupied(data, row, column):
    low_row = max(0,row-1)
    high_row = min(rows-1,row+1)
    low_col = max(0,column-1)
    high_col = min(columns-1,column+1)
    counter = 0
    r1 = range(low_row, high_row+1)
    r2 = range(low_col, high_col+1)
    for y in r1:
        for x in r2:
            if (y != row or x != column) and data[y][x] == '#':
                counter += 1
    return counter

def count_visible_occupied(data, row, column):
    adj = 0
    for x in range(column+1, columns): # RIGHT
        if data[row][x] == 'L':
            break
        elif data[row][x] == '#':
            adj += 1
            break
    for x in range(column-1, -1, -1):  # LEFT
        if data[row][x] == 'L':
            break
        elif data[row][x] == '#':
            adj += 1
            break
    for y in range(row+1, rows):  # DOWN
        if data[y][column] == 'L':
            break
        elif data[y][column] == '#':
            adj += 1
            break
    for y in range(row-1, -1, -1):  # UP
        if data[y][column] == 'L':
            break
        elif data[y][column] == '#':
            adj += 1
            break
    for i in range(1, min(rows - row, columns - column)):  # DOWNRIGHT
        if data[row + i][column + i] == 'L':
            break
        elif data[row + i][column + i] == '#':
            adj += 1
            break
    for i in range(1, min(row+1, columns - column)):  # DOWNLEFT
        if data[row - i][column + i] == 'L':
            break
        elif data[row - i][column + i] == '#':
            adj += 1
            break
    for i in range(1, min(rows - row, column+1)):  # UPRIGHT
        if data[row + i][column - i] == 'L':
            break
        elif data[row + i][column - i] == '#':
            adj += 1
            break
    for i in range(1, min(row+1, column+1)):  # UPLEFT
        if data[row - i][column - i] == 'L':
            break
        elif data[row - i][column - i] == '#':
            adj += 1
            break

    return adj


while(True):
    new_data = data.copy()
    for row in range(rows):
        for column in range(columns):
            if (data[row][column] == 'L' or data[row][column] == '#'):
                adj = count_visible_occupied(data, row, column)
                if adj == 0:
                    new_data[row] = new_data[row][:column] + \
                        '#' + new_data[row][column+1:]
                elif adj >= 5:
                    new_data[row] = new_data[row][:column] + \
                        'L' + new_data[row][column+1:]
                        
    if (same_map(data,new_data)):
        print_map(data)
        break

    data = new_data
    #print_map(data)

print(sum([x.count('#') for x in data]))

