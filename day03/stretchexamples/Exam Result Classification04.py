'''
Exam Result Classification
Difficulty: Easy

A student takes three subjects, each marked out of 100. Passing requires at least 40 in every subject. A passing student receives DISTINCTION if the average is at least 75, otherwise PASS. If any subject is below 40, print FAIL.

Reject marks outside 0–100.

Input: Three integer marks on separate lines.

Output: DISTINCTION, PASS, FAIL, or INVALID.
'''
m1 = int(input())
m2 = int(input())
m3 = int(input())

if not (0 <= m1 <= 100 and 0 <= m2 <= 100 and 0 <= m3 <= 100):
    print("INVALID")
elif m1 < 40 or m2 < 40 or m3 < 40:
    print("FAIL")
else:
    average = (m1 + m2 + m3) / 3

    if average >= 75:
        print("DISTINCTION")
    else:
        print("PASS")