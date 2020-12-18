f = open("Day6/input.txt")
data = f.read().strip()

groups = data.split("\n\n")

sum = 0
for group in groups:
        answers = {}
        persons = group.split("\n")
        for person in persons:
                for answer in person:
                        if answer in answers:
                                answers[answer] = answers[answer] + 1
                        else:
                                answers[answer] = 1
        print(len(persons))
        print(answers)
        s = len([answers[x] for x in answers if answers[x] == len(persons)])
        print(s)
        sum += s

print(sum)
