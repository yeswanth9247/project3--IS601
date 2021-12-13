""" divides two numbers """
from calculator.calculations.calculation import Calculation


class Division(Calculation):
    """ divides two numbers """
    def get_result(self):
        """ divides two numbers """
        division_values = self.values[0]
        for value in self.values[1:]:
            try:
                division_values = division_values / value
            except ZeroDivisionError:
                return "Error"
        return round(division_values, 6)
