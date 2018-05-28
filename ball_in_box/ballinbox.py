import math
import random
from ball_in_box.validate import validate
import matplotlib.pyplot as plt
import numpy as np

E=1e-8

__all__ = ['ball_in_box']

def ball_in_box(m=5, blockers=[(0.5, 0.5), (0.5, -0.5), (0.5, 0.3)]):
    """
    m is the number circles.
    n is the list of coordinates of tiny blocks.
    
    This returns a list of tuple, composed of x,y of the circle and r of the circle.
    """

    # The following is an example implementation.
    conditions=[(0,),(1,),(2,),(3,)] #x=1 x=-1 y=1 y=-1
    conditions.extend(list((i[0],i[1],0) for i in blockers))

    circles = []
    for p in range(0,m):
        con_len=len(conditions)
        re=[]
        for a in ((i,j,k) for i in range(0,con_len-2) for j in range (i+1,con_len-1) for k in range(j+1,con_len)):
            condition=list(conditions[t] for t in a)
            tmp=get_circle(condition)
            
            if tmp is not None:
                re.extend(tmp)
            print(condition,tmp)
            
        print(re)
        re=list(i[0][-1] for i in list(filter(my_validate,list((circles+[i],blockers) for i in re))))
        print(re)
        tmp=re[0]
        for c in re:
            if c[2]>tmp[2]:
                tmp=c
        circles.append(tmp)
        conditions.append(tmp)
    print(circles)
    draw(blockers,circles)
    return circles

def my_validate(c):
        return validate(c[0],c[1])

def draw(blockers,circles):
    fig=plt.figure()
    ax=fig.gca()
    plt.xlim((-1,1))
    plt.ylim((-1,1))
    
    for i in blockers:
        plt.scatter(i[0],i[1],color='', marker='o', edgecolors='g', s=20)
    for i in circles:
        if len(i)==1:
            continue
        circle = plt.Circle((i[0], i[1]), i[2], color='r',fill=False)
        ax.add_artist(circle)
    plt.show()

'''
    构建一个圆
    返回值为（x,y,r）
    condition=【（），（），（）】，其中元组为 圆(x,y,r) 
    PS：直线抽象成圆
'''
def get_circle(condition):
    len_con=list(len(i) for i in condition)
    
    if len_con[0]==1 and len_con[1]==1 and len_con[2]==1:
        return get_circle_three_line(condition)
    
    if len_con[0]==1 and len_con[1]==1:
        x=condition[2][0]
        y=condition[2][1]
        r=condition[2][2]
        
        if condition[0][0]==0 and condition[1][0]==1:
            return get_circle_two_line_1(condition)
        if condition[0][0]==2 and condition[1][0]==3:
            tmp=[]
            tmp.extend(condition[:-1])
            tmp.append((y,x,r))
            re=get_circle_two_line_1(tmp)
            return list((i[1],i[0],i[2]) for i in re)
        
        if condition[0][0]==0 and condition[1][0]==2: #x=1,y=1
            return get_circle_two_line_2(condition)
        if condition[0][0]==0 and condition[1][0]==3: #x=1,y=-1
            tmp=[]
            tmp.extend(condition[:-1])
            tmp.append((x,-y,r))
            re=get_circle_two_line_2(tmp)
            if re is not None:
                return list((i[0],-i[1],i[2]) for i in re)
        if condition[0][0]==1 and condition[1][0]==2: #x=-1,y=1
            tmp=[]
            tmp.extend(condition[:-1])
            tmp.append((-x,y,r))
            re=get_circle_two_line_2(tmp)
            if re is not None:
                return list((-i[0],i[1],i[2]) for i in re)
        if condition[0][0]==1 and condition[1][0]==3: #x=-1,y=-1
            tmp=[]
            tmp.extend(condition[:-1])
            tmp.append((-x,-y,r))
            re=get_circle_two_line_2(tmp)
            if re is not None:
                return list((-i[0],-i[1],i[2]) for i in re)
        return None
    if len_con[0]==1 :
        x0=condition[1][0]
        y0=condition[1][1]
        r0=condition[1][2]
        x1=condition[2][0]
        y1=condition[2][1]
        r1=condition[2][2]
        
        if condition[0][0]==0:  #x=1
            return get_circle_one_line(condition)
        if condition[0][0]==1:  #x=-1
            tmp=[condition[0]]
            tmp.extend([(-x0,y0,r0),(-x1,y1,r1)])
            re=get_circle_one_line(tmp)
            if re is not None:
                return list((-i[0],i[1],i[2]) for i in re)
        if condition[0][0]==2:  #y=1
            tmp=[condition[0]]
            tmp.extend([(y0,x0,r0),(y1,x1,r1)])
            re=get_circle_one_line(tmp)
            if re is not None:
                return list((i[1],i[0],i[2]) for i in re)
        if condition[0][0]==3:  #y=-1
            tmp=[condition[0]]
            tmp.extend([(-y0,x0,r0),(-y1,x1,r1)])
            re=get_circle_one_line(tmp)
            if re is not None:
                return list((i[1],-i[0],i[2]) for i in re)
        return None
    return get_circle_zero_line(condition)
def get_circle_three_line(condition):
    return [(0.0,0.0,1.0)]
    
def get_circle_two_line_1(condition):
    a1=condition[2][0]
    b1=condition[2][1]
    r1=condition[2][2]
    derta=(r1+1)**2-a1**2
    y_0=b1+derta**0.5
    y_1=b1-derta**0.5
    return [(0,y_0,1),(0,y_1,1)]

def get_circle_two_line_2(condition):
    a1=condition[2][0]
    b1=condition[2][1]
    r1=condition[2][2]
    
    b=-2*(a1+b1-r1-1)
    c=a1**2+b1**2-(r1+1)**2
    derta=b**2-4*c
    if math.fabs(derta)<E:
        x=-b/2
        return [(x,x,1-x)]
    if derta>0:
        x_0=(-b+derta**0.5)/2
        x_1=(-b-derta**0.5)/2
        return [(x_0,x_0,1-x_0),(x_1,x_1,1-x_1)]
    
    return None

def get_circle_one_line(condition):
    a1=condition[1][0]
    b1=condition[1][1]
    r1=condition[1][2]
    a2=condition[2][0]
    b2=condition[2][1]
    r2=condition[2][2]
    
    m1=2*(r1+1-a1)
    n1=a1**2-(r1+1)**2+b1**2
    m2=2*(r2+1-a2)
    n2=a2**2-(r2+1)**2+b2**2

    if math.fabs(m1-m2)<E:
        y_0=(n1*m2-n2*m1)/(2*b1*m2-2*b2*m1)
        x_0=-(n1+y_0**2-2*b1*y_0)/m1
        return [(x_0,y_0,1-x_0)]
    a=m2-m1
    b=-(2*b1*m2-2*b2*m1)
    c=(n1*m2-n2*m1)
    derta=b**2-4*a*c
    if math.fabs(derta)<E:
        y_0=-b/2.0/a
        x_0=-(n1+y_0**2-2*b1*y_0)/m1
        return [(x_0,y_0,1-x_0)]
    if derta>0:
        y_0=(-b+derta**0.5)/2.0/a
        x_0=-(n1+y_0**2-2*b1*y_0)/m1
        y_1=(-b-derta**0.5)/2.0/a
        x_1=-(n1+y_0**2-2*b1*y_0)/m1
        return [(x_0,y_0,1-x_0),(x_1,y_1,1-x_1)]
    return None

def get_circle_zero_line(condition):
    a1 = condition[0][0]
    b1 = condition[0][1]
    r1 = condition[0][2]
    a2 = condition[1][0]
    b2 = condition[1][1]
    r2 = condition[1][2]
    a3 = condition[2][0]
    b3 = condition[2][1]
    r3 = condition[2][2]

    #m1*x+n1*y+p1*r+q1=0
    m1 = 2 * (a1 - a2)
    n1 = 2 * (b1 - b2)
    p1 = 2 * (r1 - r2)
    q1 = a2 ** 2 - a1 ** 2 + b2 ** 2 - b1 ** 2 + r1 ** 2 - r2 ** 2
    m2 = 2 * (a1 - a3)
    n2 = 2 * (b1 - b3)
    p2 = 2 * (r1 - r3)
    q2 = a3 ** 2 - a1 ** 2 + b3 ** 2 - b1 ** 2 + r1 ** 2 - r3 ** 2
    print("m1:{} n1:{} p1:{} q1:{} m2:{} n2:{} p2:{} q2:{} ".format(m1,n1,p1,q1,m2,n2,p2,q2))
    #y=k1*r+h1
    k1=float(p1*m2-p2*m1)/(n2*m1-n1*m2)
    #print(k1)
    h1=float(q1*m2-q2*m1)/(n2*m1-n1*m2)
    k2=float(p1*n2-p2*n1)/(n1*m2-n2*m1)
    h2=float(q1*n2-q2*n1)/(n1*m2-n2*m1)
    print("k1:{} h1:{} k2:{} h2:{} ".format(k1,h1,k2,h2))
    'a*r**2+b*r+c=0'
    a=k1**2+k2**2-1
    b=2*(k2*h2+k1*h1-a1*k2-b1*k1-r1)
    c=a1**2+b1**2+h1**2+h2**2-2*a1*h2-2*b1*h1-r1**2
    derta=b**2-4*a*c
    print("a:{} b:{} c:{} derta:{}".format(a,b,c,derta))
    #只存在一个解
    if 0==a:
        r0=-float(c)/b
        x0 = k2 * r0 + h2
        y0 = k1 * r0 + h1
        return [(x0, y0, r0)]
    #存在两个解
    if derta>=0:
        r01 = float(-b + math.sqrt(derta)) / (2 * a)
        r02 = float(-b - math.sqrt(derta)) / (2 * a)
        re=[]
        if r01>=0:
            x0 = k2 * r01 + h2
            y0 = k1 * r01 + h1
            re.append((x0, y0, r01))
        elif r02>=0:
            x0 = k2 * r02 + h2
            y0 = k1 * r02 + h1
            re.append((x0, y0, r02))
        return re
    else:
        return None

def if_line(condition):
    a1 = condition[0][0]
    b1 = condition[0][1]
    a2 = condition[1][0]
    b2 = condition[1][1]
    a3 = condition[2][0]
    b3 = condition[2][1]
    if 0==(b2-b1)*(a3-a1)-(b3-b1)*(a2-a1):
        return True
    else:
        return False
    
if __name__=='__main__':
    conditions=[[(0,),(1,),(2,)],
               [(1,),(2,),(3,)],
               
               [(0,),(1,),(0,0,0)],
               [(0,),(1,),(0.5,0.5,0.2)],
               [(2,),(3,),(0.5,0.5,0.2)],
               
               [(0,),(2,),(0.5,0.5,0.2)],
               [(0,),(2,),(-0.5,0.5,0.2)],
               [(0,),(3,),(0.5,0.5,0.2)],
               [(1,),(2,),(0.5,0.5,0.2)],
               [(1,),(3,),(0.5,0.5,0.2)],
               
               [(0,),(0.5,-0.5,0.2),(0.5,0.5,0.2)],
               [(0,),(0,0,0.3),(0.5,0.5,0.2)],
               [(1,),(0,0,0.3),(0.5,0.5,0.2)],
               [(2,),(0,0,0.3),(0.5,0.5,0.2)],
               [(3,),(0,0,0.3),(0.5,0.5,0.2)],
               ]
    condition=conditions[-1]
    re=get_circle(condition)
    print(condition,re)
    draw([],condition+re)
