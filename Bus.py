# from Control import Control
from Memory import Memory
import threading


class Bus:

    __instance = None

    @staticmethod
    def get_instance():
        if Bus.__instance == None:
            with threading.Lock():
                if Bus.__instance == None:
                    Bus.__instance = Bus()
                else:
                    print("Bus instance already exists")
        return Bus.__instance

    def __init__(self):
        self.memory = Memory.get_instance()
        self.proc_control_1 = ""
        self.proc_control_2 = ""
        self.proc_control_3 = ""
        self.proc_control_4 = ""

    def set_proc_control(self, number, proc_control):
        if number == 1:
            self.proc_control_1 = proc_control
        elif number == 2:
            self.proc_control_2 = proc_control
        elif number == 3:
            self.proc_control_3 = proc_control
        elif number == 4:
            self.proc_control_4 = proc_control

    def read_data(self, dir_mem, number):
        block = ()

        i = 1

        while (i < 5):
            if i == 1 and i != number:
                block = self.proc_control_1.read_data(dir_mem, True)
            elif i == 2 and i != number:
                block = self.proc_control_2.read_data(dir_mem, True)
            elif i == 3 and i != number:
                block = self.proc_control_3.read_data(dir_mem, True)
            elif i == 4 and i != number:
                block = self.proc_control_4.read_data(dir_mem, True)

            if len(block) != 0:
                return block
            i += 1

        value = self.memory.read_data(dir_mem)
        return ("E", value)

    def write_mem_data(self, dir_mem, data):
        self.memory.write_data(dir_mem, data)
        return self.memory.read_data(dir_mem)

    def change_state(self, dir, func):
        pass

    def invalidate_all(self, dir_mem, number):

        i = 1

        while(i < 5):
            if i == 1 and i != number:
                self.proc_control_1.invalidate_bw(dir_mem)
            elif i == 2 and i != number:
                self.proc_control_2.invalidate_bw(dir_mem)
            elif i == 3 and i != number:
                self.proc_control_3.invalidate_bw(dir_mem)
            elif i == 4 and i != number:
                self.proc_control_4.invalidate_bw(dir_mem)
            i += 1
