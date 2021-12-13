""" Creates a CSV file from user input """
import os
import pandas as pd


class TableBuilder:
    """ Takes user input and puts it into CSV """

    @staticmethod
    def add_row(operation, valuea, valueb, valuec):
        """ Creates a row per calculation """
        add_row = pd.DataFrame({'Value1': [valuea], 'Value2': [valueb], 'Operation': [operation],
                                'Result': [valuec]})
        script_dir = os.path.dirname(os.path.abspath(__file__))

        with open(script_dir+'/results.csv', 'a') as file:
            if file.tell() <= 31:
                add_row.index += 1
                add_row.to_csv(file, header=True)
            else:
                current = pd.read_csv(script_dir + '/results.csv')
                add_row.index += len(current.index) + 1
                add_row.to_csv(file, mode='a', header=False)

    @staticmethod
    def csv_to_table():
        """ Converts in_data to dictionary """
        in_data = pd.read_csv(os.path.dirname(os.path.abspath(__file__)) + "/results.csv")
        calculation = {"record": [], "valuea": [], "valueb": [], "operation": [], "valuec": []}
        for i in range(len(in_data)):
            calculation["record"].append(in_data.iloc[i]["Unnamed: 0"])
            calculation["valuea"].append(in_data.iloc[i]["Value1"])
            calculation["valueb"].append(in_data.iloc[i]["Value2"])
            calculation["operation"].append(in_data.iloc[i]["Operation"])
            calculation["valuec"].append(in_data.iloc[i]["Result"])
        return calculation
