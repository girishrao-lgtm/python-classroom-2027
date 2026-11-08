'''
Example 18 — Common and Unique Elements Across Collections
'''
a = [1, 2, 3, 4, 5, 5]
b = [3, 4, 5, 6, 7]
c = [4, 5, 7, 8, 9]

sa = set(a)
sb = set(b)
sc = set(c)

common = sa & sb & sc
print("Common to all:", common)

all_values = sa | sb | sc
print("All distinct:", all_values)

only_a = sa - sb - sc
print("Only in A:", only_a)

exactly_one = (
    (sa - sb - sc)
    | (sb - sa - sc)
    | (sc - sa - sb)
)

print("Exactly one collection:", exactly_one)