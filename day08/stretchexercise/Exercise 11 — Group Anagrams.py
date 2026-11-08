'''
Exercise 11 — Group Anagrams
'''
words = ["eat", "tea", "tan", "ate", "nat", "bat"]

groups = {}

for word in words:
    key = tuple(sorted(word))

    if key not in groups:
        groups[key] = []

    groups[key].append(word)

print(list(groups.values()))