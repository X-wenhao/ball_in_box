import math
import random
from .validate import validate

__all__ = ['ball_in_box']

def ball_in_box(m=5, blockers=[(0.5, 0.5), (0.5, -0.5), (0.5, 0.3)]):
    """
    m is the number circles.
    n is the list of coordinates of tiny blocks.
    
    This returns a list of tuple, composed of x,y of the circle and r of the circle.
    """

    # The following is an example implementation.
    conditions=[(0,-10**10,10**10-1),(0,10**10,10**10-1),(-10**10,0,10**10-1),(10**10,0,10**10-1)]
    conditions.extend(blockers)

    circles = []
    for circle_index in range(m):

        x = random.random()*2 - 1
        y = random.random()*2 - 1
        r = random.random()*0.1

        circles.append((x, y, r))
        while not validate(circles, blockers):
            x = random.random()*2 - 1
            y = random.random()*2 - 1
            r = random.random()*0.1
            circles[circle_index] = (x, y, r)

        circle_index += 1
    
    return circles


'''
    构建一个圆
    返回值为（x,y,r）
    condition=【（），（），（）】，其中元组为 圆(x,y,r) 
    PS：直线抽象成圆
'''
def get_circle(condition):


    return