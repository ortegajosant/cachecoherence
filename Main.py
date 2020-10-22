from Memory import Memory

def main():
    memory = Memory.get_instance()
    memory2 = Memory.get_instance()
    print(memory.read_data(1))
    print(memory2.read_data(1))
    memory.set_data(1, "0x8569")
    print(memory.write_data(1))
    print(memory2.write_data(1))

main()
