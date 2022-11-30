# DATA CLEANING METHODS FOR IMPORTING ONLY
import re
import numpy as np


def single_dim_num_regex(data):
    """Pass in a string(Can be multiline) and receive back list of all data points. Works with decimals, and negative number. Only pulls single dim"""
    # values in list in string form
    raw = re.findall("[+-]?(?:\d*\.\d+|\d+)", data)

    # make each value a float
    floated = [float(x) for x in raw]

    return floated
