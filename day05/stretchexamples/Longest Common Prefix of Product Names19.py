'''
Stretch 19 — Longest Common Prefix of Product Names
Given several product names, determine their longest common prefix.
'''

products = [
    "programming",
    "programmer",
    "program",
    "progress"
]

if not products:
    print("No products")

else:
    prefix = products[0]

    for product in products[1:]:

        i = 0

        while (
            i < len(prefix)
            and i < len(product)
            and prefix[i] == product[i]
        ):
            i += 1

        prefix = prefix[:i]

        if prefix == "":
            break

    print(f"Longest common prefix = {prefix}")