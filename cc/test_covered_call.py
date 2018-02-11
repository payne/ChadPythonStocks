import pytest
from covered_call import CoveredCall

@pytest.fixture
def covered_call():
    parameters = {'symbol':'LVS', 'basis':73.82, 'current_price':77.44, 'bid_price':0.41, 
        'expiration_date':'2/23/2018', 'strike_price':85.00, 
        'contracts':2}
    cc = CoveredCall()
    cc.oldSetup(**parameters)
    return cc

def test_immediate_gain(covered_call):
    assert covered_call.immediate_gain() == 73.00

def test_lower_fee_more_gain(covered_call):
    covered_call.fee = covered_call.fee - 1
    assert covered_call.immediate_gain() == 74.00

def test_capped_gain(covered_call):
    assert covered_call.capped_gain() == pytest.approx(2229.00,0.001)


