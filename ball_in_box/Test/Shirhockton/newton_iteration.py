import math
import numpy as np
def newton_iteration(condition):

    x0 = condition[0][0]
    y0 = condition[0][1]
    r0 = condition[0][2]

    x1 = condition[1][0]
    y1 = condition[1][1]
    r1 = condition[1][2]

    x2 = condition[2][0]
    y2 = condition[2][1]
    r2 = condition[2][2]

    X0=np.matr(0,0,1)

    F=[[x0**2+y0**2-(r0+1)**2],
        [x1**2+y1**2-(r1+1)**2],
        [x2**2+y2**2-(r2+1)**2]]

    F1 =[[x0**2+y0**2-(r0+1)**2],
         [x1**2+y1**2-(r1+1)**2],
         [x2**2+y2**2-(r2+1)**2]]

    X1=X0-F1.I*F


    while np.linalg.norm(X1-X0)>1e-8:
        
        X0=X1

        F=[
             [(X0[0,0]-x0)**2+(X0[0,1]-y0)**2-(X0[0,3]+r0)**2],
             [(X0[1,0]-x0)**2+(X0[1,1]-y0)**2-(X0[1,3]+r0)**2],
             [(X0[2,0]-x0)**2+(X0[2,1]-y0)**2-(X0[2,3]+r0)**2]
            ]

        F1 = [
              [(X0[0, 0] - x0) * 2 + (X0[0, 1] - y0) * 2 - (X0[0, 3] + r0) * 2],
              [(X0[1, 0] - x0) * 2 + (X0[1, 1] - y0) * 2 - (X0[1, 3] + r0) * 2],
              [(X0[2, 0] - x0) * 2 + (X0[2, 1] - y0) * 2 - (X0[2, 3] + r0) * 2]
             ]
        X1 = X0 - F1.I * F


    return ([(X1[0,0],X1[1,0],X1,[2,0])])

