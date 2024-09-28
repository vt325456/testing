"""
Calculations Class
------------------

This is a Calculations class which manages a history of calculations that are made. The class holds methods to perform history management operations like add, getlatest,
delete, print, get the list of operations by operations 
"""
from calculator.Calculation import Calculation
from typing import List,Callable

class Calculations:
    history = [] # This list holds the history of calculations.

    @classmethod
    def history_add(cls,Calculation: Calculation):
        '''
        This method is used to add the calculation into the history list. It takes Calculation instance as argument.
        '''
        cls.history.append(Calculation)
    
    @classmethod
    def history_latest(cls):
        '''
        This method returns the most recent transaction if the history exists or else it will return None.
        '''
        if cls.history:
            return cls.history[-1]
        return None
    
    @classmethod
    def history_clear(cls):
        '''
        This method will be used to clear the history by calling clear() method.
        '''
        cls.history.clear()
        
    @classmethod
    def history_print(cls) -> List[Calculation]:
        '''
        This method will return the list of operations that are present in the history list.
        '''
        return cls.history
    
    @classmethod
    def history_get_operation(cls, operation_name:str) -> List[Calculation]:
        '''
        This method filters out the operations using operation_name from the list of history and returns the List[Calculation].
        '''
        return [calc_obj for calc_obj in cls.history if calc_obj.operation.__name__ == operation_name]