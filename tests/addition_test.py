""" Addition Tests """
# pylint disable=E1136
import os
import logging
import pandas as pd
import main as log
from calculator.calculations.addition import Addition

file_path = os.path.dirname(os.path.realpath(__file__))


def test_calculation_addition():
    """ testing csv addition functionality """
    # Arrange
    filename = "infile/Addition Data 1.csv"
    path = os.path.join(file_path, filename)
    d_frame = pd.read_csv(path)
    print("Verify your CSV Addition files")
    for i, row in d_frame.iterrows():
        values = (row.valuea, row.valueb)
        add = Addition.create(values)
        add_result = d_frame["valuec"][i]
        log.output_data(filename, row.valuea, "+", row.valueb, add_result)
        logging.debug("Verified...")
        assert add.get_result() == add_result
    print("Your Addition CSV file has been verified successfully")
