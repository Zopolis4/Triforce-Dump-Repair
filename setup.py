import argparse
import bsdiff4
import os
import py2exe
import hashlib as hash
from pathlib import Path
from distutils.core import setup

patch_files = []
for files in os.listdir(os.path.join(os.getcwd(), "Patches")):
    file = os.path.join(os.getcwd(), "Patches\\") + files
    patch_files.append(file)

setup(
    name = "Triforce Dump Repair",
    version = "1.0",
    description = "A tool to repair and rename Triforce dumps",
    author = "Zopolis4",
    console = ['triforcedumprepair.py'],
    data_files = patch_files
	)
