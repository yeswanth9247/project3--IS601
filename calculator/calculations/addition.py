""" adds two numbers """
from calculator.calculations.calculation import Calculation


class Addition(Calculation):
    """ adds two numbers """
    def get_result(self):
        """ adds two numbers """
        sum_of_vals = 0.0
        for value in self.values:
            sum_of_vals = float(value) + sum_of_vals
        return sum_of_vals
