import sys
import io
import matplotlib
import matplotlib.pyplot as plt
import string
import numpy as np
import warnings

class Draw:
    def __init__(self,x_axis,y_axis,xlabel,ylabel,name,title):
        if len(x_axis) == len(y_axis[0]):
            n = len(y_axis)
            plt.figure()
            plt.xlabel(xlabel)
            plt.ylabel(ylabel)
            plt.title(title)
            for i in range(n):
                plt.plot(x_axis,y_axis[i],label=name[i])
            plt.legend()
            plt.savefig(title+".png")
            plt.show()
        else:
            print("The lengths of x_axis and y_axis are not matched")