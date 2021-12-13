""" Calculation History Class """
from calculator.calculations.addition import Addition
from calculator.calculations.division import Division
from calculator.calculations.multiplication import Multiplication
from calculator.calculations.subtraction import Subtraction


class Calculation:
    """ Calculation History Class """
    history = []
    # pylint: disable=too-few-public-methods
    @staticmethod
    def empty_history():
        """ clears history function """
        Calculation.history.clear()
        return True


    @staticmethod
    def add_to_history(calculation):
        """ adds the calculation to history when called """
        return Calculation.history.append(calculation)


    @staticmethod
    def history_count():
        """ however many calculations have been stored in the array """
        return len(Calculation.history)


    @staticmethod
    def get_calculation(num):
        """ calling the previous calculation """
        return Calculation.history[num]


    @staticmethod
    def last_calc_to_history():
        """ returns the last calc in the array """
        return Calculation.history[-1]


    @staticmethod
    def first_calc_to_history():
        """ adds the first calculation to history """
        return Calculation.history[0]


    @staticmethod
    def get_last_calc():
        """ Returns the last calculation stored """
        last_calc = Calculation.last_calc_to_history()
        return last_calc.get_result()


    @staticmethod
    def get_first_calc():
        """ Returns the first calculation stored """
        return Calculation.history[0]


    @staticmethod
    def add_addition(values):
        """ Method to add new calculations into history """
        Calculation.add_to_history(Addition.create(values))
        return True

    @staticmethod
    def add_subtraction(values):
        """ Method to add new calculations into history """
        Calculation.add_to_history(Subtraction.create(values))
        return True

    @staticmethod
    def add_multiplication(values):
        """ Method to add new calculations into history """
        Calculation.add_to_history(Multiplication.create(values))
        return True

    @staticmethod
    def add_division(values):
        """ Method to add new calculations into history """
        Calculation.add_to_history(Division.create(values))
        return True
