#!/usr/bin/env python
# -*- coding=utf-8 -*-

"""
 @author 
 @create 2017-03-15 下午1:56
"""

import numpy as np
import pandas as pd


def pandas_series():
    s = pd.Series([1, 3, 5, np.nan, 6, 8])
    print s

    l = [(1, 2, 3, 4, 5, 4, 5), (1, 2, 3, 4, 5, 4, 5)]
    s = pd.Series(l)

    print type(l)

    print s


def pandas_date_series():
    dates = pd.date_range('20170301', periods=6)
    print dates
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
    print df

    df2 = pd.DataFrame({'A': 1.,
                        'B': pd.Timestamp('20130102'),
                        'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                        'D': np.array([3] * 4, dtype='int32'),
                        'E': pd.Categorical(["test", "train", "test", "train"]),
                        'F': 'foo'})
    print df2


pandas_date_series()
