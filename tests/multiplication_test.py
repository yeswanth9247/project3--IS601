""" Multiplication Tests """
# pylint disable=E1136
import os
import pandas as pd
import main as log
from calculator.calculations.multiplication import Multiplication

file_path = os.path.dirname(os.path.realpath(__file__))


def test_calculation_multiplication():
    """ testing csv multiplication functionality """
    #Arrange
    filename = "infile/Multiplication Data 1.csv"
    path = os.path.join(file_path, filename)
    d_frame = pd.read_csv(path)
    for i, row in d_frame.iterrows():
        values = (row.valuea, row.valueb)
        multiply = Multiplication.create(values)
        multiply_result = d_frame["valuec"][i]
        log.output_data(filename, row.valuea, "*", row.valueb, multiply_result)
        assert multiply.get_result() == multiply_result
    print("Your Multiplication CSV file has been verified successfully")
