'''
Exercise 05 — Nested Tuple Scoreboard
'''
players = (
    ("Amit", (80, 90, 85)),
    ("Neha", (95, 85, 90)),
    ("Ravi", (80, 90, 85)),
    ("Priya", (90, 92, 91))
)

scores = []

for name, rounds in players:
    scores.append((name, sum(rounds)))

scores.sort(key=lambda x: (-x[1], x[0]))

for rank, (name, score) in enumerate(scores, 1):
    print(rank, name, score)
    