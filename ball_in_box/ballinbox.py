import math
import random
#from .validate import validate
from validate import*
from matplotlib.patches import Circle
import matplotlib.pyplot as plt

__all__ = ['ball_in_box']

def draw(circles,blockers):    
    fig = plt.figure(figsize=(6,6))
    ax = fig.add_subplot(111)
    for block in blockers:
        ax.scatter(block[0],block[1], c='k')
    for circle in circles:
        x = circle[0]
        y = circle[1]
        r = circle[2]    
        cir = Circle(xy = (x, y), radius=r, alpha=0.4)
        ax.add_patch(cir)
    plt.xlim(-1.0, 1.0)
    plt.ylim(-1.0, 1.0)
    plt.show()

def ball_in_box(m=5, blockers=[(0.5, 0.5), (0.5, -0.5), (0.5, 0.3)]):
    """
    m is the number circles.
    n is the list of coordinates of tiny blocks.
    
    This returns a list of tuple, composed of x,y of the circle and r of the circle.
    """
    
    circles=[]
    for circle_index in range(0,m):
        tmp_x=0.0
        tmp_y=0.0
        tmp_r=0.0
        for x in range(1,200):
            c_x=0.01*x-1.0
            for y in range(1,200):
                c_y=0.01*y-1.0
                c_r=min(1.0-1.0*abs(c_x),1.0-1.0*abs(c_y))
                tmp_circle=[(c_x,c_y,c_r)]+circles
                while (c_r>0) and (not validate(tmp_circle,blockers)) :
                    c_r=c_r-0.01
                if tmp_r<c_r:
                    tmp_r=c_r
                    tmp_x=c_x
                    tmp_y=c_y
        circles.append((tmp_x,tmp_y,tmp_r))
        print(tmp_x,tmp_y,tmp_r)
    draw(circles,blockers)
    return circles
