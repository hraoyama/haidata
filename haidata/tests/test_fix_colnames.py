import sys
import os
import pandas as pd

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from haidatacfg import HaiDataCfg


def test_fix_colnames():
    test_file1 = os.path.join(HaiDataCfg.get_path(), '../../../../', 'data', 'examples', 'moma_art', 'artists.csv')
    df_input_original = pd.read_csv(test_file1) if os.path.isfile(test_file1) else None

    d = HaiDataCfg.construct_hai_data_cfg()
    d.add_action("fix_colnames", {"CASE": "upper"})

    for x1, x2 in zip(df_input_original.columns.values, d(df_input_original).columns.values):
        test = x1 != x2 if ' ' not in x1 and x1.lower() != x2.lower() else x1.upper() == x2.upper()
        if not test:
            test = ' ' in x1 and x1.upper() != x1 and x1.lower() != x1  # mixed case with a space...
        assert (test)

