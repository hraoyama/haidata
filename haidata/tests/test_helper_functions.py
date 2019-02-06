

import sys, os
import pandas as pd
from pandas.util.testing import assert_frame_equal

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath)
sys.path.insert(0, myPath + '/../')
sys.path.insert(0, myPath + '/../config')

from haidatacfg import HaiDataCfg


def helper_assert_haidatacfg(d, has_actions=True, has_file_name=False):
    assert type(d) == HaiDataCfg
    if has_file_name:
        assert d.file_name is not None
    else:
        assert d.file_name is None
    assert d(20) is None
    if has_actions:
        assert hasattr(d, 'ACTIONS')
    else:
        assert not hasattr(d, 'ACTIONS')
    z = pd.DataFrame()
    assert_frame_equal(z, d(z))


def helper_assert_frame_not_equal(df_1, df_2, headCount = None):
    # should be different
    try:
        if headCount is not None:
            assert_frame_equal(df_1.head(headCount), df_2.head(headCount))
        else:
            assert_frame_equal(df_1, df_2)
    except:  # apparently AssertionError doesn't catch all
        pass
    else:
        assert False