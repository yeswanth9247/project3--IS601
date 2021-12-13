""" This is the increment function"""
from calculator.history.calculations import Calculation


class Calculator:
    """ This is the Calculator class"""

    @staticmethod
    def add_number(tuple_values: tuple):
        """ adds number to result"""
        Calculation.add_addition(tuple_values)
        return True

    @staticmethod
    def subtract_number(tuple_values: tuple):
        """ subtract number from result"""
        Calculation.add_subtraction(tuple_values)
        return True

    @staticmethod
    def multiply_numbers(tuple_values: tuple):
        """ multiply two numbers and store the result"""
        Calculation.add_multiplication(tuple_values)
        return True

    @staticmethod
    def divide_numbers(tuple_values: tuple):
        """divide two numbers and store the result"""
        Calculation.add_division(tuple_values)
        return True

    @staticmethod
    def get_last_calculation():
        """ Retrieving the last calculation stored """
        return Calculation.get_last_calc()
