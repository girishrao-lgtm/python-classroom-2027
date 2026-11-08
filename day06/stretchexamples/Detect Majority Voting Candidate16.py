'''
Stretch 16 — Detect Majority Voting Candidate
'''

votes = [2, 2, 1, 2, 3, 2, 2]

candidate = None
count = 0

for vote in votes:

    if count == 0:
        candidate = vote
        count = 1

    elif vote == candidate:
        count += 1

    else:
        count -= 1

frequency = 0

for vote in votes:
    if vote == candidate:
        frequency += 1

if frequency > len(votes) // 2:
    print(f"Majority candidate: {candidate}")
else:
    print("No majority candidate")