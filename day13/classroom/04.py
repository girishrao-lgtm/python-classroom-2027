'''
Example 04 — try, except, else and finally
'''
def process_number(value):
    try:
        number = int(value)
        result = 100 / number

    except ValueError:
        print("Invalid integer")

    except ZeroDivisionError:
        print("Division by zero")

    else:
        print("Success:", result)

    finally:
        print("Processing completed")


process_number("10")
process_number("0")
process_number("abc")