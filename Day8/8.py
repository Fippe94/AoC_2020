class GameConsole:

    def __init__(self, program):
        self.reset_console()
        self.set_program(program)

    def reset_console(self):
        self.accumulator = 0
        self.instruction_pointer = 0
        self.visited_lines = set()

    def set_program(self, program):
        self.program = program


    def end_of_program(self):
        return self.instruction_pointer == len(self.program)

    def get_instruction(self):
        
        return self.program[self.instruction_pointer]

    def is_in_infinite_loop(self):
        return self.instruction_pointer in self.visited_lines

    def execute_next(self):
        self.visited_lines.add(self.instruction_pointer)
        inst = self.get_instruction().split()
        #print(inst)

        if inst[0] == 'nop':
            self.instruction_pointer += 1
        elif inst[0] == 'acc':
            self.accumulator += int(inst[1])
            self.instruction_pointer += 1
        elif inst[0] == 'jmp':
            self.instruction_pointer += int(inst[1])

    def run_program(self):
        while True:

            if self.end_of_program():
                return (0, self.accumulator)
            if self.is_in_infinite_loop():
                return (-1, self.accumulator)

            self.execute_next()

    def run_until_infinite_loop(self):
        while not self.is_in_infinite_loop():
            self.execute_next()
        return self.accumulator




f = open("Day8/input.txt")
data = f.readlines()

for index in range(len(data)):
    if data[index][:3] == 'nop':
        new_data = data.copy()
        new_data[index] = 'jmp' + data[index][3:]
        console = GameConsole(new_data)
        result = console.run_program()
        if (result[0] == 0):
            print(result[1])
    if data[index][:3] == 'jmp':
        new_data = data.copy()
        new_data[index] = 'nop' + data[index][3:]
        console = GameConsole(new_data)
        result = console.run_program()
        if (result[0] == 0):
            print(result[1])
    

console = GameConsole(data)

result = console.run_program()



print(result)

