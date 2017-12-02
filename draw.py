import sys
import io
import matplotlib
import matplotlib.pyplot as plt
import string
import numpy as np
import warnings

class Draw:
    def __init__(self,x_axis,y_axis,xlabel,ylabel,title):
        if len(x_axis) == len(y_axis):
            plt.figure()
            plt.xlabel(xlabel)
            plt.ylabel(ylabel)
            plt.title(title)
            plt.plot(x_axis,y_axis)
            # plt.legend() 如果有多条线才用
            plt.show()
            plt.savefig(title+".png")
        else:
            print("The lengths of x_axis and y_axis are not matched")