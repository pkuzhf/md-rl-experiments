import numpy as np
import warnings

class Bidder:
  
    def __init__(self, valuation_generator, strategy):
        self.valuation_generator = valuation_generator
        self.strategy = strategy
        self.history = [] # [valuation, bid, click, price]
        self.revenue = 0
        self.valuation = self.valuation_generator.generate()
        self.cnt = 0

    def bid(self):
        #self.valuation = self.valuation_generator.generate()
        bid = self.strategy.bid(self.valuation)
        self.history.append([self.valuation, bid, None, None])
        return bid


    def feedback(self, click, payment, other_bids):
        self.history[-1][2] = click
        self.history[-1][3] = payment
        self.strategy.learn(self.history[-1], other_bids)
        if click:
            self.revenue += self.history[-1][0] - payment