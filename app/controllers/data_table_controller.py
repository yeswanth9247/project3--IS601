""" Data Table Controller """
# pylint: disable=no-name-in-module, import-error, too-few-public-methods
from flask import render_template
from app.controllers.controller import ControllerBase
from CSV_to_table.csv_table import TableBuilder


class DataTableController(ControllerBase):
    """ Data Table Controller """
    @staticmethod
    def get():
        """ Data Table Controller """
        return render_template('data_table.html', data=TableBuilder.csv_to_table())
