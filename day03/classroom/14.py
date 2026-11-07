role = input("Enter role: ").strip().lower()

allowed_roles = ("admin", "editor", "viewer")

if role in allowed_roles:
    print("Recognized role")
else:
    print("Unknown role")

if role not in ("admin", "editor"):
    print("Write access unavailable")