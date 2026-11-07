text = "Python ₹"

encoded = text.encode("utf-8")
decoded = encoded.decode("utf-8")

print(encoded)
print(decoded)
print(type(encoded))
print(len(text))
print(len(encoded))