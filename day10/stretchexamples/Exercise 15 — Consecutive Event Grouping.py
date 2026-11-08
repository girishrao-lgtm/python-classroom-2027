'''
Exercise 15 — Consecutive Event Grouping
'''

from itertools import groupby

events = [
    "SUCCESS",
    "SUCCESS",
    "FAILED",
    "FAILED",
    "FAILED",
    "SUCCESS",
    "FAILED"
]

for status, group in groupby(events):
    count = sum(1 for _ in group)
    print(status, count)