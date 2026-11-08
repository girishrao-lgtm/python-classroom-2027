'''
Exercise 14 — Round-Robin Task Scheduler
'''

from itertools import cycle, islice

tasks = ["Task-A", "Task-B", "Task-C"]

scheduler = cycle(tasks)

schedule = list(islice(scheduler, 10))

for slot, task in enumerate(schedule, 1):
    print(slot, task)