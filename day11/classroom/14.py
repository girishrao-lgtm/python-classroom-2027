'''
Example 14 — Authorization Decorator
'''
from functools import wraps


def require_role(required_role):

    def decorator(func):

        @wraps(func)
        def wrapper(user, *args, **kwargs):

            if required_role not in user["roles"]:
                raise PermissionError("Access denied")

            return func(user, *args, **kwargs)

        return wrapper

    return decorator

@require_role("admin")
def delete_record(user, record_id):
    return f"Deleted record {record_id}"

admin = {"roles": ["admin", "editor"]}
student = {"roles": ["student"]}

print(delete_record(admin, 101))

try:
    print(delete_record(student, 101))
except PermissionError as error:
    print(error)