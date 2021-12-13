""" subtracts two numbers """
from calculator.calculations.calculation import Calculation


class Subtraction(Calculation):
    """ subtracts two numbers """
    def get_result(self):
        """ subtracts two numbers """
        dif_of_vals = 0.0
        for index, value in enumerate(self.values):
            if index == 0:
                dif_of_vals = value
            else:
                dif_of_vals = dif_of_vals - float(value)
        return dif_of_vals
