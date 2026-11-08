'''
Example 07 — Decorator Syntax Using @
'''

def decorator(func):

    def wrapper():
        print("Starting")
        func()
        print("Finished")

    return wrapper

@decorator
def process():
    print("Processing data")

process()
