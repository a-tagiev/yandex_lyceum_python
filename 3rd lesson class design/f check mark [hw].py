class CheckMark:
    def __init__(self, point1, point2, point3):
        self.points = [point1, point2, point3]

    def __bool__(self):
        xarr = []
        yarr = []
        for i in range(3):
            xarr.append(self.points[i].x)
        for i in range(3):
            yarr.append(self.points[i].y)
        if yarr[1]!=xarr[1]:
            return False
        if yarr[1] == xarr[1] and sorted(xarr) == sorted(yarr):
            return True

        x1, y1 = self.points[0].x, self.points[0].y
        x2, y2 = self.points[1].x, self.points[1].y
        x3, y3 = self.points[2].x, self.points[2].y

        return not (x2 - x1) * (y3 - y1) == (x3 - x1) * (y2 - y1)

    def __eq__(self, other):
        return bool(self.points)==bool(other.points)

    def __repr__(self):
        return "".join([point.name for point in self.points])


class Point:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def __eq__(self, other):

        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"{self.name}({self.x}, {self.y})"


p_A = Point('A', 1, 2)
p_B = Point('B', 0, 1)
p_C = Point('C', -1, 2)
p_D = Point('D', -1, 2)
cm_ABC = CheckMark(p_A, p_B, p_C)
cm_CBA = CheckMark(p_C, p_B, p_A)
cm_ACB = CheckMark(p_A, p_C, p_B)
cm_ABD = CheckMark(p_A, p_B, p_D)
cm_DBA = CheckMark(p_D, p_B, p_A)
print(cm_ABC == cm_CBA, cm_ABC == cm_ABD)
print(cm_ABC == cm_DBA, cm_ABC == cm_ACB)