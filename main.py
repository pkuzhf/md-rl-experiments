import numpy as np
import warnings

def main():
    n = 10
    bidders = [Bidder(uniformValuationGenerator(), Strategy()) for i in range(n)]
    ctrs = [0.1 for i in range(10)]
    auction = Auction(bidders, GSP(ctrs))
    n_auction = 10000
    for i in range(n_auction):
        auction.takeAuction()
    print([bidders[i].revenue for i in range(n)])
    print(auction.revenue)