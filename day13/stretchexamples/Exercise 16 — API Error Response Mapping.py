'''
Exercise 16 — API Error Response Mapping
'''

class APIError(Exception):
    status_code = 500
    error_code = "INTERNAL_ERROR"


class ValidationError(APIError):
    status_code = 400
    error_code = "VALIDATION_ERROR"


class AuthenticationError(APIError):
    status_code = 401
    error_code = "AUTHENTICATION_ERROR"


class ResourceNotFoundError(APIError):
    status_code = 404
    error_code = "NOT_FOUND"


def handle_request(operation):
    try:
        result = operation()

        return {
            "status": 200,
            "data": result
        }

    except APIError as error:
        return {
            "status": error.status_code,
            "error": {
                "code": error.error_code,
                "message": str(error)
            }
        }


def get_student():
    raise ResourceNotFoundError("Student not found")


print(handle_request(get_student))