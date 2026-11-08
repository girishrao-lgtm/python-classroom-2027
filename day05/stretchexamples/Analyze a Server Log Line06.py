'''
Stretch 06 — Analyze a Server Log Line
A server log contains a message such as ERROR: Database connection failed. Determine its severity using the beginning of the line, ignoring case.
'''

log = input("Enter log message: ").strip()

normalized = log.upper()

if normalized.startswith("ERROR:"):
    print("Severity = HIGH")

elif normalized.startswith("WARNING:"):
    print("Severity = MEDIUM")

elif normalized.startswith("INFO:"):
    print("Severity = LOW")

else:
    print("Severity = UNKNOWN")