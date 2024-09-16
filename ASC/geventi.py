import gevent
from gevent import monkey
monkey.patch_all()

import time

def task1():
    print("Task 1 starting")
    gevent.sleep(1)
    print("Task 1 done")

def task2():
    print("Task 2 starting")
    gevent.sleep(2)
    print("Task 2 done")

def task3():
    print("Task 3 starting")
    gevent.sleep(3)
    print("Task 3 done")

gevent.joinall([
    gevent.spawn(task1),
    gevent.spawn(task2),
    gevent.spawn(task3)
])