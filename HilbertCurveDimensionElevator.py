class HilberCurveDown:
    def __init__(self):
        self.numLayers = 1

    def layerFinder(self, maxX, maxY):
        done = True
        li = 2
        while done:
            if maxX <= li and maxY <= li:
                done = False
            else:
                self.numLayers += 1
                li = pow(2, self.numLayers)

    def layerFinderUno(self, h):
        done = True
        li = 2
        while done:
            if h <= li:
                done = False
            else:
                self.numLayers += 1
                li = pow(2, self.numLayers)

    def setLayers(self, n):
        self.numLayers = n

    def getLayers(self):
        return self.numLayers

    def h0start(self, xy):
        q = 0
        xs = 1
        ys = 1
        x = xy[0][0]
        y = xy[0][1]
        xy.remove(xy[0])
        if xs == x and ys == y:
            q = 1
            if len(xy) == 0:
                return q
            else:
                return self.h1([None, q], xy)
        else:
            ys += 1
            if xs == x and ys == y:
                q = 2
                if len(xy) == 0:
                    return q
                else:
                    return self.h0([None, q], xy)
            else:
                xs += 1
                if xs == x and ys == y:
                    q = 3
                    if len(xy) == 0:
                        return q
                    else:
                        return self.h0([None, q], xy)
                else:
                    ys -= 1
                    if xs == x and ys == y:
                        q = 4
                        if len(xy) == 0:
                            return q
                        else:
                            return self.h2([None, q], xy)

    def h0(self, qP, xy):
        xs = 1
        ys = 1
        x = xy[0][0]
        y = xy[0][1]
        xy.remove(xy[0])
        if xs == x and ys == y:
            qP.append(1)
            qP = [z for z in qP if z is not None]
            if len(xy) == 0:
                return qP
            else:
                return self.h1(qP, xy)
        else:
            ys += 1
            if xs == x and ys == y:
                qP.append(2)
                qP = [z for z in qP if z is not None]
                if len(xy) == 0:
                    return qP
                else:
                    return self.h0(qP, xy)
            else:
                xs += 1
                if xs == x and ys == y:
                    qP.append(3)
                    qP = [z for z in qP if z is not None]
                    if len(xy) == 0:
                        return qP
                    else:
                        return self.h0(qP, xy)
                else:
                    ys -= 1
                    if xs == x and ys == y:
                        qP.append(4)
                        qP = [z for z in qP if z is not None]
                        if len(xy) == 0:
                            return qP
                        else:
                            return self.h2(qP, xy)

    def h1(self, qP, xy):
        xs = 1
        ys = 1
        x = xy[0][0]
        y = xy[0][1]
        xy.remove(xy[0])
        if xs == x and ys == y:
            qP.append(1)
            qP = [z for z in qP if z is not None]
            if len(xy) == 0:
                return qP
            else:
                return self.h0(qP, xy)
        else:
            xs += 1
            if xs == x and ys == y:
                qP.append(2)
                qP = [z for z in qP if z is not None]
                if len(xy) == 0:
                    return qP
                else:
                    return self.h1(qP, xy)
            else:
                ys += 1
                if xs == x and ys == y:
                    qP.append(3)
                    qP = [z for z in qP if z is not None]
                    if len(xy) == 0:
                        return qP
                    else:
                        return self.h1(qP, xy)
                else:
                    xs -= 1
                    if xs == x and ys == y:
                        qP.append(4)
                        qP = [z for z in qP if z is not None]
                        if len(xy) == 0:
                            return qP
                        else:
                            return self.h3(qP, xy)

    def h2(self, qP, xy):
        x = xy[0][0]
        y = xy[0][1]
        xy.remove(xy[0])
        xs = 2
        ys = 2
        if xs == x and ys == y:
            qP.append(1)
            qP = [z for z in qP if z is not None]
            if len(xy) == 0:
                return qP
            else:
                return self.h3(qP, xy)
        else:
            xs -= 1
            if xs == x and ys == y:
                qP.append(2)
                qP = [z for z in qP if z is not None]
                if len(xy) == 0:
                    return qP
                else:
                    return self.h2(qP, xy)
            else:
                ys -= 1
                if xs == x and ys == y:
                    qP.append(3)
                    qP = [z for z in qP if z is not None]
                    if len(xy) == 0:
                        return qP
                    else:
                        return self.h2(qP, xy)
                else:
                    xs += 1
                    if xs == x and ys == y:
                        qP.append(4)
                        qP = [z for z in qP if z is not None]
                        if len(xy) == 0:
                            return qP
                        else:
                            return self.h0(qP, xy)

    def h3(self, qP, xy):
        x = xy[0][0]
        y = xy[0][1]
        xy.remove(xy[0])
        xs = 2
        ys = 2
        if xs == x and ys == y:
            qP.append(1)
            qP = [z for z in qP if z is not None]
            if len(xy) == 0:
                return qP
            else:
                return self.h2(qP, xy)
        else:
            ys -= 1
            if xs == x and ys == y:
                qP.append(2)
                qP = [z for z in qP if z is not None]
                if len(xy) == 0:
                    return qP
                else:
                    return self.h3(qP, xy)
            else:
                xs -= 1
                if xs == x and ys == y:
                    qP.append(3)
                    qP = [z for z in qP if z is not None]
                    if len(xy) == 0:
                        return qP
                    else:
                        return self.h3(qP, xy)
                else:
                    ys += 1
                    if xs == x and ys == y:
                        qP.append(4)
                        qP = [z for z in qP if z is not None]
                        if len(xy) == 0:
                            return qP
                        else:
                            return self.h1(qP, xy)

    def xYToZVal(self, x, y):
        xy = [[i for i in range(0, 2)]for j in range(0, self.numLayers)]
        xT = x
        yT = y
        xy[0][0] = x
        xy[0][1] = y
        for i in range(1, self.numLayers):
            xEven = True if xT % 2 == 0 else False
            yEven = True if yT % 2 == 0 else False
            xy[i][0] = (xT/2) if xEven else ((xT+1)/2)
            xy[i][1] = (yT/2) if yEven else ((yT+1)/2)
            xT = xy[i][0]
            yT = xy[i][1]
        xy2x2 = list()
        for index, item in enumerate(xy):
            xEven = True if item[0] % 2 == 0 else False
            yEven = True if item[1] % 2 == 0 else False
            x = 2 if xEven else 1
            y = 2 if yEven else 1
            lisXY = list([x, y])
            xy2x2.append(lisXY)
        xy2x2P = list()
        for item in reversed(xy2x2):
            xy2x2P.append(item)
        qVals = self.h0start(xy2x2P)
        d = -1
        if self.numLayers > 1:
            for i in range(1, self.numLayers):
                if i == 1:
                    d = 4*qVals[i-1]+qVals[i]-4
                else:
                    d = 4*d+qVals[i]-4

        else:
            d = qVals
        return d
# HilberCurveDown ends
# ------------------------------------


class HilberCurveUP():
    def __init__(self, val, height):
        self.val = val
        self.numLayers = 1
        self.layerFinder(height)

    def layerFinder(self, h):
        done = True
        li = 2
        while done:
            if h <= li:
                done = False
            else:
                self.numLayers += 1
                li = pow(2, self.numLayers)

    def h0start(self, qVal):
        q = qVal[0]
        qVal.remove(qVal[0])
        if q == 1:
            if len(qVal) == 0:
                return [1, 1]
            else:
                return self.h1([None, [1, 1]], qVal)
        elif q == 2:
            if len(qVal) == 0:
                return [1, 2]
            else:
                return self.h0([None, [1, 2]], qVal)
        elif q == 3:
            if len(qVal) == 0:
                return [2, 2]
            else:
                return self.h0([None, [2, 2]], qVal)
        else:
            if len(qVal) == 0:
                return [2, 1]
            else:
                return self.h2([None, [2, 1]], qVal)

    def h0(self, xy, qVal):
        q = qVal[0]
        qVal.remove(qVal[0])
        if q == 1:
            xy.append([1, 1])
            xy = [z for z in xy if z is not None]
            if len(qVal) == 0:
                return xy
            else:
                return self.h1(xy, qVal)
        elif q == 2:
            xy.append([1, 2])
            xy = [z for z in xy if z is not None]
            if len(qVal) == 0:
                return xy
            else:
                return self.h0(xy, qVal)
        elif q == 3:
            xy.append([2, 2])
            xy = [z for z in xy if z is not None]
            if len(qVal) == 0:
                return xy
            else:
                return self.h0(xy, qVal)
        else:
            xy.append([2, 1])
            xy = [z for z in xy if z is not None]
            if len(qVal) == 0:
                return xy
            else:
                return self.h2(xy, qVal)

    def h1(self, xy, qVal):
        print("h1")
        q = qVal[0]
        qVal.remove(qVal[0])
        if q == 1:
            xy.append([1, 1])
            xy = [z for z in xy if z is not None]
            if len(qVal) == 0:
                return xy
            else:
                return self.h0(xy, qVal)
        elif q == 2:
            xy.append([2, 1])
            xy = [z for z in xy if z is not None]
            if len(qVal) == 0:
                return xy
            else:
                return self.h1(xy, qVal)
        elif q == 3:
            xy.append([2, 2])
            xy = [z for z in xy if z is not None]
            if len(qVal) == 0:
                return xy
            else:
                return self.h1(xy, qVal)
        else:
            xy.append([1, 2])
            xy = [z for z in xy if z is not None]
            if len(qVal) == 0:
                return xy
            else:
                return self.h3(xy, qVal)

    def h2(self, xy, qVal):
        q = qVal[0]
        qVal.remove(qVal[0])
        if q == 1:
            xy.append([2, 2])
            xy = [z for z in xy if z is not None]
            if len(qVal) == 0:
                return xy
            else:
                return self.h3(xy, qVal)
        elif q == 2:
            xy.append([2, 1])
            xy = [z for z in xy if z is not None]
            if len(qVal) == 0:
                return xy
            else:
                return self.h2(xy, qVal)
        elif q == 3:
            xy.append([1, 1])
            xy = [z for z in xy if z is not None]
            if len(qVal) == 0:
                return xy
            else:
                return self.h2(xy, qVal)
        else:
            xy.append([2, 1])
            xy = [z for z in xy if z is not None]
            if len(qVal) == 0:
                return xy
            else:
                return self.h0(xy, qVal)

    def h3(self, xy, qVal):
        q = qVal[0]
        qVal.remove(qVal[0])
        if q == 1:
            xy.append([2, 2])
            xy = [z for z in xy if z is not None]
            if len(qVal) == 0:
                return xy
            else:
                return self.h2(xy, qVal)
        elif q == 2:
            xy.append([2, 1])
            xy = [z for z in xy if z is not None]
            if len(qVal) == 0:
                return xy
            else:
                return self.h3(xy, qVal)
        elif q == 3:
            xy.append([1, 1])
            xy = [z for z in xy if z is not None]
            if len(qVal) == 0:
                return xy
            else:
                return self.h3(xy, qVal)
        else:
            xy.append([1, 2])
            xy = [z for z in xy if z is not None]
            if len(qVal) == 0:
                return xy
            else:
                return self.h1(xy, qVal)

    def findXY(self):
        qVals = [None]*self.numLayers
        for i, item in enumerate(reversed(qVals)):
            if self.val % 4 == 0:
                qVals[i] = 4  # q = 4-0
                self.val /= 4  # next = (val-4+q)/4
            elif (self.val+1) % 4 == 0:
                qVals[i] = 3  # q = 4-1
                self.val = (self.val+1)/4  # next = (val-4+q)/4
            elif (self.val+2) % 4 == 0:
                qVals[i] = 2  # q = 4-2
                self.val = (self.val+2)/4  # next = (val-4+q)/4
            else:
                qVals[i] = 1  # q = 4-3
                self.val = (self.val+3)/4  # next = (val-4+q)/4
        qValsP = []
        for item in reversed(qVals):
            qValsP.append(item)
        xy2x2 = self.h0start(qValsP)
        zVal = [xy2x2[0][0], xy2x2[0][1]]
        for i, item in enumerate(xy2x2):
            x = item[0]
            y = item[1]
            if i != 0:
                xEven = True if x % 2 == 0 else False
                yEven = True if y % 2 == 0 else False
                zX = (zVal[0]*2) if xEven else (zVal[0]*2)-1
                zY = (zVal[1]*2) if yEven else (zVal[1]*2)-1
                zVal = [zX, zY]
        return zVal
# ---------------------------------


# start of user interaction
fin = True
options = "1) (x, y) to singular value\n"
options = options+"2) singular value to (x, y)"
while fin:
    print("Choose the option you want by typing in the corresponding number:")
    print(options)
    userAns = input("Option: ")
    if userAns == "1":
        x = int(input("Enter x value: "))
        y = int(input("Enter y value: "))
        hFin = HilberCurveDown()
        s = "Do you know the size of the grid? Enter \'y\' or \'n\': "
        userAns = input(s)
        if userAns == 'y':
            gridSize = int(input("Max x or y length: "))
            hFin.layerFinder(gridSize, gridSize)
        else:
            print("Finding number of layers:")
            hFin.layerFinder(x, y)
            print("Number of layers: ", hFin.getLayers())
            gSize = 2**hFin.getLayers()
            print("Grid size detected: ", gSize, "x", gSize)
        print("d val: "+str(hFin.xYToZVal(x, y)))
    else:
        hFin = HilberCurveUP
        val = int(input("Enter your value: "))
        s = "Do you know the size of the grid? Enter \'y\' or \'n\': "
        userAns = input(s)
        if userAns == 'y':
            gridSize = int(input("Max x or y length: "))
            hFin = HilberCurveUP(val, gridSize)
        else:
            hFin = HilberCurveUP(val, val)
        print("(x, y) vals: "+str(hFin.findXY()))
    quit = input("Quit: ")
    if quit == 'y':
        fin = False
