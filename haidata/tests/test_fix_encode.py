# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 02:14:56 2018

@author: HansT
"""

import sys, os
import pandas as pd
import copy
from pandas.util.testing import assert_frame_equal

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from fix_encode import fix_encode
from haidatacfg import HaiDataCfg


def test_fix_encode():
    test_file1 = os.path.join(HaiDataCfg.get_path(), '../../../../', 'data', 'examples', 'moma_art', 'artists.csv')
    df_input_original = pd.read_csv(test_file1) if os.path.isfile(test_file1) else None
    df_input = copy.deepcopy(df_input_original)
    fix_encode_dict = dict({"TYPE": ["string"]})

    df_input1 = fix_encode(df_input, fix_encode_dict)
    print(df_input1.head(4))
    try:
        assert_frame_equal(df_input1.head(7), df_input_original.head(7))
    except:  # apparently AssertionError doesn't catch all
        pass
    else:
        assert False

    fix_encode_dict = dict({"EXCLUDE": "0:2,6"})
    df_input2 = fix_encode(copy.deepcopy(df_input_original), fix_encode_dict)
    print(df_input2.head(4))
    try:
        assert_frame_equal(df_input2.head(7), df_input_original.head(7))
    except:  # apparently AssertionError doesn't catch all
        pass
    else:
        assert False

    fix_encode_dict = dict({"EXCLUDE": ":"})
    df_input3 = fix_encode(copy.deepcopy(df_input_original), fix_encode_dict)
    print(df_input3.head(4))
    assert_frame_equal(df_input3, df_input)

    pass

# if __name__ == "__main__":
#     test_fix_encode()