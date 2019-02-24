import sys
import os
import pandas as pd
import numpy as np

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from haidatacfg import HaiDataCfg


def test_fix_empty_rows():
    df = pd.DataFrame(
        data={'col1': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
              'col2': [np.nan] * 10,
              'col3': [0, 1, 2, 3, 4, 5, 6, 7, np.nan, np.nan],
              'col4': [0, 1, 2, 3, 4, 5, 6, 7, 8, np.nan],
              'col5': [0, 0, 2, 3, 0, np.nan, 6, 7, 8, np.nan]})

    d = HaiDataCfg.construct_hai_data_cfg()
    d.add_action("fix_empty_rows")
    df2 = d(df, inplace=False)

    assert (df.iloc[0, 0] == 0)
    assert (df2.iloc[0, 0] == 0)
    assert (df.iloc[9, 0] == 9)
    assert (df2.iloc[9, 0] == 9)

    d = HaiDataCfg.construct_hai_data_cfg()
    d.add_action("fix_empty_rows", dict({'ZERO': "True"}))
    df2 = d(df, inplace=False)

    assert (df.iloc[0, 0] == 0)
    assert (df2.iloc[0, 0] == 1)
    assert (df.iloc[9, 0] == 9)
    assert (df2.iloc[8, 0] == 9)

    d = HaiDataCfg.construct_hai_data_cfg()
    d.add_action("fix_empty_rows", dict({'MINIMUM': 0.5}))
    df2 = d(df, inplace=False)

    assert (df.iloc[0, 0] == 0)
    assert (df2.iloc[0, 0] == 0)
    assert (df.iloc[9, 0] == 9)
    assert (df2.iloc[8, 0] == 8)
    assert (df2.shape[0] < df.shape[0])

    d = HaiDataCfg.construct_hai_data_cfg()
    d.add_action("fix_empty_rows", dict({'MINIMUM': 0.5, 'ZERO': "True"}))
    df2 = d(df, inplace=False)

    assert (df.iloc[0, 0] == 0)
    assert (df2.iloc[0, 0] == 1)
    assert (df.iloc[9, 0] == 9)
    assert (df2.iloc[7, 0] == 8)
    assert (df2.shape[0] < df.shape[0])

    d = HaiDataCfg.construct_hai_data_cfg()
    d.add_action("fix_empty_rows", dict({'MINIMUM': 0.5, 'ZERO': True}))
    df2 = d(df, inplace=False)

    assert (df.iloc[0, 0] == 0)
    assert (df2.iloc[0, 0] == 1)
    assert (df.iloc[9, 0] == 9)
    assert (df2.iloc[7, 0] == 8)
    assert (df2.shape[0] < df.shape[0])
