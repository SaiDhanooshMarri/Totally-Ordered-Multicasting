# comm.py
from threading import Thread
import copy
import socket
import time

class Comm(Thread):
    def __init__(self, pid, clock, port):
        Thread.__init__(self)
        self.pid = pid
        self.clock = clock
        self.port = port
        self.rcv_count = 0

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind(("localhost", self.port))
            sock.listen(1)
            while self.rcv_count < 6:
                conn, addr = sock.accept()
                with conn:
                    data = conn.recv(1024)
                    if not data:
                        print(f"P{self.pid} received an empty message")
                        continue
                    rcvd_msg = eval(data.decode("utf-8"))
                    time_stamp = rcvd_msg["timestamp"]
                    self.clock.update_on_receive(time_stamp)
                    print(
                        f"P{self.pid} received message: '{rcvd_msg['message']}'"
                    )
                self.rcv_count += 1
            sock.close()

    def send_msg(self, dest_port, event, time_stamp):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect(("localhost", dest_port))
            msg = {"message": event, "timestamp": copy.deepcopy(time_stamp)}
            sock.sendall(str(msg).encode("utf-8"))
