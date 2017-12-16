import numpy as np
import warnings
import random
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
def out(bidders):
    cnt = {}
    for i in range(len(bidders)):
        cnt[bidders[i].strategy.name] = 0
    for i in range(len(bidders)):
        cnt[bidders[i].strategy.name] += 1
    for x in cnt.keys():
        print(x,cnt[x])

stra = {}
l,r = 47,53

def deal(bidders):
    ma,mi = -1e99,1e99
    jma,jmi = '',''
    cnt = {}
    revenue = {}
    bid = {}
    for i in range(len(bidders)):
        cnt[bidders[i].strategy.name],revenue[bidders[i].strategy.name] = 0,0
    for i in range(len(bidders)):
        #print(bidders[i].cnt,'BBBBBBB')
        cnt [bidders[i].strategy.name] += bidders[i].cnt
        bid [bidders[i].strategy.name] = bidders[i]
        revenue[bidders[i].strategy.name] += bidders[i].revenue
    for x in cnt.keys():
        #print(revenue[x],cnt[x],'AAAAAAAAAAAAAAAAAA')
        revenue[x] /= cnt[x]
        if(revenue[x] > ma):
            ma = revenue[x]
            jma = x
        if(revenue[x] < mi):
            mi = revenue[x]
            jmi = x
    for i in range(len(bidders)):
        if bidders[i].strategy.name == jmi:
            bidders[i] = Bidder(uniformValuationGenerator(l,r), stra[jma] )
            break
    return bidders
    
def main():
    
    bidders = []
    n_kind = 3
    n = [30,30,30]
    List_Of_Strategy = [CoefficientStrategy(0.95), CRecorderStrategy(0.95, 4), CoefficientStrategy(1.0)]
    for i in range(n_kind):
        stra[List_Of_Strategy[i].name] = List_Of_Strategy[i]

    for i in range(n_kind):
        for j in range(n[i]):
            bidders.append(Bidder(uniformValuationGenerator(l,r), List_Of_Strategy[i] ))

    sum_n = get_sum_int(n)
    n_auction, n_circle, n_once, m, n_lost= 10000, 100, 10, 10, 10
    ctrs = [(m-i+0.0)/m for i in range(m)]

    #x_axis,bidders_revenue,auction_revenue,social_welfare_revenue = [],[[] for i in range(n_kind)],[],[]
    print(0)
    out(bidders)

    for k in range(n_auction):
        
        for i in range(sum_n):
            bidders[i].revenue = 0
            bidders[i].cnt = 0
        
        #print([bidders[i].cnt for i in range(len(bidders))])

        for k2 in range(n_circle):
           temp_bidders_i = random.sample(range(sum_n), m)
           #print(temp_bidders_i)
           temp_bidders = []
           for x in temp_bidders_i:
               #print('AAA',bidders[x].cnt)
               bidders[x].cnt += 1
               temp_bidders.append(bidders[x])

           auction = Auction(temp_bidders, VCG(ctrs))
           for k3 in range(n_once):
              auction.takeAuction()
           for i in range(len(temp_bidders_i)):
               bidders[temp_bidders_i[i]].revenue += temp_bidders[i].revenue
        
        
        bidders = deal(bidders)
        print('case\n',k,'\n')
        out(bidders)

    '''
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
    '''

main()