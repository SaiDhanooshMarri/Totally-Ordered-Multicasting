# proc.py
from threading import Thread
import time
import random
from comm import Comm
from clock import Clock

class Proc(Thread):
    def __init__(self, pid, total_procs, clock, start_port):
        Thread.__init__(self)
        self.pid, self.total_procs, self.clock, self.start_port = pid, total_procs, clock, start_port
        self.comm = Comm(self.pid, self.clock, start_port + pid)
        self.comm.start()

    def join(self):
        self.comm.join()
        Thread.join(self)

    def run(self):
        i = 1
        while i < 4:
            evt = f"PID.EVT_{i}"
            self.local_op(evt)
            time.sleep(1)
            i += 1

    def local_op(self, evt):
        self.clock.inc_clock(self.pid)
        time_stamp = self.clock.get_time(self.pid)
        self.multicast(evt, time_stamp)

    def multicast(self, evt, time_stamp):
        i = 0
        while i < self.total_procs:
            if i != self.pid:
                dest_port = self.start_port + i
                self.comm.send_msg(dest_port, evt, time_stamp)
                time.sleep(0.5)
            i += 1
