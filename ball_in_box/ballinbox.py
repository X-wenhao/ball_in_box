import math
import random
from .validate import validate
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
    
    dot=2000
    step=0.001
    circles=[]
    for circle_index in range(0,m):
        tmp_x=0.0
        tmp_y=0.0
        tmp_r=0.0
        c_len=len(circles)
        for x in range(1,dot):
            c_x=step*x-1.0
            for y in range(1,dot):
                c_y=step*y-1.0
                c_r=min(1.0-1.0*abs(c_x),1.0-1.0*abs(c_y))
                for c_i in range(0,c_len):
                    delt_r=math.sqrt((c_x-circles[c_i][0])**2+(c_y-circles[c_i][1])**2)-circles[c_i][2]
                    c_r=min(delt_r,c_r)
                for b_i in blockers:
                    c_r=min(math.sqrt((c_x-b_i[0])**2+(c_y-b_i[1])**2),c_r)
                if tmp_r<c_r:
                    tmp_r=c_r
                    tmp_x=c_x
                    tmp_y=c_y
        circles.append((tmp_x,tmp_y,tmp_r))
        print(tmp_x,tmp_y,tmp_r)
    draw(circles,blockers)
    return circles
