import math
E=1e-8
def validate(circles, blockers):
    # Is circle in the box?
    for circle in circles:
        xmr = circle[0] - circle[2]
        xpr = circle[0] + circle[2]
        ymr = circle[1] - circle[2]
        ypr = circle[1] + circle[2]

        if (not (xmr <= 1+E and xmr >=-1-E )) \
           or (not (xpr <= 1+E and xpr >=-1-E )) \
           or (not (ymr <= 1+E and ymr >=-1-E )) \
           or (not (ypr <= 1+E and ypr >=-1-E )):
            #print("0",circle)
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
                if math.sqrt((x - bx)**2 + (y - by)**2) -r< -E:
                    #print("1",circle)
                    return False

    # Is circle good for each other?
    i=0
    for circle1 in circles[:-1]:
        i+=1
        for circle2 in circles[i:]:
            x1 = circle1[0]
            y1 = circle1[1]
            r1 = circle1[2]
            x2 = circle2[0]
            y2 = circle2[1]
            r2 = circle2[2]
            if math.sqrt((x1 - x2)**2 + (y1 - y2)**2) -(r1 + r2)<-E:
                #print("math:",math.sqrt((x1 - x2)**2 + (y1 - y2)**2),'  ',r1 + r2)
                #print("2",circle)
                return False

    # all good
return True
