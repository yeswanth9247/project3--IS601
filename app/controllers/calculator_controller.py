# pylint: disable=no-name-in-module, import-error
""" Calculator controller """
from flask import render_template, request, flash
from app.controllers.controller import ControllerBase
from calculator.calculator import Calculator
from CSV_to_table.csv_table import TableBuilder


class CalculatorController(ControllerBase):
    """ Calculator controller """
    @staticmethod
    def post():
        """ Posts finished calculation """
        if request.form['valuea'] == '' or request.form['valueb'] == '':
            error = 'You need at least one value filled out, try again!'
        else:
            flash('flashed message')
            # get the values out of the form
            valuea = request.form['valuea']
            valueb = request.form['valueb']
            operation = request.form['operation']
            # make the tuple
            my_tuple = (valuea, valueb)
            # this will call the correct operation
            getattr(Calculator, operation)(my_tuple)
            valuec = str(Calculator.get_last_calculation())
            TableBuilder.add_row(operation, valuea, valueb, valuec)
            return render_template('calculator.html', valuea=valuea, valueb=valueb, operation=operation,
                                   valuec=valuec)

        return render_template('calculator.html', error=error)

    @staticmethod
    def get():
        """ returns calculator """
        return render_template('calculator.html')
