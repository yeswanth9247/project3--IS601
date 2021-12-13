""" Index Controller """
# pylint: disable=no-name-in-module, import-error, too-few-public-methods
from flask import render_template
from app.controllers.controller import ControllerBase


class IndexController(ControllerBase):
    """ Index Controller """
    @staticmethod
    def get():
        """ Index Controller """
        return render_template('index.html')
