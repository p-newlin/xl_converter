""" main.py

Main function for the xl_converter application.
"""

import argparse
import faulthandler
import logging
import os
import sys
import threading
from importlib import util

def main():
    ''' The main method for the xl_converter application. This method will be called from
        __main__.py when xl_converter is started.
    This method is responsible for starting all configured xl_converter plugins.
    '''
    parse = argparse.ArgumentParser(description = 'XL Converter Utility Casserole')
    
    parser.add_argument("-cfg", "--config",
                        type = str
                        required = False
                        help = "The XL Converter config file to use.")
    parser.add_argument("-lc", "--log_config",
                        required = False,
                        default = '',
                        help = "Sets logging configuration file location. Must be a .yml file.")
    
    args = parser.parse_args()
    
    # Conditionally create configuration path per args
    config_path = args.config if args.config \
        else os.path.abspath(os.path.join(os.path.dirname(__file__), 'config'))
    
    # Instantiate global config option
    # TODO: define load_config method to parse .yml configuration file
    global _config
    _config = load_config(config_path=config_path, config_filename="xlconverter.yml")
    
    # Funciton to define logging parameters per config
    # TODO: define setup_logging method to initialize logger per config
    setup_logging(_config)
    
    
