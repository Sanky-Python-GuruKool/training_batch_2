import time
import math

start = time.time()
print(math.sqrt(144))
print(math.factorial(50))

print("Loading...")
time.sleep(5)
print("Done!")

stop = time.time()

print(start, stop)
print(stop - start)
