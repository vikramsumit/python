class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # def __repr__(self):
    #     return f"Point({self.x}, {self.y})"

class LineSegment(Point):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1)
        self.end_point = Point(x2, y2)

    def length(self):
        return ((self.end_point.x - self.x)**2 + (self.end_point.y - self.y)**2)**0.5

    def __repr__(self):
        return f"LineSegment({self.x}, {self.y}) to ({self.end_point.x}, {self.end_point.y})"

# Pt = Point(5 , 5)
# print(Pt)
line = LineSegment(-8, 5.09, 3.6, -4.5)
print(line)  
print(f"Length: {line.length()}")  
