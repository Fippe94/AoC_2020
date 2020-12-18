f = open("Day9/input.txt")
data = f.readlines()

numbers = []
preamble_length = 25
invalid_number = 0

for line in data:
    number = int(line)
    if len(numbers) > preamble_length:
        found_sum = False
        for n1 in numbers[-preamble_length:]:
            for n2 in numbers[-preamble_length:]:
                if n1 != n2 and n1+n2 == number:
                    found_sum = True
                    break
        if not found_sum:
            invalid_number = number
    numbers.append(number)

s_sum = 0
first_last = ()
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        contigous_sum = sum(numbers[i:j+1])
        if contigous_sum > invalid_number:
            break
        elif contigous_sum == invalid_number:
            first_last = (min(numbers[i:j+1]), max(numbers[i:j+1]))


print(invalid_number)
print(first_last, sum(first_last))
