class Calculation:
    def __init__(self, a, b, operation):
        self.operation = operation
        self.a = a
        self.b = b

    def get_Output(self):
        return self.operation(self.a, self.b)