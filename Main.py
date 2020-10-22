from Processor import Processor
import threading
import tkinter as tk


window = ""
memory = []
processors = []
cache1 = {}
cache2 = {}
cache3 = {}
cache4 = {}


def begin():
    global window
    window = tk.Tk()
    width = 640
    height = 480
    window.title("Cache coherence")
    window.geometry(str(width) + "x" + str(height))

    mem_label = tk.Label(window, text="Memory", relief=tk.RAISED)
    mem_label.place(x=20, y=20)

    list_dir = tk.Listbox(window, width=3, height=16)
    list_data = tk.Listbox(window, width=7, height=16)
    for i in range(16):
        list_dir.insert(i, i)

    list_dir.place(x=20, y=40)
    list_data.place(x=46, y=40)

    curr_ins_label_1 = tk.Label(window, text="Current instruction")
    curr_ins_label_2 = tk.Label(window, text="Current instruction")
    curr_ins_label_3 = tk.Label(window, text="Current instruction")
    curr_ins_label_4 = tk.Label(window, text="Current instruction")

    curr_ins_label_1.place(x=115, y=40)
    curr_ins_label_2.place(x=375, y=40)
    curr_ins_label_3.place(x=115, y=180)
    curr_ins_label_4.place(x=375, y=180)

    curr_ins_label_1 = tk.Label(window, text="Next instruction")
    curr_ins_label_2 = tk.Label(window, text="Next instruction")
    curr_ins_label_3 = tk.Label(window, text="Next instruction")
    curr_ins_label_4 = tk.Label(window, text="Next instruction")

    curr_ins_label_1.place(x=115, y=140)
    curr_ins_label_2.place(x=375, y=140)
    curr_ins_label_3.place(x=115, y=280)
    curr_ins_label_4.place(x=375, y=280)

    current_ins_1 = tk.Listbox(window, width=15, height=1)
    current_ins_2 = tk.Listbox(window, width=15, height=1)
    current_ins_3 = tk.Listbox(window, width=15, height=1)
    current_ins_4 = tk.Listbox(window, width=15, height=1)
    
    current_ins_1.place(x=240, y=40)
    current_ins_2.place(x=500, y=40)
    current_ins_3.place(x=240, y=180)
    current_ins_4.place(x=500, y=180)

    next_ins_1 = tk.Listbox(window, width=15, height=1)
    next_ins_2 = tk.Listbox(window, width=15, height=1)
    next_ins_3 = tk.Listbox(window, width=15, height=1)
    next_ins_4 = tk.Listbox(window, width=15, height=1)

    next_ins_1.place(x=240, y=140)
    next_ins_2.place(x=500, y=140)
    next_ins_3.place(x=240, y=280)
    next_ins_4.place(x=500, y=280)

    cache_1_label = tk.Label(window, text="Processor 1", relief=tk.RAISED)
    cache_1_label.place(x=240, y=20)
    cache_2_label = tk.Label(window, text="Processor 2", relief=tk.RAISED)
    cache_2_label.place(x=500, y=20)
    cache_3_label = tk.Label(window, text="Processor 3", relief=tk.RAISED)
    cache_3_label.place(x=240, y=160)
    cache_4_label = tk.Label(window, text="Processor 4", relief=tk.RAISED)
    cache_4_label.place(x=500, y=160)

    list_cache_1 = tk.Listbox(window, width=15, height=4)
    list_cache_2 = tk.Listbox(window, width=15, height=4)
    list_cache_3 = tk.Listbox(window, width=15, height=4)
    list_cache_4 = tk.Listbox(window, width=15, height=4)

    list_cache_1.place(x=240, y=62)
    list_cache_2.place(x=500, y=62)
    list_cache_3.place(x=240, y=202)
    list_cache_4.place(x=500, y=202)


    update_memory(list_data)

    window.mainloop()


def update_memory(list_data):
    for i in range(len(memory)):
        list_data.insert(i, memory[i])



def set_initial_data():
    global processors, memory

    for i in range(1, 5):
        processors.append(Processor(i))

    memory = processors[0].control.bus.memory.memory
    cache1 = processors[0].control.cache.cache_mem
    cache2 = processors[1].control.cache.cache_mem
    cache3 = processors[2].control.cache.cache_mem
    cache4 = processors[3].control.cache.cache_mem


def main():

    set_initial_data()

    begin()

    # count = 0
    # while count < 5:
    #     print("\n -- Iteration ", count, "--\n")
    #     for i in processors:
    #         i.execute()

    #     count += 1


main()
