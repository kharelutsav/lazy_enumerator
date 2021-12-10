import threading
from queue import Queue
import time
import socket

# a print_lock is used to prevent "double"
# modification of shared variables this is
# used so that while one thread is using a
# variable others cannot access it Once it
# is done, the thread releases the print_lock.
# In order to use it, we want to specify a
# print_lock per thing you wish to print_lock.
print_lock = threading.Lock()

# ip = socket.gethostbyname(target)
target = 'localhost'

def portscan(port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		con = s.connect((target, port))
		with print_lock:
			print('port is open', port)
		con.close()
	except:
		print('port is close', port)


# The threader thread pulls a worker
# from a queue and processes it
def threader():
	while True:
		# gets a worker from the queue
		worker = q.get()

		# Run the example job with the available
		# worker in queue (thread)
		portscan(worker)

		# completed with the job
		q.task_done()


# Creating the queue and threader
q = Queue()

# number of threads are we going to allow for
for x in range(42):
	t = threading.Thread(target=threader)

	# classifying as a daemon, so they it will
	# die when the main dies
	t.daemon = True

	# begins, must come after daemon definition
	t.start()


start = time.time()

# 10 jobs assigned.
for worker in range(1, 1000):
	q.put(worker)

# wait till the thread terminates.
q.join()
