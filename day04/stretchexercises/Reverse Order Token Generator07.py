'''
Stretch 07 — Reverse Order Token Generator
Generate tokens from N down to 1, skipping numbers divisible by 4.
'''
n = int(input("Enter N: "))

for token in range(n, 0, -1):

    if token % 4 == 0:
        continue

    print(f"TOKEN-{token}")