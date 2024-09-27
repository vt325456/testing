from calculator.operations import add, subtract, divide, multiply
from calculator.Calculation import Calculation
from calculator.History import History

class Calculator:

    @staticmethod
    def _do_operate(a, b, operation):
        calculation = Calculation.create(a, b, operation)
        Calculationhistory.add_history(calculation)
        return calculation.operate()
    
    @staticmethod
    def add(a, b):
        return Calculator._do_operate(a,b,add)
    
    @staticmethod
    def subtract(a, b):
        return Calculator._do_operate(a,b,subtract)

    @staticmethod
    def multiply(a, b):
        return Calculator._do_operate(a,b,multiply)
    
    @staticmethod
    def divide(a, b):
        return Calculator._do_operate(a,b,divide)