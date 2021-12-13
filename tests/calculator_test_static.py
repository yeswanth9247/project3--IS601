"""Testing the Calculator"""
import pytest
from calculator.history.calculations import Calculation
from calculator.calculations.addition import Addition
from calculator.calculations.subtraction import Subtraction
from calculator.calculations.multiplication import Multiplication
from calculator.calculations.division import Division


@pytest.fixture
def clear_history_fixture():
    """ clears history after each run """
    # pylint: disable=redefined-outer-name
    Calculation.empty_history()


def test_calculator_add_static(clear_history_fixture):
    """ tests the addition between 2 numbers """
    # pylint: disable=unused-argument,redefined-outer-name
    my_nums = (1.0, 2.0)
    addition = Addition(my_nums)
    assert addition.get_result() == 3.0


def test_calculator_subtract_static(clear_history_fixture):
    """Testing the subtract method of the calculator"""
    # pylint: disable=unused-argument,redefined-outer-name,too-many-function-args
    my_nums = (10.0, 5.0)
    subtraction = Subtraction(my_nums)
    assert subtraction.get_result() == 5.0


def test_calculator_multiply_static(clear_history_fixture):
    """ tests multiplication of two numbers"""
    # pylint: disable=unused-argument,redefined-outer-name,too-many-function-args
    my_nums = (4.0, 10.0)
    multiplication = Multiplication(my_nums)
    assert multiplication.get_result() == 40.0


def test_calculator_divide_static(clear_history_fixture):
    """ tests multiplication of two numbers"""
    # pylint: disable=unused-argument,redefined-outer-name,too-many-function-args
    my_nums = (10.0, 2.5)
    division = Division(my_nums)
    assert division.get_result() == 4.0


def test_calculator_division_exception():
    """ tests the divide by zero exception """
    # pylint: disable=redefined-outer-name,too-many-function-args
    my_nums = (10.0, 0)
    division = Division(my_nums)
    assert division.get_result() == "Error"
