'''
Exercise 01 — Smart Parking Fee Calculator
Difficulty: Easy

A parking facility charges ₹30 for the first hour and ₹20 for every additional started hour. If the vehicle stays more than 8 hours, the total charge is capped at ₹150.

Input: Parking duration in minutes, a positive integer.

Output: Total parking fee, or INVALID for nonpositive duration.
Input	Output
30	30
60	30
61	50
180	70
480	150
0	INVALID
'''
minutes = int(input())

if minutes <= 0:
    print("INVALID")
else:
    hours = (minutes + 59) // 60
    fee = 30 + (hours - 1) * 20

    if hours > 8:
        fee = min(fee, 150)

    print(fee)