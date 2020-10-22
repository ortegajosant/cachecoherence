import threading

class Memory:

    __instance = None

    @staticmethod
    def get_instance():
        if Memory.__instance == None:
            with threading.Lock():
                if Memory.__instance == None:
                    Memory.__instance = Memory()
                else:
                    print("Memory instance already exists")
        return Memory.__instance

    def __init__(self):
        self.memory = ["0x0000", "0x0000", "0x0000", "0x0000",
                       "0x0000", "0x0000", "0x0000", "0x0000",
                       "0x0000", "0x0000", "0x0000", "0x0000",
                       "0x0000", "0x0000", "0x0000", "0x0000"]

    def read_data(self, dir_mem):
        for i in range(len(self.memory)):
            if i == dir_mem:
                return self.memory[i]

    def write_data(self, dir_mem, data):
        for i in range(len(self.memory)):
            if i == dir_mem:
                self.memory[i] = data["value"]
                return self.memory[i]
