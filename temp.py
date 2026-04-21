from datetime import datetime, time
import time
x = datetime.now()
print(x)
time.sleep(2)
y = datetime.now()
print(y)
print(y-x)
print((y-x).days)
print((y-x).microseconds)
