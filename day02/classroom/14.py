samples = ["Python", "12345", "Python123", "   ", ""]

for s in samples:
    print(
        repr(s),
        s.isalpha(),
        s.isdigit(),
        s.isalnum(),
        s.isspace()
    )