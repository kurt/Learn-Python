import _thread
import time


def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(threadName, ": ", time.ctime(time.time()))

try:
    _thread.start_new_thread(print_time, ("Thread1", 2))
    _thread.start_new_thread(print_time, ("Thread2", 4))
except:
    print("Error thread could not start")

while 1:
    pass
