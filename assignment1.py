# main.py
from proc import Proc
from clock import Clock
import time
import random

def main():
    num_procs = 3
    clock = Clock(num_procs)

    start_port = 5000 + random.randint(0, 1000)
    procs = [
        Proc(i, num_procs, clock, start_port) for i in range(num_procs)
    ]
    time.sleep(1)
    i = 0
    while i < len(procs):
        procs[i].start()
        i += 1

    i = 0
    while i < len(procs):
        procs[i].join()
        i += 1

if __name__ == "__main__":
    main()
