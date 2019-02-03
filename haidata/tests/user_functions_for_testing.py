# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 19:39:40 2018

@author: hraoy
"""

import pandas as pd
import copy

from operator import itemgetter
from haidatautils import to_int_list


def set_uneven_int(df_input, arg_dict):
    df = copy.deepcopy(df_input)
    col_names_to_check = list(df.columns.values)
    if 'EXCLUDE' in arg_dict.keys():
        if arg_dict['EXCLUDE'].strip() != ':':
            try:
                colnames_idxs = to_int_list(arg_dict['EXCLUDE'])
                excluded_names = list(itemgetter(*colnames_idxs)(col_names_to_check))
                col_names_to_check = list(set(col_names_to_check) - set(excluded_names))
            except IndexError as e:
                raise e
        else:
            return df

    try:
        include_types = ['int16', 'int32', 'int64']
        used_column_names = df.loc[:, col_names_to_check].select_dtypes(include=include_types).columns.values
        if len(used_column_names) == 0:
            return df
        to_replace_df = df.loc[:, used_column_names].apply(
            lambda x: pd.Series(map(lambda y: y + 1 if y % 2 == 0 else y, x)))
        df.loc[:, used_column_names] = to_replace_df
    except TypeError as te:
        raise te
    return df
