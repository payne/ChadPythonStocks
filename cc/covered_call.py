class CoveredCall(object):

    def __init__(self):
       pass

    def setup(self, num, symbol, basis, fee):
        self.num = num
        self.contracts = num / 100
        self.symbol = symbol
        self.basis = basis
        self.fee = fee

    def oldSetup(self, symbol, basis, current_price, bid_price, expiration_date, strike_price, contracts):
        self.symbol = symbol
        self.basis = basis
        self.current_price = current_price
        self.bid_price = bid_price
        self.expiration_date = expiration_date
        self.strike_price = strike_price
        self.contracts = contracts
        self.fee = 7.0
        self.commission = 1.0 * self.contracts;

    def current_price(self, current_price):
        self.current_price = current_price

    def strike_price(self, strike_price):
        self.strike_price = strike_price

    def bid_price(self, bid_price):
        self.bid_price = bid_price

    def commission(self, c):
        self.commission = c

    def immediate_gain(self):
        return (self.bid_price) * 100 * self.contracts - self.fee - self.commission

    def capped_gain(self):
        return (self.strike_price - self.basis) * 100 * self.contracts - self.fee

