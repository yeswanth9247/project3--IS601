""" Subtraction Tests """
# pylint disable=E1136
import os
import pandas as pd
import main as log

from calculator.calculations.subtraction import Subtraction

file_path = os.path.dirname(os.path.realpath(__file__))


def test_calculation_subtraction():
    """ testing csv subtraction functionality """
    #Arrange
    filename = "infile/Subtraction Data 1.csv"
    path = os.path.join(file_path, filename)
    d_frame = pd.read_csv(path)
    for i, row in d_frame.iterrows():
        values = (row.valuea, row.valueb)
        subtract = Subtraction.create(values)
        subtract_result = d_frame["valuec"][i]
        log.output_data(filename, row.valuea, "-", row.valueb, subtract_result)
        assert subtract.get_result() == subtract_result
    print("Your Subtraction CSV file has been verified successfully")
