'''
Hospital Patient Priority Classification
Difficulty: Medium

A hospital assigns priority using these rules, in order:
- Oxygen saturation below 90%: CRITICAL
- Otherwise, heart rate below 50 or above 120: HIGH
- Otherwise, age at least 65 and temperature at least 38°C: MEDIUM
- Otherwise: NORMAL
Input: Age, heart rate, oxygen saturation, and temperature on separate lines.

Output: Priority or INVALID for age outside 0–120, heart rate outside 1–250, oxygen saturation outside 0–100, or temperature outside 30–45°C.

'''
age = int(input())
heart_rate = int(input())
oxygen = int(input())
temperature = float(input())

if not (
    0 <= age <= 120
    and 1 <= heart_rate <= 250
    and 0 <= oxygen <= 100
    and 30 <= temperature <= 45
):
    print("INVALID")
elif oxygen < 90:
    print("CRITICAL")
elif heart_rate < 50 or heart_rate > 120:
    print("HIGH")
elif age >= 65 and temperature >= 38:
    print("MEDIUM")
else:
    print("NORMAL")