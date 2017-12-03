import numpy as np
import warnings
from auction import Auction
from bidder import Bidder
from strategy import *
from mechanism import * 
from valuation_generator import uniformValuationGenerator
from draw import Draw
def get_sum_int(a):
    sum = 0
    for x in a:
        sum += x
    return sum
def main():
    
    l,r = 0,10
    n_kind = 2
    n = [10,10]
    List_Of_Strategy = [Strategy(),RandomStrategy()]
    bidders = []
    bidders_name = ['truth bidders','random bidders']
    for i in range(n_kind):
        for j in range(n[i]):
            bidders.append(Bidder(uniformValuationGenerator(l,r), List_Of_Strategy[i] ))

    sum_n = get_sum_int(n)
    ctrs = [(sum_n-i+0.0)/sum_n for i in range(sum_n)]

    auction = Auction(bidders, GFP(ctrs))
    n_auction = 1000
    x_axis,bidders_revenue,auction_revenue = [],[[] for i in range(n_kind)],[]

    for k in range(n_auction):
        auction.takeAuction()
        x_axis.append(k+1)
        now = 0
        print(k)
        for j in range(n_kind):    
            sum = np.sum(np.array([bidders[i].revenue for i in range(now,now+n[j])]))
            bidders_revenue[j].append(sum)            #  目前取总和
            now += n[j]
        auction_revenue.append(auction.revenue)

    a = [auction_revenue]
    a.extend([bidders_revenue[i] for i in range(n_kind)])
    b = ['mechanism revenue']
    b.extend([bidders_name[j]+' revenue' for j in range(n_kind)])
    
    Draw(x_axis,a,'times','revenue',b,"GFP vs diverse bidders")
    #Draw(x_axis,auction_revenue,'times','revenue',"auction_revenue")

    #print([bidders[i].revenue for i in range(n)])
    #print(auction.revenue)

main()