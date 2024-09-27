class Calculation:
    def __init__(self, operation, a, b):
        self.operation = operation
        self.a = a
        self.b = b

    def get_Output(self):
        return self.operation(self.a, self.b)