'''
Stretch 12 — Move Zero Stock Items to the End
'''
stock = [0, 10, 0, 20, 30, 0, 40]

write = 0

for read in range(len(stock)):

    if stock[read] != 0:
        stock[write] = stock[read]
        write += 1

while write < len(stock):
    stock[write] = 0
    write += 1

print(f"Rearranged stock: {stock}")
