from calculator.Calculation import Calculation
from calculator import Calculator
from typing import List

class History:
    history = List[Calculator] = []

    @classmethod
    def history_add(cls,Calculation: Calculation):
        cls.history.append(Calculation)
    
    @classmethod
    def history_latest(cls):
        if cls.history:
            return cls.history[-1]
        return None
    
    @classmethod
    def history_clear(cls):
        cls.history.clear()
        
    @classmethod
    def history_print(cls) -> List[Calculation]:
        return cls.history
    
    
    @classmethod
    def history_get_operation(cls, operation_name:str) -> List[Calculation]:
        return [calc_obj for calc_obj in cls.history if i.operation.__name__ == operation_name]