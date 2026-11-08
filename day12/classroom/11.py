'''
Example 11 — Multiple Inheritance and Method Resolution Order
'''
class A:

    def process(self):
        print("A")


class B(A):

    def process(self):
        print("B before")
        super().process()
        print("B after")


class C(A):

    def process(self):
        print("C before")
        super().process()
        print("C after")


class D(B, C):

    def process(self):
        print("D before")
        super().process()
        print("D after")


obj = D()

obj.process()

print([cls.__name__ for cls in D.__mro__])