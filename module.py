import time
import threading
from multiprocessing import Process, cpu_count

print(__name__)

print(time.perf_counter())
print(threading.active_count())
print(threading.enumerate())

print(cpu_count())
