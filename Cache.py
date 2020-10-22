from copy import copy

class Cache():

    def __init__(self):
        self.cache_mem = {
            "0": [
                {
                    "state": "I",
                    "value": "0x0000",
                    "dir": None
                },
                {
                    "state": "I",
                    "value": "0x0000",
                    "dir": None
                }
            ],
            "1": [
                {
                    "state": "I",
                    "value": "0x0000",
                    "dir": None
                },
                {
                    "state": "I",
                    "value": "0x0000",
                    "dir": None
                }
            ]
        }

    def read_data(self, dir_mem):
        block_set = []
        block = ""

        if dir_mem % 2 == 0:
            block_set = self.cache_mem["0"]
        else:
            block_set = self.cache_mem["1"]

        if block_set[0]["dir"] == dir_mem:
            block = block_set[0]
        elif block_set[1]["dir"] == dir_mem:
            block = block_set[1]

        return block

    def write_data(self, value, replacement_dir, dir_mem, state=None):
        block = ""

        if dir_mem % 2 == 0:
            block = self.cache_mem["0"][replacement_dir]
        else:
            block = self.cache_mem["1"][replacement_dir]

        block["value"] = copy(value)
        block["dir"] = dir_mem

        if state != None:
            block["state"] = state

        return value

    def change_state(self, dir_mem, state, replacement_dir):

        if dir_mem % 2 == 0:
            self.cache_mem["0"][replacement_dir]["state"] = state
        else:
            self.cache_mem["1"][replacement_dir]["state"] = state

        return state
