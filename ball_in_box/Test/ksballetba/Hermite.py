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





def find(bound_set):
    new_bound_set = copy(bound_set) 
    max_r = 0
    for selected_3_bound in list(combinations(bound_set, 3)):
        new_bound = Bound(solve(selected_3_bound)[0],solve(selected_3_bound)[1],solve(selected_3_bound)[2])        
        # set_trace()
        if new_bound.fit_all(new_bound_set) and new_bound.r > max_r:
            max_r = new_bound.r
            max_bound = new_bound                
    new_bound_set.append(max_bound)
    return new_bound_set




  def solve(three_bounds):
    def fi(solution,bound):
        if bound.x == INFT :
            return solution[0] + solution[2] - 1.0
        elif bound.x == - INFT :
            return solution[0] - solution[2] - 0.0
        elif bound.y == INFT :
            return solution[1] + solution[2] - 1.0
        elif bound.y == - INFT :
            return solution[1] - solution[2] - 0.0    
        else:
