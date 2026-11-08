'''
Exercise 12 — Missing Roll Numbers
'''
start = 101
end = 110

present = {101, 102, 104, 106, 107, 110}

expected = set(range(start, end + 1))

missing = expected - present

print("Missing roll numbers:", sorted(missing))
print("Missing count:", len(missing))