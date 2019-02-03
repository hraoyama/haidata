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
from pandas.util.testing import assert_frame_equal

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
sys.path.insert(0, myPath + '/../../')

from haidatacfg import HaiDataCfg
from haidatautils import int_list_from_exclude_include

from test_helper_functions import helper_assert_haidatacfg
from test_helper_functions import helper_assert_frame_not_equal

from fix_encode import fix_encode
from user_functions_for_testing import set_uneven_int


test_file1 = os.path.join(HaiDataCfg.get_path(), '../../../../', 'data', 'examples', 'moma_art', 'artists.csv')
df_input = pd.read_csv(test_file1) if os.path.isfile(test_file1) else None
lin = pd.read_csv(os.path.join(HaiDataCfg.get_path(), '../../../../','data', 'examples', 'stocks', 'lin_2018.csv'))


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

    default_config_file_name = os.path.join(HaiDataCfg.get_path(), 'config', 'default_cfg.json')
    b = HaiDataCfg.from_json(default_config_file_name)
    helper_assert_haidatacfg(b, has_actions=True, has_file_name=True)
    assert 'test' not in dir(b)
    assert b.file_name == default_config_file_name
    assert not hasattr(b, 'test')
    assert not hasattr(b, 'ACTIONLIST')
    df_input2 = b(df_input)
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
    assert d.file_name == default_config_file_name
    assert not hasattr(d, 'test')
    assert not hasattr(d, 'ACTIONLIST')


def test_haidatacfg_user():
    user_config_file_name = os.path.join(HaiDataCfg.get_path(), 'config', 'cfg_for_testing.json')
    assert os.path.isfile(user_config_file_name)

    b = HaiDataCfg.from_json(user_config_file_name, {**locals(), **globals()})
    helper_assert_haidatacfg(b, has_actions=True, has_file_name=True)
    assert b.file_name == user_config_file_name
    df_input2 = b(df_input)
    assert df_input['ConstituentID'][2] == df_input2['ConstituentID'][1]
    assert df_input['ConstituentID'][2] == df_input2['ConstituentID'][2]
    assert df_input['ConstituentID'][500] == df_input2['ConstituentID'][499]
    assert df_input['ConstituentID'][500] == df_input2['ConstituentID'][500]

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
    df_input2 = d(lin)
    assert_frame_equal(df_input2.head(10), lin.head(10))

    d = HaiDataCfg.from_json(
        r'{"ACTIONS":[{"ACTION":"fix_encode","ARGS":{},"SEQUENCE":0}]}')
    helper_assert_haidatacfg(d, has_actions=True, has_file_name=False)
    lin_fe = d(lin)

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
    assert_frame_equal(lin_2.head(7), lin_3.head(7))  # should be equal (both with extra column)
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
