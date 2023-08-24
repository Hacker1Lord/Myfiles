import threading
import time

def test():
    ta="you are good"
    time.sleep(2)
    print(ta)
c=threading.Thread(target=test(),args=(100,))
"""
b=threading.Thread(target=test(),args=(1,))
c=threading.Thread(target=test(),args=(1,))
a.start()
b.start()"""
c.start()
