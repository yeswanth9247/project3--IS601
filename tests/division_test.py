""" Division Tests """
# pylint disable=E1136
import os
import logging
import pandas as pd
import pytest
import main as log
from calculator.calculations.division import Division

file_path = os.path.dirname(os.path.realpath(__file__))

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
f = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S')
fhandler = logging.FileHandler('zeroexception.log')
fhandler.setFormatter(f)
logger.addHandler(fhandler)


def test_calculation_division():
    """ testing csv division functionality """
    # Arrange
    filename = "infile/Division Data 1.csv"
    path = os.path.join(file_path, filename)
    data_frame = pd.read_csv(path)
    for i, row in data_frame.iterrows():
        values = (row.valuea, row.valueb)
        divide = Division.create(values)
        try:
            # Assert
            divide_result = data_frame['valuec'][i]
            log.output_data(filename, row.valuea, "/", row.valueb, divide_result)
            assert divide.get_result() == divide_result
        except ZeroDivisionError:
            with pytest.raises(ZeroDivisionError):
                logger.error("Cannot divide by zero")
                assert divide.get_result() is True
    print("Your Division CSV file has been verified successfully")
