from Control import Control
from random import randint


class Processor:

    def __init__(self, number):
        self.control = Control(number)
        self.number = number
        self.instructions = ("calc", "read", "write")
        self.current_ins = []
        self.next_ins = []

    def generate_instruction(self):
        instruction = randint(0, 2)
        instruction = self.instructions[instruction]
        self.current_ins = self.next_ins

        if instruction == "calc":
            self.next_ins = [instruction]
        elif instruction == "write":
            data = str(hex(randint(0, 65535)))
            dir_mem = randint(0, 15)
            self.next_ins = [instruction, dir_mem, data]
        else:
            dir_mem = randint(0, 15)
            self.next_ins = [instruction, dir_mem]

    def execute(self):
        self.generate_instruction()
        if len(self.current_ins) == 0:
            print("No instruction loaded")
        else:
            if self.current_ins[0] == "write":
                data = self.control.write_data(
                    self.current_ins[1], self.current_ins[2])
                print("Writing: ", data)
            elif self.current_ins[0] == "read":
                data = self.control.read_data(self.current_ins[1])
                print("Reading: ", data)
