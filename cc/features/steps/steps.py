from behave import *
from hamcrest import *
from covered_call import *

# Parse type table is at https://pythonhosted.org/behave/parse_builtin_types.html

@given(u'Buy {num:d} shares of {symbol:S} at ${basis:f} with a ${fee:g} fee')
def step_impl(context, num, symbol, basis, fee):
    context.cc = CoveredCall()
    context.cc.setup(num, symbol, basis, fee)

@given(u'{symbol:S} is valued at ${current_price:g}')
def step_impl(context, symbol, current_price):
    assert (context.cc.symbol == symbol)
    context.cc.current_price(current_price)

@when(u'Sell {symbol:S} {month:d}/{day:d}/{year:d} C ${strike_price:g} for ${bid_price:g} a share for commission ${c:g}')
def step_impl(context, symbol, month, day, year, strike_price, bid_price, c):
    assert (context.cc.symbol == symbol)
    context.cc.strike_price(strike_price)
    context.cc.bid_price(bid_price)
    context.cc.commission(c)

@then(u'Profit is capped at ${profit_cap:g} in return for an immediate gain of ${immediate_gain:g}')
def step_impl(context, profit_cap, immediate_gain):
    assert_that(context.cc.capped_gain(), close_to(profit_cap,0.001))
    assert_that(context.cc.immediate_gain(), close_to(immediate_gain, 0.001))


