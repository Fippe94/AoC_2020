
combinations = {}

def find_combinations(adapters):
    if len(adapters) == 1:
        return 1
    adapter = adapters.pop(0)
    #print(adapters)
    #print(combinations)
    if adapter in combinations:
        return combinations[adapter]
    sum = 0
    for i in range(min(len(adapters), 3) -1, -1,-1):
        if adapters[i] - adapter <= 3:
            res = find_combinations(adapters[i:])
            sum += res
            combinations[adapters[i]] = res
    return sum


f = open("Day10/input.txt")
data = f.readlines()

numbers = [0]

for line in data:
    numbers.append(int(line))

numbers.sort()

differences = {1: 0, 2: 0, 3: 1}
for i in range(1, len(numbers)):
    diff = numbers[i] - numbers[i - 1]
    differences[diff] += 1

print(differences)
print(differences[1] * differences[3])

print(find_combinations(numbers))



