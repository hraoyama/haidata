# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 18:40:06 2018

@author: HansT


to test: go to anaconda prompt and type (one directory above this file):    
    py.test -v ./tests/test_haidatacfg.py 
    
"""

import sys
import os
import pandas as pd
import numpy as np
from pandas.util.testing import assert_frame_equal
import haidata

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath)
sys.path.insert(0, os.path.join(myPath, '..'))
sys.path.insert(0, os.path.join(myPath, '../config'))

from haidata.haidatacfg import HaiDataCfg
from haidata.haidatautils import int_list_from_exclude_include

from test_helper_functions import helper_assert_haidatacfg
from test_helper_functions import helper_assert_frame_not_equal

from haidata.fix_encode import fix_encode
from user_functions_for_testing import set_uneven_int

df_input = pd.DataFrame.from_dict(dict({'ArtistBio': {1: 'Spanish, born 1936',
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
lin = pd.DataFrame.from_dict(dict(
    {'Date': {1: '2018/01/02',
              2: '2018/01/02',
              3: '2018/01/02',
              4: '2018/01/02',
              5: '2018/01/02',
              6: '2018/01/02',
              7: '2018/01/02',
              8: '2018/01/02',
              9: '2018/01/02'},
     'DateTime': {1: '2018-01-02 09:02:17.290',
                  2: '2018-01-02 09:02:17.350',
                  3: '2018-01-02 09:02:28.140',
                  4: '2018-01-02 09:05:21.220',
                  5: '2018-01-02 09:05:31.730',
                  6: '2018-01-02 09:05:47.240',
                  7: '2018-01-02 09:05:47.260',
                  8: '2018-01-02 09:05:47.300',
                  9: '2018-01-02 09:12:34.010'},
     'Exchange Code': {1: np.nan,
                       2: np.nan,
                       3: np.nan,
                       4: np.nan,
                       5: np.nan,
                       6: np.nan,
                       7: np.nan,
                       8: np.nan,
                       9: np.nan},
     'Exclude Record Flag': {1: np.nan,
                             2: np.nan,
                             3: np.nan,
                             4: np.nan,
                             5: np.nan,
                             6: np.nan,
                             7: np.nan,
                             8: np.nan,
                             9: np.nan},
     'Filtered Price': {1: np.nan,
                        2: np.nan,
                        3: np.nan,
                        4: np.nan,
                        5: np.nan,
                        6: np.nan,
                        7: np.nan,
                        8: np.nan,
                        9: np.nan},
     'Market Mechanism': {1: 1.0,
                          2: 1.0,
                          3: 1.0,
                          4: 1.0,
                          5: 1.0,
                          6: 1.0,
                          7: 1.0,
                          8: 1.0,
                          9: 1.0},
     'Price': {1: 180.55,
               2: 180.55,
               3: 180.55,
               4: 180.15,
               5: 180.15,
               6: 180.1,
               7: 180.0,
               8: 180.0,
               9: 179.75},
     'Price Adjustment': {1: np.nan,
                          2: np.nan,
                          3: np.nan,
                          4: np.nan,
                          5: np.nan,
                          6: np.nan,
                          7: np.nan,
                          8: np.nan,
                          9: np.nan},
     'Sales Condition': {1: 'X',
                         2: 'X',
                         3: 'X',
                         4: 'X',
                         5: 'X',
                         6: 'X',
                         7: 'X',
                         8: 'X',
                         9: 'X'},
     'Symbol': {1: 'LIN',
                2: 'LIN',
                3: 'LIN',
                4: 'LIN',
                5: 'LIN',
                6: 'LIN',
                7: 'LIN',
                8: 'LIN',
                9: 'LIN'},
     'Time': {1: '09:02:17.290',
              2: '09:02:17.350',
              3: '09:02:28.140',
              4: '09:05:21.220',
              5: '09:05:31.730',
              6: '09:05:47.240',
              7: '09:05:47.260',
              8: '09:05:47.300',
              9: '09:12:34.010'},
     'Trade Mode': {1: '2',
                    2: '2',
                    3: '2',
                    4: '2',
                    5: '2',
                    6: '2',
                    7: '2',
                    8: '2',
                    9: '2'},
     'Transaction Category': {1: '-',
                              2: '-',
                              3: '-',
                              4: '-',
                              5: '-',
                              6: '-',
                              7: '-',
                              8: '-',
                              9: '-'},
     'VWAP': {1: 181.03466,
              2: 181.02447,
              3: 181.00797,
              4: 180.89937,
              5: 180.87906,
              6: 180.85851,
              7: 180.8287,
              8: 180.67803,
              9: 180.61879},
     'Volume': {1: 10.0,
                2: 7.0,
                3: 12.0,
                4: 50.0,
                5: 11.0,
                6: 11.0,
                7: 15.0,
                8: 96.0,
                9: 36.0}}))

def test_haidatacfg_base():

    now_str = HaiDataCfg._now_time_string()
    file_name_to_save = os.path.join(os.getcwd(), 'testlog_' + now_str + '.json')
    assert type(HaiDataCfg._create_json_string_from_dict(dict({'test': 4}), file_name_to_save)) == str
    assert os.path.isfile(file_name_to_save)

    a = HaiDataCfg.from_json(file_name_to_save)
    helper_assert_haidatacfg(a, has_actions=False, has_file_name=True)
    assert 'test' in dir(a)
    assert a.file_name == file_name_to_save
    assert hasattr(a, 'test')
    assert a.test == 4
    os.remove(file_name_to_save)

    a = HaiDataCfg.from_json(r'{"test": 5}')
    helper_assert_haidatacfg(a, has_actions=False, has_file_name=False)
    assert 'test' in dir(a)
    assert hasattr(a, 'test')
    assert a.test == 5
    assert not hasattr(a, 'ACTIONS')

    default_config_file_name = os.path.join(myPath, '../config', 'default_cfg.json')
    b = HaiDataCfg.from_json(default_config_file_name)
    helper_assert_haidatacfg(b, has_actions=True, has_file_name=True)
    assert 'test' not in dir(b)
    assert b.file_name == default_config_file_name
    assert not hasattr(b, 'test')
    assert not hasattr(b, 'ACTIONLIST')
    df_input2 = b(df_input, inplace=False)
    assert_frame_equal(df_input2.head(20), df_input.head(20))

    illegal_config_file_name = os.path.join(HaiDataCfg.get_path(),
                                            'src', 'python', 'data_cleaning', 'config',
                                            'does_not_exist_default_cfg.json')
    try:
        z = HaiDataCfg.from_json(illegal_config_file_name)
    except FileNotFoundError as error:
        pass
    else:
        raise AssertionError("Was able to process illegal file {0}".format(illegal_config_file_name))

    d = HaiDataCfg.construct_hai_data_cfg()  # same as using the default
    helper_assert_haidatacfg(b, has_actions=True, has_file_name=True)
    assert 'test' not in dir(b)
    assert not hasattr(d, 'test')
    assert not hasattr(d, 'ACTIONLIST')


def test_haidatacfg_user():
    
    user_config_file_name = os.path.join(myPath, '../config', 'cfg_for_testing.json')
    assert os.path.isfile(user_config_file_name)

    b = HaiDataCfg.from_json(user_config_file_name, {**locals(), **globals()})
    helper_assert_haidatacfg(b, has_actions=True, has_file_name=True)
    assert b.file_name == user_config_file_name
    df_input2 = b(df_input, inplace=False)
    assert df_input['ConstituentID'][2] == df_input2['ConstituentID'][1]
    assert df_input['ConstituentID'][4] == df_input2['ConstituentID'][2]
    assert df_input['ConstituentID'][4] == df_input2['ConstituentID'][3]
    assert df_input['ConstituentID'][9] == df_input2['ConstituentID'][8]
    assert df_input['ConstituentID'][9] == df_input2['ConstituentID'][7]

    helper_assert_frame_not_equal(df_input2, df_input, 7)


def test_haidatacfg_usage():

    def to_date_from_str(df, args_dict):
        column_names_to_process = [df.columns.values[x] for x in int_list_from_exclude_include(df, args_dict)]
        replace = True
        if "REPLACE" in args_dict.keys():
            replace = bool(args_dict["REPLACE"])
        if replace:
            for col_name in column_names_to_process:
                df[col_name] = pd.to_datetime(df[col_name])
        else:
            for col_name in column_names_to_process:
                df["DT_" + col_name] = pd.to_datetime(df[col_name])
        return df

    def no_op(df, args_dict):
        return df

    d = HaiDataCfg.from_json(
        r'{"ACTIONS":[{"ACTION":"no_op","ARGS":{},"SEQUENCE":0}]}',
        {**locals(), **globals()})
    helper_assert_haidatacfg(d, has_actions=True, has_file_name=False)
    df_input2 = d(lin, inplace=False)
    assert_frame_equal(df_input2.head(10), lin.head(10))

    d = HaiDataCfg.from_json(
        r'{"ACTIONS":[{"ACTION":"fix_encode","ARGS":{},"SEQUENCE":0}]}')
    helper_assert_haidatacfg(d, has_actions=True, has_file_name=False)
    lin_fe = d(lin, inplace=False)

    d = HaiDataCfg.from_json(
        r'{"ACTIONS":[{"ACTION":"to_date_from_str","ARGS":{ "INCLUDE": "Date","REPLACE":false},"SEQUENCE":0}]}',
        {**locals(), **globals()})
    helper_assert_haidatacfg(d, has_actions=True, has_file_name=False)
    lin_2 = d(lin, inplace=False)
    helper_assert_frame_not_equal(lin_2, lin, 7)

    d = HaiDataCfg.from_json(
        dict({"ACTIONS": [dict({"ACTION": "to_datetime", "ARGS": {"INCLUDE": "Date", "REPLACE": False},
                                "SEQUENCE": 0})]}),
        {**locals(), **globals()})
    helper_assert_haidatacfg(d, has_actions=True, has_file_name=False)
    lin_3 = d(lin, inplace=False)
    assert_frame_equal(lin_2.head(7), lin_3.head(7))  # should be equal (both with extra column)
    helper_assert_frame_not_equal(lin_3.head(7), lin.head(7))  # should not be equal

    d = HaiDataCfg.from_json(
        dict({"ACTIONS": [dict({"ACTION": "fix_encode", "ARGS": {}, "SEQUENCE": 0}),
                          dict({"ACTION": "to_datetime", "ARGS": {"INCLUDE": "Date", "REPLACE": False},
                                "SEQUENCE": 1}),
                          ]}),
        {**locals(), **globals()})
    helper_assert_haidatacfg(d, has_actions=True, has_file_name=False)
    lin_3 = d(lin, inplace=False)
    helper_assert_frame_not_equal(lin_2.head(7), lin_3.head(7))  # should be equal (both with extra column)
    helper_assert_frame_not_equal(lin_3.head(7), lin.head(7))  # should not be equal

    d = HaiDataCfg.construct_hai_data_cfg()
    d.add_action("no_op", _locals={**locals(), **globals()})
    helper_assert_haidatacfg(d, has_actions=True, has_file_name=True) # there is the default file name
    lin_2 = d(lin, inplace=False)
    assert_frame_equal(lin_2.head(10), lin.head(10))
    d.add_action("fix_encode")
    helper_assert_haidatacfg(d, has_actions=True, has_file_name=True)
    lin_2 = d(lin, inplace=False)
    assert_frame_equal(lin_2.head(10), lin_fe.head(10))
    d.add_action("to_datetime", dict({"INCLUDE": "Date"}))
    helper_assert_haidatacfg(d, has_actions=True, has_file_name=True)
    lin_2 = d(lin, inplace=False)
    helper_assert_frame_not_equal(lin_2, lin_fe, 10)
    helper_assert_frame_not_equal(lin_2, lin, 10)
    d.add_action("to_datetime", dict({"INCLUDE": "Date", "REPLACE": False}))
    helper_assert_haidatacfg(d, has_actions=True, has_file_name=True)
    lin_xtra_col = d(lin, inplace=False)
    helper_assert_frame_not_equal(lin_xtra_col, lin_2, 10)
    assert_frame_equal(lin_xtra_col[lin_2.columns.values].head(10), lin_2.head(10))

    now_str = HaiDataCfg._now_time_string()
    new_file_name = os.path.join(os.getcwd(), 'testcfg_' + now_str + '.json')
    d.to_json(new_file_name)

    assert os.path.isfile(new_file_name)

    e = HaiDataCfg.from_json(new_file_name, {**locals(), **globals()})
    lin_from_json = e(lin, inplace=False)
    assert_frame_equal(lin_xtra_col.head(20), lin_from_json.head(20))

    d = HaiDataCfg.construct_hai_data_cfg()
    d.add_action("no_op", seq_count= 0, _locals={**locals(), **globals()})
    lin_2 = d(lin, inplace=False)
    assert_frame_equal(lin_2.head(10), lin.head(10))
    d.add_action("fix_encode", seq_count=1)
    lin_2 = d(lin, inplace=False)
    assert_frame_equal(lin_2.head(10), lin_fe.head(10))
    d.add_action("to_datetime", dict({"INCLUDE": "Date"}), seq_count=2)
    lin_2 = d(lin, inplace=False)
    helper_assert_frame_not_equal(lin_2, lin_fe, 10)
    helper_assert_frame_not_equal(lin_2, lin, 10)
    d.add_action("to_datetime", dict({"INCLUDE": "Date", "REPLACE": False}), seq_count=3)
    lin_xtra_col = d(lin, inplace=False)
    helper_assert_frame_not_equal(lin_xtra_col, lin_2, 10)
    assert_frame_equal(lin_xtra_col[lin_2.columns.values].head(10), lin_2.head(10))

# def test_haidatacfg_interface():
#     d = HaiDataCfg.construct_hai_data_cfg()
#     pass

# if __name__ == "__main__":
#     test_haidatacfg_usage()
