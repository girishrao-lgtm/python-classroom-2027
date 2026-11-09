'''
Example 13 — Context Manager with Exception Handling
'''
class SafeTransaction:

    def __enter__(self):
        print("Transaction started")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            print("Transaction committed")
        else:
            print("Transaction rolled back")

        return False


try:
    with SafeTransaction():
        print("Updating records")
        raise ValueError("Database update failed")

except ValueError as error:
    print("Caller received:", error)