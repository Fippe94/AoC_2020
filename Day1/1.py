f = open("Day1/input.txt")

data = f.readlines()

numbers = [int(line) for line in data]

for i in range(len(numbers)-1):
    for j in range(i+1,len(numbers)):
        for k in range(j+1,len(numbers)):
            sum = numbers[i] + numbers[j] + numbers[k]
            if (sum == 2020):
                print(numbers[i]*numbers[j]*numbers[k])
                break

    

