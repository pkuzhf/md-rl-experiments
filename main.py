import numpy as np
import warnings
from auction import Auction
from bidder import Bidder
from strategy import Strategy
from mechanism import * 
from valuation_generator import uniformValuationGenerator
from draw import Draw
def main():

    n = 10
    l=0 
    r=10
    bidders = [Bidder(uniformValuationGenerator(l,r), Strategy()) for i in range(n)]
    ctrs = [0.1 for i in range(10)]
    auction = Auction(bidders, GSP(ctrs))
    n_auction = 10000
    x_axis,bidders_revenue,auction_revenue = [],[],[]
    for i in range(n_auction):
        auction.takeAuction()
        x_axis.append(i+1)
        sum = np.sum(np.array([bidders[i].revenue for i in range(n)]))/n
        bidders_revenue.append(sum)            #  目前取平均值
        auction_revenue.append(auction.revenue)
        
    Draw(x_axis,bidders_revenue,'times','revenue',"bidders_revenue")
    Draw(x_axis,auction_revenue,'times','revenue',"auction_revenue")

    print([bidders[i].revenue for i in range(n)])
    print(auction.revenue)

main()