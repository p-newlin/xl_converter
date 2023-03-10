""" __version__.py

The version file for the xl_convevrter application.
"""
import os
from pathlib import Path

version_txt_filename = Path(os.path.dirname(os.path.abspath(__file__))) / "version.txt"
VERSION = open(version_txt_filename).readline().strip()
