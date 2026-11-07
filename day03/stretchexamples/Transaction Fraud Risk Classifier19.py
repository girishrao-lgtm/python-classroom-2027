'''
Transaction Fraud Risk Classifier
Difficulty: Hard

A payment system classifies a transaction as follows:
- BLOCK: amount exceeds ₹100,000, or the account is flagged
- REVIEW: amount exceeds ₹50,000, or the transaction is international and amount exceeds ₹20,000
- Otherwise: APPROVE
Input: Amount, international status (yes/no), flagged status (yes/no) on separate lines.

Output: BLOCK, REVIEW, APPROVE, or INVALID INPUT.
'''
amount = float(input())
international = input().strip().lower()
flagged = input().strip().lower()

if (
    amount <= 0
    or international not in ("yes", "no")
    or flagged not in ("yes", "no")
):
    print("INVALID INPUT")
elif amount > 100000 or flagged == "yes":
    print("BLOCK")
elif amount > 50000 or (
    international == "yes" and amount > 20000
):
    print("REVIEW")
else:
    print("APPROVE")