import sys
import os
import pandas as pd
import numpy as np

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath)
sys.path.insert(0, myPath + '/../')

from haidatacfg import HaiDataCfg
from return_type import ReturnType
from extract_returns import extract_returns


def test_extract_returns():
    np.random.seed(10)
    a = pd.DataFrame({'A': np.fabs(np.random.randn(200)), 'B': np.random.uniform(200, 300, 200)})
    b = a.copy()
    ReturnType.LOG_RETURN(b, 'A')
    
    assert np.isnan(b.A[0])
    assert not np.isnan(a.A[0])
    
    assert b.A[199] < -0.71
    assert b.A[199] > -0.72
    
    assert (a.A[199] - a.A[198]) < -0.595
    assert a.A[199] > 0.57
    
    b = a.copy()
    ReturnType.LOG_RETURN(b, ['A', 'B'])
    
    assert np.isnan(b.A[0])
    assert not np.isnan(a.A[0])
    
    assert np.isnan(b.B[0])
    assert not np.isnan(a.B[0])
    
    assert b.A[199] < -0.71
    assert b.A[199] > -0.72
    
    assert (a.A[199] - a.A[198]) < -0.595
    assert a.A[199] > 0.57
    
    b = a.copy()
    
    extract_returns(b, {"COLS": "A,B", "RETURN_TYPE": "LOG_RETURN"})
    
    assert np.isnan(b.A[0])
    assert not np.isnan(a.A[0])
    
    assert np.isnan(b.B[0])
    assert not np.isnan(a.B[0])
    
    assert b.A[199] < -0.71
    assert b.A[199] > -0.72
    
    assert (a.A[199] - a.A[198]) < -0.595
    assert a.A[199] > 0.57
