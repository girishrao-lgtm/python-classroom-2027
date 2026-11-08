'''
Example 15 — Subsets, Supersets and Disjoint Sets
'''
required = {"read", "write"}
user = {"read", "write", "execute"}

print(required.issubset(user))
print(user.issuperset(required))

print(required <= user)
print(user >= required)

a = {1, 2, 3}
b = {4, 5, 6}
c = {3, 4, 5}

print(a.isdisjoint(b))
print(a.isdisjoint(c))

print({1, 2} < {1, 2, 3})