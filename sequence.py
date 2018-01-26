import math
import random


class StringTool:
    def __init__(self):
        self.r1 = ""
        self.r2 = ""

    def __eq__(self, other):
        pass

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def dac(self, x, y, f, p):
        m = len(x)
        n = len(y)
        if m <= 2 or n <= 2:
            M = StringTool.alignment(x, y, f)
            self.r1 = self.r1[:-1]
            self.r2 = self.r2[:-1]
            r1, r2 = StringTool.build_alignment_iter(x, y, M, "", "")
            self.r1 += r1
            self.r2 += r2
        else:
            pos = math.ceil(n / 2)
            y1 = y[:pos]
            y2 = y[pos:]
            fs = StringTool.alignment_linear(x, y1, f)
            gs = StringTool.alignment_linear(list(reversed(x)), list(reversed(y2)), f)
            l = list(map(lambda x: sum(x), zip(fs, reversed(gs))))
            k_star = max(l)
            k_star_index = l.index(k_star)
            path = (k_star_index, pos)

            p.append(path)
            self.dac(x[:k_star_index], y[:pos], f, p)
            self.dac(x[k_star_index - 1:], y[pos - 1:], f, p)

    @staticmethod
    def local_alignment_path(x, y, f):
        b1 = StringTool.local_alignment_linear_number(x, y, f)
        bound = b1[0]
        yj = b1[1][1]
        xj = b1[1][0]
        x1 = x[:xj]
        y1 = y[:yj]
        b2 = StringTool.local_alignment_search(list(reversed(x1)), list(reversed(y1)), f, bound)

        xi = len(x1) - b2[1][0]

        yi = len(y1) - b2[1][1]

        xij = x[xi:xj]
        yij = y[yi:yj]

        return xij, yij

    @staticmethod
    def local_alignment_linear_number(x, y, func):
        m = len(x)
        n = len(y)
        prev = [0 for i in range(n + 1)]
        best = (0, (0, 0))
        for i in range(1, m + 1):
            cur = [prev[0]]
            for j in range(1, n + 1):
                a = prev[j - 1] + func(x[i - 1], y[j - 1], 'match-mismatch')
                b = cur[-1] + func("", y[j - 1], 'indel')
                c = prev[j] + func(x[i - 1], '', 'indel')
                v = max(a, b, c, 0)
                cur.append(v)

                if best[0] < v:
                    best = (v, (i, j))

            prev = cur

        return best

    @staticmethod
    def local_alignment_search(x, y, func, bound):
        m = len(x)
        n = len(y)
        prev = [0 for i in range(n + 1)]
        best = (0, (0, 0))
        cur = list()
        fin = False
        for i in range(1, m + 1):
            cur.append(0)
            if fin:
                break
            for j in range(1, n + 1):
                try:
                    a = prev[j - 1] + func(x[i - 1], y[j - 1], 'match-mismatch')
                    b = cur[-1] + func("", y[j - 1], 'indel')
                    c = prev[j] + func(x[i - 1], '', 'indel')
                except IndexError:
                    print()

                v = max(a, b, c, 0)
                cur.append(v)

                if v == bound:
                    best = (v, (i, j))
                    fin = True
                    break

            prev = cur
            cur = list()

        return best

    @staticmethod
    def alignment_linear(x, y, cost):
        m = len(x)
        n = len(y)
        prev = [0]
        for i in range(n):
            prev.append(prev[i] + cost('', '', 'indel'))
        f = list()
        f.append(prev[-1])
        for i in range(1, m + 1):
            cur = [prev[0] + cost('', '', 'indel')]
            for j in range(1, n + 1):
                a = prev[j - 1] + cost(x[i - 1], y[j - 1], 'match-mismatch')
                b = cur[-1] + cost("", y[j - 1], 'indel')
                c = prev[j] + cost(x[i - 1], '', 'indel')
                cur.append(max(a, b, c))

            f.append(cur[-1])
            prev = cur

        return f

    @staticmethod
    def alignment(x, y, f):
        m = len(x)
        n = len(y)
        M = []
        StringTool.populate_base(M, m, n, f)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                a = M[i - 1][j - 1][0] + f(x[i - 1], y[j - 1], 'match-mismatch')
                b = M[i - 1][j][0] + f("", y[j - 1], 'indel')
                c = M[i][j - 1][0] + f(x[i - 1], '', 'indel')

                vals = [a, b, c]
                maxx = max(vals)
                M[i][j] = (maxx, StringTool.get_parent(vals.index(maxx), i, j))

        return M

    @staticmethod
    def populate_base(M, m, n, cost):
        for i in range(0, m + 1):
            for j in range(0, n + 1):
                if i == 0 and j == 0:
                    M.append([(i, None)])
                elif i == 0 and j > 0:
                    val = M[i][j - 1][0] + cost('', '', 'indel')
                    M[i].append((val, (i, j - 1, 'left')))
                elif i > 0 and j == 0:
                    val2 = M[i - 1][0][0] + cost('', '', 'indel')
                    M.append([(val2, (i - 1, j, 'up'))])
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
    def build_alignment_iter(x, y, M, r1, r2):
        i = len(x)
        j = len(y)
        while i > 0 or j > 0:
            parent_info = M[i][j][1]
            r1, r2 = StringTool.build_alignment_string(x, y, parent_info[2], i, j, r1, r2)

            parent_i = parent_info[0]
            parent_j = parent_info[1]

            i = parent_i
            j = parent_j

        return r1, r2

    @staticmethod
    def build_alignment_string(x, y, path, i, j, r1, r2):
        if path == 'diag':
            r1 = x[i - 1] + r1
            r2 = y[j - 1] + r2
        elif path == 'up':
            r1 = x[i - 1] + r1
            r2 = "_" + r2
        elif path == 'left':
            r1 = "_" + r1
            r2 = y[j - 1] + r2
        return r1, r2

    @staticmethod
    def local_alignment_matrix(x, y, f):
        m = len(x)
        n = len(y)
        M = [[0 for i in range(n + 1)]]
        for i in range(1, m + 1):
            M.append([0])
            for j in range(1, n + 1):
                a = M[i - 1][j - 1] + f(x[i - 1], y[j - 1], 'match-mismatch')
                b = M[i - 1][j] + f("", y[j - 1], 'indel')
                c = M[i][j - 1] + f(x[i - 1], '', 'indel')

                M[i].append(max([a, b, c, 0]))

        return M

    @staticmethod
    def populate_base_matrix(M, m, n):
        for i in range(0, m + 1):
            for j in range(0, n + 1):
                if i == 0 and j == 0:
                    M.append([(i, None)])
                elif i == 0 and j > 0:
                    M[i].append((j, (i, j - 1, 'left')))
                elif i > 0 and j == 0:
                    M.append([(i, (i - 1, j, 'up'))])
                else:
                    M[i].append((0, None))

    @staticmethod
    def alignment_matrix(x, y, f):
        m = len(x)
        n = len(y)
        M = list()
        StringTool.populate_base_matrix(M, m, n)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                a = M[i - 1][j - 1][0] + f(x[i - 1], y[j - 1], 'match-mismatch')
                b = M[i - 1][j][0] + f("", y[j - 1], 'indel')
                c = M[i][j - 1][0] + f(x[i - 1], "", 'indel')
                vals = [a, b, c, 0]
                mynn = min(vals)
                M[i][j] = (mynn, StringTool.get_parent(vals.index(mynn), i, j))

        return M

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

    @staticmethod
    def print_matrix(M):
        for row in M:
            for x in row:
                print(x, end=" ")
            print()

    @staticmethod
    def sequence_generator(n, letters):
        return [random.choice(letters) for i in range(n)]
