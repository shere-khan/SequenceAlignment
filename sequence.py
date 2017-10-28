class StringTool:
    def __init__(self):
        # self.__prev = []
        self.A = []

    def __eq__(self, other):
        pass

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def alignment(self, s1, s2):
        for i in range(len(s1) + 1):
            self.A.append([])
            for j in range(len(s2) + 1):
                self.A[i].append(0)

        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                val1 = self.A[i - 1][j - 1]
                val2 = self.A[i][j - 1]
                val3 = self.A[i - 1][j]
                c1 = self.cost(s1[i - 1], s2[j - 1])
                c2 = self.cost(s1[i - 1], "")
                c3 = self.cost("", s2[j - 1])
                a = val1 + c1
                b = val2 + c2
                c = val3 + c3
                # a = self.A[i - 1][j - 1] + self.cost(s1[i], s2[j])
                # b = self.A[i][j - 1] + self.cost(s1[i], "")
                # c = self.A[i - 1][j] + self.cost("", s2[j])
                self.A[i][j] = min(a, b, c)

        return self.A[len(s1)][len(s2)]

    def cost(self, x, y):
        return 0 if x == y else 1

class StringCreator:
    pass
