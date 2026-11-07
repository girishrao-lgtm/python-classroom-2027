cgpa = float(input("Enter CGPA: "))
attendance = float(input("Enter attendance %: "))
backlogs = int(input("Enter active backlogs: "))
coding_score = int(input("Enter coding score: "))

if not (
    0 <= cgpa <= 10
    and 0 <= attendance <= 100
    and backlogs >= 0
    and 0 <= coding_score <= 100
):
    print("Invalid input")

elif backlogs > 0:
    print("Not eligible: active backlogs")

elif cgpa < 7.0:
    print("Not eligible: CGPA below 7")

elif attendance < 75:
    print("Not eligible: attendance below 75%")

elif coding_score >= 80:
    print("Eligible: Priority Interview Track")

elif coding_score >= 60:
    print("Eligible: Standard Interview Track")

else:
    print("Coding improvement required")