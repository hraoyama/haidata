import sys
import os
import pandas as pd
import numpy as np

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath)
sys.path.insert(0, myPath + '/../')

from haidata.haidatacfg import HaiDataCfg

df_input_original = pd.DataFrame.from_dict(dict({'ArtistBio': {1: 'Spanish, born 1936',
                               2: 'American, born 1941',
                               3: 'American, born 1946',
                               4: 'Danish, born 1941',
                               5: 'Italian, born 1925',
                               6: 'American, born 1941',
                               7: 'American, born Lithuania 1923',
                               8: 'American, born Germany 1918',
                               9: 'French, born Germany (Alsace). 1886–1966',
                               10: 'Estonian, born 1936'},
                 'BeginDate': {1: 1936,
                               2: 1941,
                               3: 1946,
                               4: 1941,
                               5: 1925,
                               6: 1941,
                               7: 1923,
                               8: 1918,
                               9: 1886,
                               10: 1936},
                 'ConstituentID': {1: 2,
                                   2: 3,
                                   3: 4,
                                   4: 5,
                                   5: 6,
                                   6: 7,
                                   7: 9,
                                   8: 10,
                                   9: 11,
                                   10: 12},
                 'DisplayName': {1: 'Doroteo Arnaiz',
                                 2: 'Bill Arnold',
                                 3: 'Charles Arnoldi',
                                 4: 'Per Arnoldi',
                                 5: 'Danilo Aroldi',
                                 6: 'Bill Aron',
                                 7: 'David Aronson',
                                 8: 'Irene Aronson',
                                 9: 'Jean (Hans) Arp',
                                 10: 'Jüri Arrak'},
                 'EndDate': {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 1966, 10: 0},
                 'Gender': {1: 'Male',
                            2: 'Male',
                            3: 'Male',
                            4: 'Male',
                            5: 'Male',
                            6: 'Male',
                            7: 'Male',
                            8: 'Female',
                            9: 'Male',
                            10: 'Male'},
                 'Nationality': {1: 'Spanish',
                                 2: 'American',
                                 3: 'American',
                                 4: 'Danish',
                                 5: 'Italian',
                                 6: 'American',
                                 7: 'American',
                                 8: 'American',
                                 9: 'French',
                                 10: 'Estonian'},
                 'ULAN': {1: np.nan,
                          2: np.nan,
                          3: 500027998.0,
                          4: np.nan,
                          5: np.nan,
                          6: np.nan,
                          7: 500003363.0,
                          8: 500042413.0,
                          9: 500031000.0,
                          10: np.nan},
                 'Wiki QID': {1: np.nan,
                              2: np.nan,
                              3: 'Q1063584',
                              4: np.nan,
                              5: np.nan,
                              6: np.nan,
                              7: 'Q5230870',
                              8: 'Q19748568',
                              9: 'Q153739',
                              10: np.nan}}))


def test_fix_colnames():

    d = HaiDataCfg.construct_hai_data_cfg()
    d.add_action("fix_colnames", {"CASE": "upper"})

    for x1, x2 in zip(df_input_original.columns.values, d(df_input_original).columns.values):
        test = x1 != x2 if ' ' not in x1 and x1.lower() != x2.lower() else x1.upper() == x2.upper()
        if not test:
            test = ' ' in x1 and x1.upper() != x1 and x1.lower() != x1  # mixed case with a space...
        assert (test)

