f = open("Day2/input.txt")

data = f.readlines()

valid_count = 0


for line in data:
    split_data = line.split(" ")
    sep = split_data[0].index("-")
    pos1 = int(split_data[0][0:sep])
    pos2 = int(split_data[0][sep+1:])
    pass_letter = split_data[1][0]

    password = split_data[2]
    if (password[pos1-1] == pass_letter) ^ (password[pos2-1] == pass_letter):
        valid_count += 1

print(valid_count)


