import numpy as np
import warnings

class ValuationGenerator:
    def generate():
        return np.random_random_sample()

class uniformValuationGenerator:

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def generate(self):
        #if(np.random.random_sample()<0.75):
            #print('a')
            #return np.random.random_sample() * (self.right - self.left)*0.3 + self.left
        #else:
        return np.random.random_sample() * (self.right - self.left) + self.left

class normalValuationGenerator:

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def generate(self):
        pass
        