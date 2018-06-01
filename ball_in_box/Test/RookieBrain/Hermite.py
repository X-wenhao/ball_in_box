from itertools import combinations
from scipy.optimize import fsolve
from copy import copy
from pdb import set_trace
INFT = float(10**10)
class Bound(object):
  
    def __init__(self,x,y,r):
        self.x , self.y , self.r = x , y , r
        
    def fit(self,another_bound):
      
        if another_bound.x == INFT :
            return self.x + self.r <= 1.0
          
        elif another_bound.x == - INFT :
           return self.x - self.r >= 0.0
          
        elif another_bound.y == INFT :
            return self.y + self.r <= 1.0
          
        elif another_bound.y == - INFT :
            return self.y - self.r >= 0.0   
          
        else:
