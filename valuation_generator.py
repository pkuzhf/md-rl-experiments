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
        return np.random.random_sample() * (self.right - self.left) + self.left

