from behave import *
from covered_call import *

@given(u'Buy {num:d} shares of {symbol:s} at ${basis:f} with a ${fee:g} fee')
def step_impl(context, num, symbol, basis, fee):
    context.cc = CoveredCall(num, symbol, basis, fee)

@given(u'{symbol:s} is valued at ${current_price:g}')
def step_impl(context, symbol, current_price):
    assert (context.cc.symbol == symbol)
    context.cc.current_price(current_price)

@when(u'Sell LVS 2/23/2018 C $85.00 for $0.41 a share')
def step_impl(context):
    #raise NotImplementedError(u'STEP: When Sell LVS 2/23/2018 C $85.00 for $0.41 a share')
    print("skip")



@then(u'Profit is capped at $2227.00 in return for an immediate gain of $73')
def step_impl(context):
    #raise NotImplementedError(u'STEP: Then Profit is capped at $2227.00 in return for an immediate gain of $73')
    print("skip")

