'''
Triangle Validity and Classification
Difficulty: Medium

Given three integer side lengths, determine whether they form a valid triangle. A valid triangle has positive sides and satisfies all three triangle inequalities.

If valid, classify it as EQUILATERAL, ISOSCELES, or SCALENE. Otherwise print INVALID.

Input: Three side lengths on separate lines.
'''
a = int(input())
b = int(input())
c = int(input())

if (
    a <= 0
    or b <= 0
    or c <= 0
    or a + b <= c
    or a + c <= b
    or b + c <= a
):
    print("INVALID")
elif a == b == c:
    print("EQUILATERAL")
elif a == b or b == c or a == c:
    print("ISOSCELES")
else:
    print("SCALENE")