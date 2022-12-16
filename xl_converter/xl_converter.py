""" xl_converter.py

Module to convert distributed CSV files into single excel-formatted
workbook with multiple sheets.
"""

import pandas as pd
import xlsxwriter as xls
import numpy as np
import os
import argparse
from datetime import datetime
from typing import Any, List

# Create some useful command line arguments
argParser = argparse.ArgumentParser()
argParser.add_argument("directory")
args = argParser.parse_args

# TODO: create command line argument for data directory

# Get current time to use in filename + preserve duplicates
timestamp_format = '%Y%d%m_%H%M%S'
current_time = str(round(np.random.random(), 2))
current_time = datetime.now().strftime(timestamp_format)

class WriteExcel:
    '''Main function for converting multiple CSV files into an excel workbook
    with configurable parameters.
    '''

    def __init__(self, data_directory: str,
                filename = f"out_{current_time}",
                output_directory = 'output'):
        '''General function to instantiate the class.
        Checks for files then merges distributed outputs into an Excel workbook.
        :param data_directory: name of directory containing .csv data files
        :param args: list of arguments to be passed into subclass methods
        '''
        # TODO: Extendable through formatting module.
        # TODO: Read from config.yml

        self._path = os.getcwd()
        self._filename = filename
        self.manifest = []
        self.workbook = None
        self._data_directory = data_directory
        self.files = os.listdir(self._data_directory)
        self._output_dir = output_directory

    def convert_excel(self):
        self.manifest = self.generate_manifest()
        self.workbook = self.create_workbook()
        self.add_worksheets()
        self.workbook.close()
        print('workbook generated successfully!')

    def generate_manifest(self):
        ''' Function to create a manifest of all CSV files to be included
        in the conversion.
        '''
        for file in self.files:
          if file.endswith('.csv'):
            self.manifest.append(str(file))
        return self.manifest

    def add_worksheets(self):
        ''' Function to generate new worksheets from manifest.
        :param workbook: the workbook object created by create_workbook
        :param manifest: the list of files created by generate_manifest
        '''

        # TODO: make the presence of header row configurable

        for file in self.manifest:
            file_path = f"{self._data_directory}/{file}"
            temp_df = pd.read_csv(file_path)
            sheetname = str(file).replace('.csv', '')
            worksheet = self.workbook.add_worksheet(f"{sheetname}")
            c_iter = 0
            for c_index, column in enumerate(list(temp_df.columns)):
                field = list(temp_df[column])
                worksheet.write(0, c_iter, str(column))
                c_iter += 1
                r_iter = 1
                for r_index, element in enumerate(field, start = 1):
                    element = ['NA' if pd.isna(element) else element][0]
                    worksheet.write(r_iter, c_index, element)
                    r_iter += 1

    def create_workbook(self):
        ''' Function to generate an empty workbook. '''
        file_path = f'{self._output_dir}/{self._filename}.xlsx'
        self.workbook = xls.Workbook(file_path)
        return self.workbook

testinstance = WriteExcel('data/')
testinstance.convert_excel()
