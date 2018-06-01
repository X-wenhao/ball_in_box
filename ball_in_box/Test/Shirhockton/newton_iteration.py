import math
import numpy as np
def newton_iteration(condition):
    x0 = condition[1][0]
    y0 = condition[1][1]
    r0 = condition[1][2]
    x1 = condition[2][0]
    y1 = condition[2][1]
    r1 = condition[2][2]
    X=[[],[],[]]
    X=np.mat(X)
