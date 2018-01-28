class CoveredCall(object):

    def __init__(self, symbol, basis, current_price, bid_price, expiration_date, contracts):
        self.symbol = symbol
        self.basis = basis
        self.current_price = current_price
        self.bid_price = bid_price
        self.expiration_date = expiration_date
        self.contracts = contracts
        self.fee = 7.0
        self.commission = 2.0;

    def immediate_gain(self):
        return (self.bid_price) * 100 * self.contracts - self.fee - self.commission

