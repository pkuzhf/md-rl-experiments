import numpy as np
import warnings
import bidder

class Auction:

    def __init__(self, bidders, mechanism):
        self.bidders = bidders
        self.mechanism = mechanism
        self.revenue = 0

    def takeAuction(self):
        bids = []
        for bidder in bidders:
            bids.append(bidder.bid())
        [allocation, payments] = self.mechanism.calcAllocationAndPayments(bids)
        single_history = [[bids[i], None, None] for i in range(len(bidders))]
        for i in range(len(self.mechanism.ctrs)):
            ctr = self.mechanism.ctrs[i]
            click = np.random.random_sample() < ctr
            if click:
                price = payments[i]
                self.revenue += price
            else:
                price = None
            self.bidders[allocation[i]].feedback(click, price)
            single_history[allocation[i]][1:] = [click, payments[i]]
        self.mechanism.learn(single_history)