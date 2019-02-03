"""A haidata demonstration vehicle.

.. moduleauthor:: Hans Roggeman <hansroggeman2@gmail.com>

"""

import pandas as pd
import numpy as np

from haidata.haidatacfg import HaiDataCfg
from haidata.haidatautils import listify_strings
from haidata.haidatautils import slice_string_to_list
from haidata.haidatautils import to_int_list
from haidata.haidatautils import dicts_get

from haidata.fix_encode import fix_encode
from haidata.fix_colnames import fix_colnames
from haidata.fix_empty_cols import fix_empty_cols
from haidata.fix_excess_stdev import fix_excess_stdev
from haidata.to_datetime import to_datetime
from haidata.drop_cols import drop_cols

def start():
    # "This starts this module running ..."
    pass
