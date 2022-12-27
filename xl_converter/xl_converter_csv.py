""" xl_converter_csv.py

Module to convert formatted .xlsx files into multiple plaintext .csv's.
"""

import pandas as pd
import xlsxwriter as xls
import numpy as np
import os
import argparse
from datetime import datetime
from typing import Any, List
from glob import glob

# Create some useful command line arguments
argParser = argparse.ArgumentParser()
argParser.add_argument("directory")
args = argParser.parse_args

# TODO: create command line argument for data directory

# Get current time to use in filename + preserve duplicates
timestamp_format = '%Y%d%m_%H%M%S'
current_time = str(round(np.random.random(), 2))
current_time = datetime.now().strftime(timestamp_format)

class WriteCSV:
    ''' Main function for converting a formatted .xlsx workbook into
    mutliple plaintext .csv's.
    '''
    
    def __init__(self, data_directory: str,
                filename = f"out_{current_time}",
                output_directory = 'output'):
        '''General function to instantiate the class.
        Checks for files then distributes outputs as .csv's.
        :param data_directory: name of directory containing .xlsx data files
        :param filename:
        :param output_directory:
        '''

        self._path = os.getcwd()
        self._filename = filename
        self.manifest = []
        
        #self.workbook = None
        
        self._data_directory = data_directory
        self.files = os.listdir(self._data_directory)
        self._output_dir = output_directory

class WorksheetManifest:

    

    def create_worksheet_iterator():
        ''' Iterator object to read all worksheets in a workbook when number of sheets is not known. '''
    
        workbook = load_workbook("your path")
        sheet = workbook.worksheets[1]

    #function to correctly format date column
    def convert_header(self):
        for column in self.analysis
        s=s.split('-')
        yr=int(s[0])
        m=int(s[1])
        months=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        m=months[m-1]
        yr=yr-2000
        return str(yr)+'-'+m

#function to read through excel folder and make csv in same folder
for excel_file in glob(read_path):
    print(excel_file)
    df = pd.read_excel(excel_file)
    col = df.columns.tolist()
    strcol = [x for x in col if isinstance(x, str)]
    lowstr = [x.lower() for x in strcol]
    if (any("deps" in s for s in lowstr)) or (any("equip" in s for s in lowstr)) or (not any("fleet" in s for s in lowstr)) : #interim station stats file (deps) or subfleet reference (equip) has fleet but doesn't need special date formatting, anything without fleet has no special formattting
        csv_file = os.path.splitext(excel_file)[0] + '.csv'
        df.to_csv(csv_file, index=None, header=True)
    else : #all remaining files should have fleet/fleet seat and then YY-Mon as columns
        if 'category' in lowstr : #prior RL file has fleet wtih YY-Mon format but an extra column in front
            df.rename(columns={ df.columns[1]: "fleet_seat" }, inplace = True) #force capitalization to be the same on all
            df = df.set_index(['Category','fleet_seat'])
        else:
            df.rename(columns={ df.columns[0]: "fleet_seat" }, inplace = True) #force capitalization to be the same on all
            df = df.set_index(df.columns[0])
        init_columns=df.columns
        for i in init_columns:
            df=df.rename(columns={i:convert_header(str(i))})
        csv_file = os.path.splitext(excel_file)[0] + '.csv'
        df.to_csv(csv_file, index=True, header=True)
