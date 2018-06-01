import numpy as np
import math


def get_circle_not_line(condition):

    a1 = condition[0][0]
    b1 = condition[0][1]
    r1 = condition[0][2]
    a2 = condition[1][0]
    b2 = condition[1][1]
    r2 = condition[1][2]
    a3 = condition[2][0]
    b3 = condition[2][1]
    r3 = condition[2][2]

    'm1*x+n1*y+p1*r+q1=0'
    m1 = 2 * (a1 - a2)
    n1 = 2 * (b1 - b2)
    p1 = 2 * (r1 - r2)
    q1 = a2 ** 2 - a1 ** 2 + b2 ** 2 - b1 ** 2 + r1 ** 2 - r2 ** 2
    m2 = 2 * (a1 - a3)
    n2 = 2 * (b1 - b3)
    p2 = 2 * (r1 - r3)
    q2 = a3 ** 2 - a1 ** 2 + b3 ** 2 - b1 ** 2 + r1 ** 2 - r3 ** 2

    if math.fabs(n1*m2-n2*m1)<E:
        if math.fabs(p1*m2-p2*m1)<E:
            if math.fabs(p1 * n2 - p2 * n1) < E:
                return None
            else:
                r0 = -float(q1 * n2 - q2 * n1) / (p1 * n2 - p2 * n1)
                if math.fabs(m1) < E:
                    y0 = -float(p1 * r0 + q1) / n1
                    s = (r0 + r1) ** 2 - (y0 - b1) ** 2
                    if s >= 0:
                        x01 = a1 + math.sqrt(s)
                        x02 = a1 - math.sqrt(s)
                        return [(x01, y0, r0), (x02, y0, r0)]
                    elif s >= -E:
                        x0=a1
                        return [(x0, y0, r0)]
                    else:
                        return None
                else:
                    'y=ky*x+hy'
                    ky = -float(m1) / n1
                    hy = -float(p1 * r0 + q1) / n1

                    'ay**2*x+by*x+cy=0'
                    ay = ky ** 2 + 1
                    by = 2 * (ky * hy - ky * b1 - a1)
                    cy = (hy - b1) ** 2 + a1 ** 2 - (r0 + r1) ** 2
                    dertay = by ** 2 - 4 * ay * cy
                    if dertay >= 0:
                        x01 = float(-by + math.sqrt(dertay)) / (2 * ay)
                        x02 = float(-by - math.sqrt(dertay)) / (2 * ay)
                        return [(x01, ky * x01 + hy, r0), (x02, ky * x02 + hy, r0)]
                    elif math.fabs(dertay) >= -E:
                        x0 = float(-by) / (2 * ay)
                        return [(x0, ky * x0 + hy, r0)]
                    else:
                        return None


        else:
            r0=-float(q1*m2-q2*m1)/(p1*m2-p2*m1)
            if math.fabs(m1)<E:
                y0=-float(p1*r0+q1)/n1
                s=(r0+r1)**2-(y0-b1)**2
                if s>=0:
                    x01=a1+math.sqrt(s)
                    x02=a1-math.sqrt(s)
                    return [(x01,y0,r0),(x02,y0,r0)]
                elif s>=-E:
                    x0=a1
                    return [(x0,y0,r0)]
                else:
                    return None
            else:
                'x=kx*y+hx'
                kx=-float(n1)/m1
                hx=-float(p1*r0+q1)/m1

                'ax**2*y+bx*y+cx=0'
                ax=kx**2+1
                bx=2*(kx*hx-kx*a1-b1)
                cx=(hx-a1)**2+b1**2-(r0+r1)**2
                dertax=bx**2-4*ax*cx
                if dertax>=0:
                    y01 = float(-bx + math.sqrt(dertax)) / (2 * ax)
                    y02 = float(-bx - math.sqrt(dertax)) / (2 * ax)
                    return [(kx*y01+hx,y01,r0),(kx*y02+hx,y02,r0)]
                elif math.fabs(dertax)>=-E:
                    y0= float(-bx ) / (2 * ax)
                    return [(kx*y0+hx,y0,r0)]
                else:
                    return None


    else:
        'y=k1*r+h1'
        k1 = float(p1 * m2 - p2 * m1) / (n2 * m1 - n1 * m2)
        h1 = float(q1 * m2 - q2 * m1) / (n2 * m1 - n1 * m2)
        k2 = float(p1 * n2 - p2 * n1) / (n1 * m2 - n2 * m1)
        h2 = float(q1 * n2 - q2 * n1) / (n1 * m2 - n2 * m1)

        'a*r**2+b*r+c=0'
        a = k1 ** 2 + k2 ** 2 - 1
        b = 2 * (k2 * h2 + k1 * h1 - a1 * k2 - b1 * k1 - r1)
        c = a1 ** 2 + b1 ** 2 + h1 ** 2 + h2 ** 2 - 2 * a1 * h2 - 2 * b1 * h1 - r1 ** 2
        derta = b ** 2 - 4 * a * c

        '只存在一个解'
        if math.fabs(a) < E:
            r0 = -float(c) / b
            x0 = k2 * r0 + h2
            y0 = k1 * r0 + h1
            return [(x0, y0, r0)]


        '存在两个解'
        if derta >= 0:
            r01 = float(-b + math.sqrt(derta)) / (2 * a)
            r02 = float(-b - math.sqrt(derta)) / (2 * a)
            if r01 >= -E:
                x0 = k2 * r01 + h2
                y0 = k1 * r01 + h1
                return [(x0, y0, r01)]
            else:
                x0 = k2 * r02 + h2
                y0 = k1 * r02 + h1
                return [(x0, y0, r02)]
        elif derta >= -E:
            r0 = float(-b) / (2 * a)
            x0 = k2 * r0 + h2
            y0 = k1 * r0 + h1
            return [(x0, y0, r0)]
        else:
            return None
