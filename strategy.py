import numpy as np
import warnings

class Strategy:

    def bid(self, valuation):
        return valuation

    def learn(self, single_history):
        return

class RandomStrategy(Strategy):

    def bid(self, valuation):
        return np.random.random_sample() * valuation
