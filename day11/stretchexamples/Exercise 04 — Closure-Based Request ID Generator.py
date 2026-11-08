'''
Exercise 04 — Closure-Based Request ID Generator

'''
def request_id_generator(prefix):

    counter = 0

    def generate():
        nonlocal counter
        counter += 1

        return f"{prefix}-{counter:05d}"

    return generate

api_ids = request_id_generator("API")
order_ids = request_id_generator("ORD")

print(api_ids())
print(api_ids())

print(order_ids())
print(order_ids())