# clock.py
class Clock:
    def __init__(self, num_procs):
        self.num_procs = num_procs
        self.clocks = [0] * num_procs

    def inc_clock(self, pid):
        self.clocks[pid] += 1

    def get_time(self, pid):
        return self.clocks[:]

    def update_on_receive(self, received_time):
        i = 0
        while i < self.num_procs:
            self.clocks[i] = max(self.clocks[i], received_time[i]) + 1
            i += 1
