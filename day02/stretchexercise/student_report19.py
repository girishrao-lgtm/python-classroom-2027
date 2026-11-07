name1 = input("Enter first student name: ")
score1 = float(input("Enter first score: "))

name2 = input("Enter second student name: ")
score2 = float(input("Enter second score: "))

print(f"{'Student':<20}{'Score':>10}")
print("-" * 30)

print(f"{name1:<20}{score1:>10.2f}")
print(f"{name2:<20}{score2:>10.2f}")