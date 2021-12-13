""" Testing Calculator """
import pytest
from calculator.history.calculations import Calculation
from calculator.calculations.multiplication import Multiplication


@pytest.fixture(name="clear_history_fixture")
def clear_history_fixture():
    """ Clears history after each run """
    Calculation.empty_history()


@pytest.fixture(name="setup_multiplication_calc_fixture")
def setup_multiplication_calc_fixture():
    """ Runs each time a test is passed through it """
    # pylint: disable=redefined-outer-name
    my_nums = (2.0, 5.0)
    multiply = Multiplication(my_nums)
    Calculation.add_to_history(multiply)


def add_calc_to_history_test(clear_history_fixture, setup_multiplication_calc_fixture):
    """ Testing if calculations are added """
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert Calculation.history_count() == 1


def clear_history_calculation_test(clear_history_fixture, setup_multiplication_calc_fixture):
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    """ testing if history can be cleared """
    assert Calculation.history_count() == 1
    Calculation.empty_history()
    assert Calculation.history_count() == 0
    assert Calculation.empty_history() is True


def get_calculation_test(clear_history_fixture, setup_multiplication_calc_fixture):
    """ Testing if it is possible to get a specific calculation from the history """
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculation.get_calculation(0).get_result() == 10.0


def get_last_calculation_test(clear_history_fixture, setup_multiplication_calc_fixture):
    """ testing obtaining the last calculation from history """
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculation.last_calc_to_history().get_result() == 10.0


def get_first_calculation_test(clear_history_fixture, setup_multiplication_calc_fixture):
    """ testing obtaining the first calculation from history """
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculation.first_calc_to_history().get_result() == 10.0


def history_count_test(clear_history_fixture, setup_multiplication_calc_fixture):
    """ testing if history is tracking calculations """
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculation.history_count() == 1


def get_last_value(clear_history_fixture, setup_multiplication_calc_fixture):
    """ Testing if the identity of the last calculation is stored """
    # pylint: disable=unused-argument,redefined-outer-name
    assert isinstance(Calculation.get_last_calc(), Multiplication)
