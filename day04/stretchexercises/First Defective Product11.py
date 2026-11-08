'''
Stretch 11 — First Defective Product
A production line records product quality using 1 for good and 0 for defective. Find the first defective product.
'''

quality = [1, 1, 1, 1, 0, 1, 0, 1]

for index in range(len(quality)):

    if quality[index] == 0:
        print(f"First defective product at position {index + 1}")
        break

else:
    print("All products passed quality inspection")