import sys
import os
import pandas as pd
import numpy as np
import haidata

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from haidata.haidatacfg import HaiDataCfg


def test_fix_empty_cols():
    df = pd.DataFrame(
        data={'col1': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 'col2': [np.nan] * 10,
              'col3': [0, 1, 2, 3, 4, 5, 6, 7, np.nan, np.nan],
              'col4': [0, 1, 2, 3, 4, 5, 6, 7, 8, np.nan]})

    d = HaiDataCfg.construct_hai_data_cfg()
    d.add_action("fix_empty_cols")

    df2 = d(df, inplace=False)

    assert ('col2' in df.columns.values)
    assert ('col2' not in df2.columns.values)

    d.add_action("fix_empty_cols", dict({"MINIMUM": 0.5}))
    df3 = d(df, inplace=False)
    assert ('col2' in df.columns.values)
    assert ('col2' not in df3.columns.values)

    d.add_action("fix_empty_cols", dict({"MINIMUM": 0.9}))
    df4 = d(df, inplace=False)
    assert ('col2' in df.columns.values)
    assert ('col2' not in df4.columns.values)
    assert ('col3' not in df4.columns.values)
    assert ('col4' in df4.columns.values)

    d.add_action("fix_empty_cols", dict({"MINIMUM": 0.95}))
    df5 = d(df, inplace=False)
    assert ('col2' in df.columns.values)
    assert ('col2' not in df5.columns.values)
    assert ('col3' not in df5.columns.values)
    assert ('col4' not in df5.columns.values)
