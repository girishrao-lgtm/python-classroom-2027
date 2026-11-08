'''
Exercise 09 — Diamond Inheritance and Cooperative super()
'''

class Base:

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("Base initialized")


class LoggerMixin(Base):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("Logger initialized")


class ValidatorMixin(Base):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("Validator initialized")


class Service(LoggerMixin, ValidatorMixin):

    def __init__(self):
        super().__init__()
        print("Service initialized")


service = Service()

print([cls.__name__ for cls in Service.mro()])
