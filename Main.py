from Processor import Processor
import threading
import tkinter as tk

def main_loop():
    pass


def main():

    processors = []

    for i in range(1, 5):
        processors.append(Processor(i))

    count = 0
    while count < 5:
        print("\n -- Iteration ", count, "--\n")
        for i in processors:
            i.execute()
        
        count += 1

main()
