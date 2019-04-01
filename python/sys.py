import sys
import time

for i in range(100):
    time.sleep(0.3)
    print (i)
    if i == 5:
      sys.exit()