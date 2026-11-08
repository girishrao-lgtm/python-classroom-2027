'''
Example 03 — Nested Functions and Lexical Scope
'''
def outer():
    message = "Outer function"

    def inner():
        print(message)

    inner()

outer()