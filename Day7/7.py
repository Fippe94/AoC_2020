import re
f = open("Day7/input.txt")
data = f.readlines()

bags = {}

carried_in = {}

for line in data:
        bag_data = re.split(" bags contain | bags\, | bag\, | bags\.$|bag\.$", line.strip())[:-1]

        bag = bag_data[0].strip()
        if (bag_data[1] == "no other"):
                continue
        for b in  bag_data[1:]:
                bag_type = b[2:].strip()
                if bag_type in carried_in:
                        carried_in[bag_type].append(bag)
                else:
                        carried_in[bag_type] = [bag]
                if bag in bags:
                        bags[bag].append((int(b[0]), bag_type))
                else:
                        bags[bag] = [(int(b[0]), bag_type)]

can_carry_gold = set()

current_bags = ['shiny gold']
while len(current_bags) > 0:
        current_bag = current_bags.pop()
        if current_bag in carried_in:
                current_bags.extend(carried_in[current_bag])
                can_carry_gold.update(carried_in[current_bag])

number_of_bags = 0
current_bags = [(1, 'shiny gold')]
while len(current_bags) > 0:
        current_bag = current_bags.pop()
        if current_bag[1] in bags:
                for i in range(current_bag[0]):
                        for b in bags[current_bag[1]]:
                                number_of_bags += b[0]
                                current_bags.append(b)


print(len(can_carry_gold))
print(number_of_bags)
