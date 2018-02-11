Feature: Covered calls
Scenario: LVS Example
  Given Buy 200 shares of LVS at $73.82 with a $7 fee
  And LVS is valued at $77.44
  When Sell LVS 2/23/2018 C $85.00 for $0.41 a share for commission $2
  Then Profit is capped at $2229.00 in return for an immediate gain of $73

