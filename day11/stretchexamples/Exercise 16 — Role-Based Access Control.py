'''
Exercise 16 — Role-Based Access Control
'''

from functools import wraps


def require_permissions(*required_permissions):

    def decorator(func):

        @wraps(func)
        def wrapper(user, *args, **kwargs):

            permissions = set(user["permissions"])

            if not set(required_permissions).issubset(permissions):
                raise PermissionError("Insufficient permissions")

            return func(user, *args, **kwargs)

        return wrapper

    return decorator

@require_permissions("read", "delete")
def delete_file(user, filename):
    return f"{filename} deleted"

admin = {
    "permissions": ["read", "write", "delete"]
}

viewer = {
    "permissions": ["read"]
}

print(delete_file(admin, "report.pdf"))

try:
    print(delete_file(viewer, "report.pdf"))
except PermissionError as error:
    print(error)