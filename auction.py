import numpy as np
import warnings
import bidder

class Auction:

    def __init__(self, bidders, mechanism):
        self.bidders = bidders
        self.mechanism = mechanism
        self.revenue = 0
        self.social_welfare = 0

    def takeAuction(self):
        bids = []
        for bidder in self.bidders:
            bids.append(bidder.bid())
        [allocation, payments] = self.mechanism.calcAllocationAndPayments(bids)
        single_history = [[bids[i], None, None] for i in range(len(self.bidders))]
        for i in range(len(self.mechanism.ctrs)):
            ctr = self.mechanism.ctrs[i]
            click = int(np.random.random_sample() < ctr)
            if click:
                price = payments[i]
                self.revenue += price
                self.social_welfare += self.bidders[allocation[i]].valuation
            else:
                price = 0 #之前写的是None，改掉了
            self.bidders[allocation[i]].feedback(click, price, bids)
            single_history[allocation[i]][1:] = [click, payments[i]]
        self.mechanism.learn(single_history)