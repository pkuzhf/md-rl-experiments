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
    
    bidders = []
    l,r = 0,1
    n_kind = 2

    '''
    n = [1,1,1,1,1,1,1,1,1,1,90]
    List_Of_Strategy = [CoefficientStrategy(i/10.0) for i in range(1,11)]
    List_Of_Strategy.append(RandomStrategy())
    bidders_name = ['C = '+str(i/10.0) for i in range(1,11)]
    bidders_name.append('random')
    '''

    
    #n = [10 for i in range(n_kind)]
    #List_Of_Strategy = [CoefficientStrategy(i/10.0) for i in range(1,11)]
    #bidders_name = ['C = '+str(i/10.0) for i in range(1,11)]
    
    #n = [100]
    #List_Of_Strategy = [CoefficientStrategy(1)]
    #bidders_name = ['truth']
    n = [25,25]
    List_Of_Strategy = [CoefficientStrategy(1),BarStrategy()]
    #bidders_name = ['C = 0.4','C = 0.5']
    #n = [10 for i in range(n_kind)]
    #List_Of_Strategy = [CoefficientStrategy(0.5),RandomStrategy()]
    #bidders_name = ['C = 0.5','Random']
    bidders_name = ['truth','Bar']
    #bidders_name.append('C = 0.7 *')
    
    
    #List_Of_Strategy = [CoefficientStrategy(i/100+0.3) for i in range(1,11)]
    #List_Of_Strategy.append(RandomStrategy())
    #bidders_name = ['X = '+str(i) for i in range(1,11)]


    #List_Of_Strategy = [Strategy(),RandomStrategy(),CoefficientStrategy(0.4),CoefficientStrategy(0.5),CoefficientStrategy(0.6),CoefficientStrategy(0.7),PolyStrategy(50,1)]
    #bidders_name = ['truth','random','C = 0.4','C = 0.5','C = 0.6','C = 0.7','Poly']

    for i in range(n_kind):
        for j in range(n[i]):
            bidders.append(Bidder(uniformValuationGenerator(l,r), List_Of_Strategy[i] ))

    sum_n = get_sum_int(n)
    ctrs = [(sum_n-i+0.0)/sum_n for i in range(sum_n)]

    auction = Auction(bidders, VCG(ctrs))
    n_auction = 10000
    x_axis,bidders_revenue,auction_revenue,social_welfare_revenue = [],[[] for i in range(n_kind)],[],[]

    for k in range(n_auction):
        auction.takeAuction()
        x_axis.append(k+1)
        now = 0
        print(k)
        for j in range(n_kind):    
            sum = np.sum(np.array([bidders[i].revenue for i in range(now,now+n[j])]))
            bidders_revenue[j].append(sum/n[j])            #  目前取总和 * n_kind
            now += n[j]
        auction_revenue.append(auction.revenue)
        social_welfare_revenue.append(auction.social_welfare)
    for j in range(n_kind):
        for i in range(len(bidders_revenue[j])-1,-1,-1):
            if i >= 300:
                bidders_revenue[j][i] -= bidders_revenue[j][i-300]
            bidders_revenue[j][i] /= min(i+1,300)

    print(auction_revenue[n_auction-1],social_welfare_revenue[n_auction-1]*10)
    for i in range(n_kind):
        print(bidders_revenue[i][n_auction-1])
    # details of DRAW

    #a = [auction_revenue]
    a = []
    a.extend([bidders_revenue[i] for i in range(n_kind)])
    #b = ['mechanism revenue']
    b = []
    b.extend([bidders_name[j]+' bidders'+' revenue' for j in range(n_kind)])
    
    Draw(x_axis,a,'times','revenue',b,"GSP vs diverse bidders 10")

    #print([bidders[i].revenue for i in range(n)])
    #print(auction.revenue)

main()