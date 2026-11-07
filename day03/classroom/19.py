status = int(input("Enter HTTP status code: "))

match status:
    case 200:
        print("OK")
    case 201:
        print("Created")
    case 400:
        print("Bad Request")
    case 401 | 403:
        print("Access denied")
    case 404:
        print("Not Found")
    case 500:
        print("Internal Server Error")
    case _:
        print("Other status")