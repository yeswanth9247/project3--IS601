""" sets up the program to perform calculations """
class Calculation: # pylint: disable=too-few-public-methods
    """ constructor, first function called """
    def __init__(self, values: tuple):
        self.values = Calculation.convert_args_to_list_float(values)

    @classmethod
    def create(cls, values: tuple):
        """ Factory method for creating values for each calculation  """
        return cls(values)

    @staticmethod
    def convert_args_to_list_float(values):
        """ make a list of floats """
        list_vals_float = []
        for element in values:
            list_vals_float.append(float(element))
        return tuple(list_vals_float)
