class fuzzy():
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __str__(self):
        return " ".join([str(i) for i in [self.a, self.b, self.c, self.d]])

    def find_y(self, x):
        if self.b <= x <= self.c:
            return 1
        elif x >= self.d or x <= self.a:
            return 0
        elif self.a <= x <= self.b:
            return (x - self.a) / (self.b - self.a)
        else:
            return (x - self.d) / (self.c - self.d)

    def obrez_y(self, x, maxy):
        return min(self.find_y(x), maxy)

    def peresech(self, second):
        maxperesech = 0
        step = 0.01
        start = min(self.a, second.a)
        end = min(self.d, second.d)
        while start <= end:
            y1 = self.find_y(start)
            y2 = second.find_y(start)
            if abs(y1 - y2) <= 0.01 and y1 != 0 and y2 != 0:
                maxperesech = y1
                if y1 == 1:
                    return 1
            start += step
        return maxperesech
    @staticmethod
    def combine_rules(situation, rules, step):
        x = []
        result = []
        start = 0
        end = max(rules, key=lambda f: f[-1].d)[-1].d + 2
        while start <= end:
            x.append(start)
            result.append(
                max([i[-1].obrez_y(start, min([i[j].peresech(situation[j]) for j in range(len(i) - 1)])) for i in rules]))
            start += step
        return x, result

    @staticmethod
    def mass_center(x, y, step):
        s1 = 0
        s2 = 0
        for i in range(len(x)):
            s1 += x[i] * y[i] * step
            s2 += y[i] * step
        return s1 / s2


