

import threading
import time

class myThread (threading.Thread):
   def __init__(self, threadID, name, period):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.period = period
   def run(self):
      print ("Starting High Level Control" + self.name)
      # Get lock to synchronize threads
      #threadLock.acquire()
      print_time(self.name, self.period, 20)
      # Free lock to release next thread
      #threadLock.release()

class mySecondThread (threading.Thread):
    def __init__(self, threadID,name, period):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.period = period
    def run(self):
        print("Starting My Periodic Alive" + self.name)
        #threadLock.acquire()
        print_time(self.name,self.period, 10)
        #threadLock.release()

def print_time(threadName, delay, counter):
   while counter:

      time.sleep(delay)
      print ("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1




threadLock = threading.Lock()
threads = []

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()

# Add threads to thread list
threads.append(thread1)
threads.append(thread2)

# Wait for all threads to complete
for t in threads:
   t.join()
print ("Exiting Main Thread")
