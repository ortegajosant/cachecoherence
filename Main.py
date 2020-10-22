from Processor import Processor
import threading
import tkinter as tk
from time import sleep


window = ""
memory = []
processors = []
cache1 = {}
cache2 = {}
cache3 = {}
cache4 = {}

next_list = []
current_list = []
entry = ""
pause = True
list_data = []
list_cache = []
threads = []
run = True
infinite = True


def begin():
    global window, next_list, current_list, entry, list_data, list_cache

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
    curr_ins_label_3.place(x=115, y=200)
    curr_ins_label_4.place(x=375, y=200)

    cache_name_1 = tk.Label(window, text="Cache 1")
    cache_name_2 = tk.Label(window, text="Cache 2")
    cache_name_3 = tk.Label(window, text="Cache 3")
    cache_name_4 = tk.Label(window, text="Cache 4")

    cache_name_1.place(x=115, y=62)
    cache_name_2.place(x=375, y=62)
    cache_name_3.place(x=115, y=222)
    cache_name_4.place(x=375, y=222)

    curr_ins_label_1 = tk.Label(window, text="Next instruction")
    curr_ins_label_2 = tk.Label(window, text="Next instruction")
    curr_ins_label_3 = tk.Label(window, text="Next instruction")
    curr_ins_label_4 = tk.Label(window, text="Next instruction")

    curr_ins_label_1.place(x=115, y=140)
    curr_ins_label_2.place(x=375, y=140)
    curr_ins_label_3.place(x=115, y=300)
    curr_ins_label_4.place(x=375, y=300)

    current_ins_1 = tk.Listbox(window, width=15, height=1)
    current_ins_2 = tk.Listbox(window, width=15, height=1)
    current_ins_3 = tk.Listbox(window, width=15, height=1)
    current_ins_4 = tk.Listbox(window, width=15, height=1)

    current_ins_1.place(x=240, y=40)
    current_ins_2.place(x=500, y=40)
    current_ins_3.place(x=240, y=200)
    current_ins_4.place(x=500, y=200)

    next_ins_1 = tk.Listbox(window, width=15, height=1)
    next_ins_2 = tk.Listbox(window, width=15, height=1)
    next_ins_3 = tk.Listbox(window, width=15, height=1)
    next_ins_4 = tk.Listbox(window, width=15, height=1)

    next_ins_1.place(x=240, y=140)
    next_ins_2.place(x=500, y=140)
    next_ins_3.place(x=240, y=300)
    next_ins_4.place(x=500, y=300)

    cache_1_label = tk.Label(window, text="Processor 1", relief=tk.RAISED)
    cache_1_label.place(x=240, y=20)
    cache_2_label = tk.Label(window, text="Processor 2", relief=tk.RAISED)
    cache_2_label.place(x=500, y=20)
    cache_3_label = tk.Label(window, text="Processor 3", relief=tk.RAISED)
    cache_3_label.place(x=240, y=180)
    cache_4_label = tk.Label(window, text="Processor 4", relief=tk.RAISED)
    cache_4_label.place(x=500, y=180)

    list_cache_1 = tk.Listbox(window, width=15, height=4)
    list_cache_2 = tk.Listbox(window, width=15, height=4)
    list_cache_3 = tk.Listbox(window, width=15, height=4)
    list_cache_4 = tk.Listbox(window, width=15, height=4)
    list_cache = [list_cache_1, list_cache_2, list_cache_3, list_cache_4]
    list_cache_1.place(x=240, y=62)
    list_cache_2.place(x=500, y=62)
    list_cache_3.place(x=240, y=222)
    list_cache_4.place(x=500, y=222)

    current_list = [current_ins_1, current_ins_2, current_ins_3, current_ins_4]
    next_list = [next_ins_1, next_ins_2, next_ins_3, next_ins_4]


    button_step = tk.Button(window, text="Step by step", command=step_func)
    button_cicle = tk.Button(window, text="Cicle", command=cicle_func)
    button_infinite = tk.Button(window, text="Inf", command=infi_func)
    button_pause = tk.Button(window, text="Pause", command=change_pause)

    button_step.place(x=100, y=400)
    button_cicle.place(x=250, y=400)
    button_infinite.place(x=350, y=400)
    button_pause.place(x=350, y=440)

    entry = tk.Entry(window, width=5)
    entry.place(x=250, y=440)

    window.mainloop()


def change_pause():
    global pause
    if pause:
        pause = False


def step_func():
    execute_instructon(1)


def cicle_func():
    global entry
    
    cicles = entry.get()

    if len(cicles) != 0:
        execute_instructon(int(cicles))


def infi_func():
    global pause
    pause = True

    while pause:
        step_func()


def update_memory():
    global list_data
    for i in range(len(memory)):
        list_data.insert(i, memory[i])


def update_cache(number):
    global list_cache
    global cache1, cache2, cache3, cache4
    cache = {}

    if number == 1:
        cache = cache1
    elif number == 2:
        cache = cache2
    elif number == 3:
        cache = cache3
    else:
        cache = cache4
    string = ""
    count = 0
    # print(cache)
    for i in cache["0"]:
        string += i["state"] + "\t" + i["value"] + "\t" + str(i["dir"])
        list_cache[number - 1].insert(count, string)
        string = ""
        count += 1
    string = ""
    for i in cache["1"]:
        string += i["state"] + "\t" + i["value"] + "\t" + str(i["dir"])
        list_cache[number - 1].insert(count, string)
        string = ""
        count += 1


def execute_instructon(cicle):
    count = 0

    while (count < cicle):
        execute_proc_1()
        execute_proc_2()
        execute_proc_3()
        execute_proc_4()
        sleep(1)
        count += 1


def execute_proc_1():
    global processors, run

    processors[0].execute()
    update_memory()
    update_cache(1)
    update_instructions(1)


def execute_proc_2():
    global processors

    processors[1].execute()
    update_memory()
    update_cache(2)
    update_instructions(2)


def execute_proc_3():
    global processors

    processors[2].execute()
    update_memory()
    update_cache(3)
    update_instructions(3)


def execute_proc_4():
    global processors

    processors[3].execute()
    update_memory()
    update_cache(4)
    update_instructions(4)


def update_instructions(number):
    global current_list, next_list
    proc = processors[number - 1]
    curr_str = ""
    next_str = ""
    for i in proc.current_ins:
        curr_str += str(i) + " "
    for i in proc.next_ins:
        next_str += str(i) + " "

    current_list[proc.number - 1].insert(0, curr_str)
    next_list[proc.number - 1].insert(0, next_str)


def set_initial_data():
    global processors, memory, cache1, cache2, cache3, cache4, threads

    for i in range(1, 5):
        processors.append(Processor(i))
        if i == 1:
            threads.append(threading.Thread(target=execute_proc_1))
        elif i == 2:
            threads.append(threading.Thread(target=execute_proc_2))
        elif i == 3:
            threads.append(threading.Thread(target=execute_proc_2))
        elif i == 4:
            threads.append(threading.Thread(target=execute_proc_4))

    memory = processors[0].control.bus.memory.memory
    cache1 = processors[0].control.cache.cache_mem
    cache2 = processors[1].control.cache.cache_mem
    cache3 = processors[2].control.cache.cache_mem
    cache4 = processors[3].control.cache.cache_mem

    


def main():

    set_initial_data()

    begin()


main()
