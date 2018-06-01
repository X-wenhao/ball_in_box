import math
import random
from .validate import validate

MOVE1=0.01  #第一次搜索的步长
MOVE2=0.001 #第二次搜索的步长

__all__ = ['ball_in_box']
E=1e-8
def ball_in_box(m=5, blockers=[(0.5, 0.5), (0.5, -0.3)]):
    """
    m is the number circles.
    n is the list of coordinates of tiny blocks.
    
    This returns a list of tuple, composed of x,y of the circle and r of the circle.
    """

    # The following is an example implementation.
    circles = []
    for i in range(0,m):
        maxCir=[0,0,0]
        y=-1+MOVE1
        x=-1+MOVE1
        tmpR=0
        while y<1:
            #for x in (-1+MOVE1*i for i in range(int(2/MOVE1))):
            x=-1+MOVE1
            while x<1:
                minR=1
                #边界判断
                tmpR=abs(x+1)
                if tmpR<minR:
                    minR=tmpR
                tmpR=abs(1-x)
                if tmpR<minR:
                    minR=tmpR
                tmpR=abs(y+1)
                if tmpR<minR:
                    minR=tmpR
                tmpR=abs(1-y)
                if tmpR<minR:
                    minR=tmpR
                #障碍判断
                for block in blockers:
                    tmpR=math.sqrt((x-block[0])**2+(y-block[1])**2)
                    if tmpR<minR:
                        minR=tmpR
                #圆覆盖判断
                for c in circles:
                    tmpR=math.sqrt((x-c[0])**2+(y-c[1])**2)-c[2]
                    if tmpR<minR:
                        minR=tmpR
                if minR>maxCir[2]:
                    maxCir[0]=x
                    maxCir[1]=y
                    maxCir[2]=minR
                x+=MOVE1
            y+=MOVE1
        y=maxCir[1]-10*MOVE2
        while y<maxCir[1]+10*MOVE2:
            x=maxCir[0]-10*MOVE2
            
            while x<maxCir[0]+10*MOVE2:
                minR=1
                #边界判断
                tmpR=abs(x+1)
                if tmpR<minR:
                    minR=tmpR
                tmpR=abs(1-x)
                if tmpR<minR:
                    minR=tmpR
                tmpR=abs(y+1)
                if tmpR<minR:
                    minR=tmpR
                tmpR=abs(1-y)
                if tmpR<minR:
                    minR=tmpR
                #障碍判断
                for block in blockers:
                    tmpR=math.sqrt((x-block[0])**2+(y-block[1])**2)
                    if tmpR<minR:
                        minR=tmpR
                #圆覆盖判断
                for c in circles:
                    tmpR=math.sqrt((x-c[0])**2+(y-c[1])**2)-c[2]
                    if tmpR<minR:
                        minR=tmpR
                if minR>maxCir[2]:
                    maxCir[0]=x
                    maxCir[1]=y
                    maxCir[2]=minR
                x+=MOVE2
            y+=MOVE2
        circles.append(maxCir)
        print('findone \n')
return circles
