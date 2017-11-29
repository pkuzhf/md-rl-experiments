import numpy as np
import warnings

class Mechanism:
    def __init__(self, ctrs):
        self.ctrs = ctrs

    def calcAllocationAndPayments(self, bids):
        return [allocation, payments]
    def learn(self, single_history):
        return

class GFP(Mechanism):

    def calcAllocationAndPayments(self, bids):
        print(bids)
        bidder = []
        for i in range(len(bids)):
            bidder.append([bids[i], i])
        bidder = sorted(bidder)
        bidder.reverse()
        allocation = [bidder[i][1] for i in range(len(bidder))]
        payments = [bidder[i][0] for i in range(len(bidder))]
        return [allocation,payments]
    
class VCG(Mechanism):

    def calcAllocationAndPayments(self, bids):
        bidder = []
        for i in range(len(bids)):
            bidder.append([bids[i], i])
        bidder = sorted(bidder)
        bidder.reverse()
        payments = [0 for i in range(bidder)]
        for i in range(len(bids)):
            sum = 0.0
            for j in range(len(bids)-1,-1,-1):
                payments[j] = sum
                if(j):
                    sum+=(self.ctrs[j-1]-self.ctrs[j])*bidder[j][0]

        allocation = [bidder[i][1] for i in range(len(bidder))]
        return [allocation,payments]



class GSP(Mechanism):

    def calcAllocationAndPayments(self, bids):
        #print(bids)
        bidder = []
        for i in range(len(bids)):
            bidder.append([bids[i], i])
        bidder = sorted(bidder)
        bidder.reverse()
        allocation = [bidder[i][1] for i in range(len(bidder))]
        payments = [bidder[i+1][0] for i in range(len(bidder)-1)]
        payments.append(0)
        #print(allocation,payments)
        return [allocation,payments]