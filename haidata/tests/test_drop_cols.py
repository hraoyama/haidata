import sys
import os
import pandas as pd
import numpy as np
import haidata

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from haidata.haidatacfg import HaiDataCfg


def test_drop_cols():
    df = pd.DataFrame(
        data={'col1': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
              'col2': [np.nan] * 10,
              'col3': [0, 1, 2, 3, 4, 5, 6, 7, np.nan, np.nan],
              'col4': [0, 1, 2, 3, 4, 5, 6, 7, 8, np.nan],
              'col5': [100, 1, 2, 3, 4, 5, 6, 7, 8, np.nan]})
    
    d = HaiDataCfg.construct_hai_data_cfg()
    d.add_action("drop_cols", {'COLS': "0,col4,col5"})
    df2 = d(df)
    
    assert ('col2' in df.columns.values)
    assert ('col2' in df2.columns.values)
    
    assert ('col1' in df.columns.values)
    assert ('col1' not in df2.columns.values)
    
    assert ('col4' in df.columns.values)
    assert ('col4' not in df2.columns.values)
    
    assert ('col5' in df.columns.values)
    assert ('col5' not in df2.columns.values)
