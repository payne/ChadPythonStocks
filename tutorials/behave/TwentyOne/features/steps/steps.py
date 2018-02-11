from behave import *
from twentyone import *

@given(u'a dealer')
def step_impl(context):
    context.dealer = Dealer()

@when(u'the round starts')
def step_impl(context):
    context.dealer.new_round()

@then(u'the dealer gives itself two cards')
def step_impl(context):
    assert(len(context.dealer.hand) == 2)

