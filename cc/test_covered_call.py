import pytest
from covered_call import CoveredCall

@pytest.fixture
def covered_call():
    cc = CoveredCall("LVS", 73.82, 77.44, 0.41, '2/23/2018', 85.00, 2)
    return cc

def test_immediate_gain(covered_call):
    assert covered_call.immediate_gain() == 73.00

def test_lower_fee_more_gain(covered_call):
    covered_call.fee = covered_call.fee - 1
    assert covered_call.immediate_gain() == 74.00

def test_capped_gain(covered_call):
    assert covered_call.capped_gain() == pytest.approx(2229.00,0.001)


