'''
Dynamic Cab Fare Calculator
Difficulty: Hard

A cab service charges ₹50 base fare plus ₹12 per kilometre. During peak hours (8–10 AM and 6–9 PM), a 1.5× multiplier applies to the entire fare. If the distance exceeds 20 km, apply a 10% discount after the peak multiplier.

Input: Distance in kilometres and trip start hour (0–23) on separate lines.

Output: Final fare with two decimal places, or INVALID.

Assume peak hours are 8 ≤ hour < 10 and 18 ≤ hour < 21.
'''
distance = float(input())
hour = int(input())

if distance < 0 or not (0 <= hour <= 23):
    print("INVALID")
else:
    fare = 50 + distance * 12

    peak = (8 <= hour < 10) or (18 <= hour < 21)

    if peak:
        fare *= 1.5

    if distance > 20:
        fare *= 0.90

    print(f"{fare:.2f}")