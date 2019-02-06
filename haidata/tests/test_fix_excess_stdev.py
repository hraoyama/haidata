import sys
import os
import pandas as pd
import numpy as np
from pandas.util.testing import assert_frame_equal

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from haidatacfg import HaiDataCfg


def test_fix_excess_stdev():
    df = pd.DataFrame(
        data={'col1': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
              'col2': [np.nan] * 10,
              'col3': [0, 1, 2, 3, 4, 5, 6, 7, np.nan, np.nan],
              'col4': [0, 1, 2, 3, 4, 5, 6, 7, 8, np.nan],
              'col5': [10.5, 40.3, 20.3, 20.9, 34.21, 12.34, 78.34, 100.10, 103.43, 110.98],
              'col6': [11.5, 42.3, 29.3, 28.9, 54.21, 62.34, 78.34, 150.10, 153.43, 190.98],
              'col7': [4.5, 14.3, 20.3, 2.9, 3.21, 1.34, 178.34, 200.10, 223.43, 210.98],
              'TAG': [0, 0, 0, 0, 1, 1, 1, 2, 2, 2],
              })
    
    d = HaiDataCfg.construct_hai_data_cfg()
    d.add_action("fix_excess_stdev", {'COLS': "col1", 'NUM_STD': 1.25})
    df2 = d(df, inplace=False)
    
    assert (9 in df['col1'].values)
    assert (9 not in df2['col1'].values)
    
    assert (8 in df['col1'].values)
    assert (8 in df2['col1'].values)
    
    assert (2 in df['col1'].values)
    assert (2 in df2['col1'].values)
    
    assert (1 in df['col1'].values)
    assert (1 in df2['col1'].values)
    
    d = HaiDataCfg.construct_hai_data_cfg()
    d.add_action("fix_excess_stdev", {'COLS': "col1", 'NUM_STD': 0.75})
    df3 = d(df, inplace=False)
    
    assert (9 in df['col1'].values)
    assert (9 not in df3['col1'].values)
    
    assert (8 in df['col1'].values)
    assert (8 not in df3['col1'].values)
    
    assert (3 in df['col1'].values)
    assert (3 in df3['col1'].values)
    
    assert (2 in df['col1'].values)
    assert (2 not in df3['col1'].values)
    
    assert (1 in df['col1'].values)
    assert (1 not in df3['col1'].values)
    
    d = HaiDataCfg.construct_hai_data_cfg()
    d.add_action("fix_excess_stdev", {'COLS': "col1", 'NUM_STD': 1.25, 'ITER': "true"})
    df4 = d(df, inplace=False)
    assert_frame_equal(df3, df4)
    
    d = HaiDataCfg.construct_hai_data_cfg()
    d.add_action("fix_excess_stdev", {'COLS': "col7", 'NUM_STD': 1.0, 'BY': "TAG"})
    df5 = d(df, inplace=False)
    
    assert (4.50 in df['col7'].values)
    assert (4.50 in df5['col7'].values)
    
    assert (20.3 in df['col7'].values)
    assert (20.3 not in df5['col7'].values)
    
    assert (3.21 in df['col7'].values)
    assert (3.21 in df5['col7'].values)
    
    assert (178.34 in df['col7'].values)
    assert (178.34 not in df5['col7'].values)
    
    assert (200.10 in df['col7'].values)
    assert (200.10 in df5['col7'].values)
    
    assert (223.43 in df['col7'].values)
    assert (223.43 not in df5['col7'].values)

# if __name__ == '__main__':
#     test_fix_excess_stdev()
