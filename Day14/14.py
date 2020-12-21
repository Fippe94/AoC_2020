f = open("Day14/input.txt")
data = f.readlines()

class Bitmask_system():

    def __init__(self):
        self.bitmask = "X" * 36
        self.mem = {}

    def set_bitmask(self, bitmask):
        self.bitmask = bitmask

    def set_value(self, address, value):
        binary = format(value, 'b')
        binary = "0" * (36 - len(binary)) + binary

        actual_value = ""
        for i in range(len(binary)):
            if self.bitmask[i] != "X":
                actual_value += self.bitmask[i]
            else:
                actual_value += binary[i]

        self.mem[address] = int(actual_value, 2)
    
    def print(self):
        for var in self.mem:
            print(str(var) + ": " + str(self.mem[var]))

    def mem_sum(self):
        return sum([self.mem[x] for x in self.mem])


        
system = Bitmask_system()

for string in data:
    line = string.split(' = ')
    if line[0] == 'mask':
        system.set_bitmask(line[1])
    else:
        system.set_value(int(line[0][4:-1]), int(line[1]))


system.print()
print(system.mem_sum())

