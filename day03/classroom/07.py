
values = [
    0, 1, -5,
    "", "Python",
    [], [10],
    {}, {"a": 1},
    None, False, True
]

for value in values:
    print(f"{value!r:20} -> {bool(value)}")