class nechetkoe():
    def __init__(self, a, b, c, d, maxy=1):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.maxy = maxy

    def __str__(self):
        return " ".join([str(i) for i in [self.a, self.b, self.c, self.d, self.maxy]])

    def find_y(self, x):
        if self.b <= x <= self.c:
            return self.maxy
        elif x >= self.d or x <= self.a:
            return 0
        elif self.a <= x <= self.b:
            return (x - self.a) / (self.b - self.a)
        else:
            return (x - self.d) / (self.c - self.d)

    def obrez_y(self, x, maxy):
        return min(self.find_y(x), maxy)

    def peresech(self, second):
        pass
