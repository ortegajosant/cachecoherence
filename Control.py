from Cache import Cache
from Bus import Bus


class Control:

    def __init__(self, number):
        self.cache = Cache()
        self.cache_state = self.cache.cache_mem
        # self.cache_state = {
        #     "0": [
        #         {
        #             "state": "I",
        #             "dir": None
        #         },
        #         {
        #             "state": "I",
        #             "dir": None
        #         }
        #     ],
        #     "1": [
        #         {
        #             "state": "I",
        #             "dir": None
        #         },
        #         {
        #             "state": "I",
        #             "dir": None
        #         }
        #     ]
        # }
        self.cache_state
        self.bus = Bus.get_instance()
        self.bus.set_proc_number(number, self)
        self.number = number

    def read_data(self, dir_mem, out_request=False):
        block_set = []
        block = ""
        i = 0
        if dir_mem % 2 == 0:
            block_set = self.cache_state["0"]
        else:
            block_set = self.cache_state["1"]
        if block_set[0]["dir"] == dir_mem and block_set[0]["state"] != "I":
            block = self.cache.read_data(dir_mem)
            i = 0
        elif block_set[1]["dir"] == dir_mem and block_set[1]["state"] != "I":
            block = self.cache.read_data(dir_mem)
            i = 1

        if isinstance(block, str) and not out_request:
            self.check_bus_data(dir_mem, "read")
        elif out_request:
            replacement_state = "S"
            if block["state"] == "E" or block["state"] == "M":
                replacement_local_state = ""
                if block["state"] == "E":
                    replacement_local_state = "S"
                elif block["state"] == "M":
                    replacement_local_state = "O"
                self.cache.change_state(dir_mem, replacement_local_state, i)

            return (replacement_state, block["value"])
            

    def check_bus_data(self, dir_mem, flag_func):
        block_set = []
        block = ""
        if dir_mem % 2 == 0:
            block_set = self.cache_state["0"]
        else:
            block_set = self.cache_state["1"]

        if block_set[0]["dir"] == dir_mem:
            block = block_set[0]
        elif block_set[1]["dir"] == dir_mem:
            block = block_set[1]

        block = self.bus.read_data(dir_mem, self.number)
        self.__replacement_policie(dir_mem, block)

    def write_data(self, dir_mem, data):
        block_set = []
        block = 0
        if dir_mem % 2 == 0:
            block_set = self.cache_state["0"]
        else:
            block_set = self.cache_state["1"]
        if block_set[0]["dir"] == dir_mem:
            block = 0

        elif block_set[1]["dir"] == dir_mem:
            block = 1

        if isinstance(block, str):
            block = self.__replacement_policie(dir_mem, "M")

        self.bus.invalidate_all(dir_mem, self.number)
        self.cache.write_data(data, block, dir_mem, "M")

    def __replacement_policie(self, dir_mem, state, func=None):
        block_set = []
        if dir_mem % 2 == 0:
            block_set = self.cache_state["0"]
        else:
            block_set = self.cache_state["1"]

        if block_set[0]["state"] == "I" or block_set[1]["state"] == "I":
            i = 0
            if block_set[1]["state"] == "I" and block_set[0]["state"] != "I":
                i = 1

        elif block_set[0]["state"] == "E" or block_set[1]["state"] == "E":
            i = 0
            if block_set[1]["state"] == "E" and block_set[0]["state"] != "E":
                i = 1

        elif block_set[0]["state"] == "S" or block_set[1]["state"] == "S":
            i = 0
            if block_set[1]["state"] == "S" and block_set[0]["state"] != "S":
                i = 1

        elif block_set[0]["state"] == "M" or block_set[1]["state"] == "M":
            i = 0
            if block_set[1]["state"] == "M" and block_set[0]["state"] != "M":
                i = 1
            value = self.cache.read_data(self.block_set[i]["dir"])
            self.bus.write_mem_data(block_set[i]["dir"], value)

        elif block_set[0]["state"] == "O" or block_set[1]["state"] == "O":
            i = 0
            if block_set[1]["state"] == "O" and block_set[0]["state"] != "O":
                i = 1
            value = self.cache.read_data(self.block_set[i]["dir"])
            self.bus.write_mem_data(block_set[i]["dir"], value)

        return i

    def invalidate_bw(self, dir_mem):
        block_set = []
        if dir_mem % 2 == 0:
            block_set = self.cache_state["0"]
        else:
            block_set = self.cache_state["1"]

        block = ""
        if block_set[0]["dir"] == dir_mem:
            block = 0
        elif block_set[1]["dir"] == dir_mem:
            block = 1

        if not isinstance(block, str):
            if block_set[block]["state"] == "M" or block_set[block]["state"] == "O":
                value = self.cache.read_data(self.block_set[block]["dir"])
                self.bus.write_mem_data(block_set[block]["dir"], value)
            self.cache.change_state(dir_mem, "I", block)
            return True
        else:
            return False
