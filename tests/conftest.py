'''
This module will generate test data for basic arithmetic operations using Faker and decimal.
It will include the functionality of generating random numbers for test cases for operations
like addition, subtraction, multiplication and division along with error handling conditions
like DivideByzero.

'''
from decimal import Decimal
from faker import Faker
from calculator.operations import add, subtract, multiply, divide

fake = Faker()

def generate_test_data(num_of_records):
    '''
    This method will generate the test data for arithemetic operations. Each test case will 
    contain two decimal numbers and a randomly selected arithmetic operation along with the
    expected result of the operation. The function also will handle the cases where division
    by zero might occur.
    '''
    mappings = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }
    for _ in range(num_of_records):
        a = Decimal(fake.random_number(digits=2))
        b = Decimal(fake.random_number(digits=2)) if _ % 4 != 3 else Decimal(fake.random_number(digits=1))
        operation_name = fake.random_element(elements=list(mappings.keys()))
        operation_func = mappings[operation_name]
        if operation_func == "divide":
            b = Decimal('1') if b == Decimal('0') else b
        try:
            if operation_func == "divide" and b == Decimal('0'):
                expected = "ZeroDivisionError"
            else:
                expected = operation_func(a, b)
        except ZeroDivisionError:
            expected = "ZeroDivisionError"
        yield a, b, operation_name, operation_func, expected

def pytest_addoption(parser):
    '''
    This method will add a command line option for pytest to customize test data generation.
    '''
    parser.addoption("--num_records", action="store", default=5, type=int, help="Number of test records to generate")

def pytest_generate_tests(metafunc):
    '''
    To generate the parametrize tests for pytest based on the available fixture names and the
    number of records specified. This function will check if required fixtures are present to 
    generate test cases using the specified number of records.
    '''
    if {"a", "b", "expected"}.intersection(set(metafunc.fixturenames)):
        num_of_records = metafunc.config.getoption("num_records")
        parameters = list(generate_test_data(num_of_records))
        converted_parameters = [(a, b, op_name if 'operation_name' in metafunc.fixturenames else op_func, expected) for a, b, op_name, op_func, expected in parameters]
        metafunc.parametrize("a,b,operation,expected", converted_parameters)
