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

class CoefficientStrategy(Strategy):

    def __init__(self,c = 0.5):
        self.c=c
    def bid(self, valuation):
        return self.c * valuation

class SubstractionStrategy(Strategy):

    def __init__(self,x = 1):
        self.x = x
    def bid(self, valuation):
        return max(0, valuation - self.x)
class MaxStrategy(Strategy):
    def get_f(self, x, valuation):
        return (x-x*np.log(x))*(valuation - x)
    def bid(self, valuation):
        a,b = 0,0
        for i in range(1,10001):
            c = self.get_f(i/10000.0, valuation)
            if((b-a)*(b-c)>0):
                x = i/10000.0
                sum = -valuation * np.log(x) + 2 * x * np.log(x) - x
                print(valuation, i/10000.0,valuation * 0.4,sum)
                return i/10000.0
            a = b
            b = c
        return 1

class PolyStrategy(Strategy):

    def __init__(self,k,p):
        self.history = []
        self.k = k
        self.p = p
        pass
    
    def learn(self,h):
        for i in range(len(self.history)):
            if(self.history[i][1]==h[1]):
                self.history[i] = h
                return None
        self.history.append(h)

    def bid(self, valuation):
        ValueRange = [0, valuation]
        warnings.simplefilter('ignore', np.RankWarning)
        l=len(self.history)
        p = self.p
        k = self.k
#        print("history of",self.bidderName,l)
        if l<=1:
            return valuation
        else:
            if p>l-1:
                p=l-1
            start=max(0,l-k)
            click = np.array([self.history[i][2] for i in range(start,l)])
            price = np.array([self.history[i][3] for i in range(start,l)])
            bid   = np.array([self.history[i][1] for i in range(start,l)])
            #bidMean = bid.mean()
            #bid = bid - bidMean
#            a = np.polyfit(bid,click,p)
#            b = np.polyfit(bid,click*price,p)
            c = np.polyfit(bid,click*(np.array([valuation for i in range(start,l)]) - price),p)
#            print(c)
            d = np.polyder(c)
            root = np.roots(d)
            root = [x for x in root if np.isreal(x)]
            root = np.append(root,ValueRange[0])
            root = np.append(root,ValueRange[1])
#            print(root)
            ma = np.argmax([np.polyval(c,x) for x in root if x >= ValueRange[0] and x <= ValueRange[1]])
            return ma
            #return ma+bidMean

class BarStrategy(Strategy):

    def __init__(self):
        self.n = 40 #Bar的分度值
        self.l,self.r = 0,1 #认为的valuation的范围
        self.alpha = [0 for i in range (self.n)]
        self.price = [0 for i in range (self.n)] 
        self.weight = 0.9 #新加入数据的权重
        self.weight_decline = 0.99999
        self.beside = 0.9
        self.beside_n = 10
        self.beside_decline = 0.99999
        self.eps = 0.5 #exploit的概率
        self.eps_decline = 0.99999
    
    def learn(self,h):
        pos = int(h[1] * self.n)
        if pos == self.n:
            pos -= 1
        delta = 1
        for i in range(self.beside_n):
            if pos + i < self.n:
                self.alpha[pos+i] = self.alpha[pos+i] * (1 - self.weight * delta) + h[2] * self.weight * delta
                self.price[pos+i] = self.price[pos+i] * (1 - self.weight * delta) + h[3] * self.weight * delta
            if pos - i >= 0 and i:
                self.alpha[pos-i] = self.alpha[pos-i] * (1 - self.weight * delta) + h[2] * self.weight * delta
                self.price[pos-i] = self.price[pos-i] * (1 - self.weight * delta) + h[3] * self.weight * delta
            delta *= self.beside
        self.weight *= self.weight_decline
        self.beside *= self.beside_decline

    def bid(self, valuation):
        ma,pos = 0,0
        self.eps *= self.eps_decline
        if(np.random.random_sample() < self.eps):
            return np.random.random_sample()
        for i in range(self.n):
            sum = self.alpha[i] * (valuation - self.price[i])
            if sum > ma:
                ma = sum
                pos = i
        
        if np.random.random_sample() < 0.03:
            print(self.alpha)
            print(self.eps,self.beside,self.weight)
            print(valuation,pos/(self.n+0.0))
        return pos / (self.n+0.0)