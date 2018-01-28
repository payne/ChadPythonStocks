import pytest
from covered_call import CoveredCall

def test_example_two():
    cc = CoveredCall("LVS", 73.82, 77.44, 0.41, '2/23/2018', 2)
    assert cc.immediate_gain() == 73.00
