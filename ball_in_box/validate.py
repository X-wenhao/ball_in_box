import math

def validate(circles, blockers):
    # Is circle in the box?
    for circle in circles:
        xmr = circle[0] - circle[2]
        xpr = circle[0] + circle[2]
        ymr = circle[1] - circle[2]
        ypr = circle[1] + circle[2]

        if (not (xmr <= 1 and xmr >=-1 )) \
           or (not (xpr <= 1 and xpr >=-1 )) \
           or (not (ymr <= 1 and ymr >=-1 )) \
           or (not (ypr <= 1 and ypr >=-1 )):
            return False

    # Is circle good for blockers?
    if blockers is not None and len(blockers) > 0:
        for circle in circles:
            for block in blockers:
                x = circle[0]
                y = circle[1]
                r = circle[2]
                bx = block[0]
                by = block[1]
                if math.sqrt((x - bx)**2 + (y - by)**2) < r:
                    return False

    # Is circle good for each other?
    circleNum=len(circles)
    for circle1 in range(0,circleNum):
        for circle2 in range(circle1+1,circleNum):
            x1 = circles[circle1][0]
            y1 = circles[circle1][1]
            r1 = circles[circle1][2]
            x2 = circles[circle2][0]
            y2 = circles[circle2][1]
            r2 = circles[circle2][2]
            if math.sqrt((x1 - x2)**2 + (y1 - y2)**2) < (r1 + r2):
                return False

    # all good
    return True
