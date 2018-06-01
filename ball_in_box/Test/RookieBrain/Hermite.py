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
           return (self.r + another_bound.r)**2 <=  (self.x - another_bound.x)**2 + (self.y - another_bound.y)**2 
        # return (self.r + another_bound.r)**2 <=  (self.x - another_bound.x)**2 + (self.y - another_bound.y)**2 
    def fit_all(self,bounds):
        for i in bounds:
            if not self.fit(i):
                return False
        return True
# bound( x , y , r )
bound_set0 = [
    Bound( -INFT , 0.0 , INFT ),
    Bound( INFT , 0.0 , INFT ),
    Bound(  0.0, -INFT, INFT ),
    Bound(  0.0, INFT, INFT  ),
    Bound( 0.5, 0.5, 0)
    ] 
