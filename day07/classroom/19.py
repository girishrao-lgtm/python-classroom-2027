'''
Example 19 — First Repeated Element and Distinct Counts
'''
numbers = [5, 3, 8, 3, 9, 5, 2]

seen = set()
first_repeated = None

for x in numbers:
    if x in seen:
        first_repeated = x
        break

    seen.add(x)

print("First repeated:", first_repeated)
print("Distinct count:", len(set(numbers)))

prefix_seen = set()

for x in numbers:
    prefix_seen.add(x)
    print(f"After {x}: {len(prefix_seen)} distinct")
    