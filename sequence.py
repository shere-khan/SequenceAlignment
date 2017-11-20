class StringTool:
    def __eq__(self, other):
        pass

    def __repr__(self):
        pass

    def __str__(self):
        pass

    @staticmethod
    def alignment_linear(x, y, f):
        m = len(x)
        n = len(y)
        prev = [i for i in range(n + 1)]
        cur = []
        for i in range(1, m + 1):
            cur = [prev[0] + 1]
            for j in range(1, n + 1):
                a = prev[j - 1] + f(x[i - 1], y[j - 1])
                # print(i, j)
                b = cur[-1] + f("", y[j - 1])
                c = prev[j] + f(x[i - 1], "")
                cur.append(min(a, b, c))

            prev = cur

        return cur[-1]

    @staticmethod
    def alignment(x, y, f):
        n = len(x)
        m = len(y)
        M = []
        StringTool.populate_base(M, m, n)
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                a = M[i - 1][j - 1][0] + f(x[i - 1], y[j - 1])
                b = M[i - 1][j][0] + f("", y[j - 1])
                c = M[i][j - 1][0] + f(x[i - 1], "")
                vals = [a, b, c]
                mynn = min(vals)
                M[i][j] = (mynn, StringTool.get_parent(vals.index(mynn), i, j))

        return M

    @staticmethod
    def populate_base(M, m, n):
        for i in range(0, n + 1):
            for j in range(0, m + 1):
                if i == 0 and j == 0:
                    M.append([(i, None)])
                elif i == 0 and j > 0:
                    M[i].append((j, (i, j - 1, 'left')))
                elif i > 0 and j == 0:
                    M.append([(i, (i - 1, j, 'up'))])
                else:
                    M[i].append((0, None))

    @staticmethod
    def get_parent(val, i, j):
        if val == 0:
            return i - 1, j - 1, 'diag'
        if val == 1:
            return i - 1, j, 'up'
        if val == 2:
            return i, j - 1, 'left'

    @staticmethod
    def __cost(x, y):
        return 0 if x == y else 1

    @staticmethod
    def unpack_alignment(M, s1, s2, r1, r2):
        if M is None:
            return 'No alignment'
        n = len(s1)
        m = len(s2)
        parent_info = M[n][m][1]
        if parent_info is None:
            return 'No alignment'

        parent_i = parent_info[0]
        parent_j = parent_info[1]
        res = StringTool.get_string(s1, s2, parent_info[2], n, m)
        r1 += res[0]
        r2 += res[1]

        r1, r2 = StringTool.__unpack_alignment(M, parent_i, parent_j, s1, s2, r1, r2)

        return r1, r2

    @staticmethod
    def __unpack_alignment(M, i, j, s1, s2, r1, r2):
        parent_info = M[i][j][1]
        if parent_info is None:
            return r1, r2
        if parent_info[0] == parent_info[1] == 0:
            if parent_info[2] == 'up':
                r1 = s1[i - 1] + r1
                r2 = "_" + r2

                return r1, r2

            r1 = "_" + r1
            r2 = s2[j - 1] + r2

            return r1, r2

        res = StringTool.get_string(s1, s2, parent_info[2], i, j)
        r1 = res[0] + r1
        r2 = res[1] + r2

        parent_i = parent_info[0]
        parent_j = parent_info[1]
        parent = M[parent_i][parent_j][1]

        r1, r2 = StringTool.__unpack_alignment(M, parent_i, parent_j, s1, s2, r1, r2)

        return r1, r2

    @staticmethod
    def get_string(s1, s2, s, i, j):
        if s == 'diag':
            return s1[i - 1], s2[j - 1]
        if s == 'up':
            # return s1[i - 1], s2[j]
            return s1[i - 1], "_"
        if s == 'left':
            # return s1[i], s2[j - 1]
            return "_", s2[j - 1]


class StringCreator:
    pass
