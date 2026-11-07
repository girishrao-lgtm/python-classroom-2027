'''
Loan Eligibility Decision Engine
Difficulty: Hard

A bank approves a loan if the applicant is between 21 and 60 years old, has monthly income of at least ₹30,000, has a credit score of at least 700, and has existing monthly EMI obligations no greater than 40% of monthly income.

Input: Age, monthly income, credit score, and existing monthly EMI on separate lines.

Output: APPROVED, REJECTED, or INVALID INPUT.

'''
age = int(input())
income = float(input())
credit_score = int(input())
emi = float(input())

if (
    age < 0
    or income < 0
    or emi < 0
    or not (300 <= credit_score <= 900)
):
    print("INVALID INPUT")
elif (
    21 <= age <= 60
    and income >= 30000
    and credit_score >= 700
    and emi <= income * 0.40
):
    print("APPROVED")
else:
    print("REJECTED")