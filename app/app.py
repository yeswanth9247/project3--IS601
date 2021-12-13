""" A simple flask web app """
# pylint: disable=no-name-in-module, import-error
import sys
import os
from flask import Flask, request

from app.controllers.index_controller import IndexController
from app.controllers.calculator_controller import CalculatorController
from app.controllers.data_table_controller import DataTableController
from app.controllers.webpage_controller import AboutController, AAAController, PIEAController, \
    SeparationOfConcernsController, aaaController, webserverController, w3cController, historyController, \
    httpController, dotcombubbleController, contactusController, internethistoryController, ipanddnsController, \
    oopController, oopincalController, pylintController, seperationController, browserwarsController

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


parent_dir = os.getcwd()
path = os.path.dirname(parent_dir)
sys.path.append(parent_dir)


@app.route("/", methods=['GET'])
def index_get():
    """ Returns index """
    return IndexController.get()


@app.route("/calculator", methods=['GET'])
def calculator_get():
    """ Returns calculator """
    return CalculatorController.get()


@app.route("/calculator", methods=['POST'])
def calculator_post():
    """ Returns calculator results """
    return CalculatorController.post()


@app.route("/data_table", methods=['GET', 'POST'])
def data_table():
    """ Results Table Route """
    if request.method == 'POST':
        return DataTableController.post()
    return DataTableController.get()


@app.route("/about", methods=['GET'])
def about_get():
    """ Returns about """
    return AboutController.get()


@app.route("/aaa", methods=['GET'])
def aaa_get():
    """ returns aaa  """
    return aaaController.get()


@app.route("/arpanet", methods=['GET'])
def arpanet_get(arpanetController=None):
    """ returns arpanet """
    return arpanetController.get()


@app.route("/browserwars", methods=['GET'])
def separationofconcerns_get():
    """ returns separation of concerns """
    return browserwarsController.get()


@app.route("/contactus", methods=['GET'])
def contactus_get():
    """ returns contactus """
    return contactusController.get()

@app.route("/dotcombubble", methods=['GET'])
def dotcombubble_get():
    """ returns dotcombubble """
    return dotcombubbleController.get()

@app.route("/history", methods=['GET'])
def history_get():
    """ returns history """
    return historyController.get()

@app.route("/http", methods=['GET'])
def http_get():
    """ returns http """
    return httpController.get()

@app.route("/internethistory", methods=['GET'])
def internethistory_get():
    """ returns internethistory """
    return internethistoryController.get()

@app.route("/ipanddns", methods=['GET'])
def ipanddns_get():
    """ returns ipanddns """
    return ipanddnsController.get()

@app.route("/oop", methods=['GET'])
def oop_get():
    """ returns oop """
    return oopController.get()

@app.route("/oopincal", methods=['GET'])
def oopincal_get():
    """ returns oopincal """
    return oopincalController.get()

@app.route("/pylint", methods=['GET'])
def pylint_get():
    """ returns pylint """
    return pylintController.get()

@app.route("/seperation", methods=['GET'])
def seperation_get():
    """ returns seperation """
    return seperationController.get()

@app.route("/tcpip", methods=['GET'])
def tcpip_get(tcpipController=None):
    """ returns tcpip """
    return tcpipController.get()

@app.route("/w3c", methods=['GET'])
def w3c_get():
    """ returns w3c """
    return w3cController.get()

@app.route("/webserver", methods=['GET'])
def webserver_get():
    """ returns webserver """
    return webserverController.get()
