'''
Stretch 05 — Customer Waiting Queue
'''
queue = ["Amit", "Ravi", "Neha", "Priya"]

print(f"Initial queue: {queue}")

new_customer = input("New customer: ")
queue.append(new_customer)

if queue:
    served = queue.pop(0)
    print(f"Served: {served}")

print(f"Remaining queue: {queue}")