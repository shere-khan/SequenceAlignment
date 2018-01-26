import re, sequence as sq


class InputManager:

    def __init__(self, file):
        self.file = file

    def tokenize(self):
        # open and read file
        f = open(self.file, 'r')
        c = f.read()

        # make all strings lowercase
        c.lower()

        result = list()

        # tokenize on white space
        toks = c.split()

        # run rules on each token
        for t in toks:
            t = self.remove_special_chars_begin_filter(t, result)
            res = self.remove_special_chars_end_filter(t)
            word = res.pop(-1)
            if self.has_apostrophe_s(word):
                self.remove_apostrophe_s_filter(word, result)
            elif self.has_apostrophe_m(word):
                self.remove_apostrophe_m_filter(word, result)
            elif self.has_apostrophe_nt(word):
                self.remove_apostrophe_nt_filter(word, result)
            else:
                result.append(word)

            result.extend(res)

        f.close()

        return result

    def remove_special_chars_begin_filter(self, s, result):
        exp = r'^\W'
        match = re.search(exp, s)
        while match:
            result.append(match.group())
            s = s[1:]
            match = re.search(exp, s)

        return s

    def remove_special_chars_end_filter(self, s):
        exp = r'\W$'
        match = re.search(exp, s)

        result = list()
        while match:
            result.insert(0, match.group())
            s = s[:-1]
            match = re.search(exp, s)

        result.append(s)

        return result

    def remove_apostrophe_s_filter(self, s, result):
        exp = r"'s$"
        match = re.search(exp, s)

        if match:
            s = s[:-2]
            result.append(s)
            result.append(match.group())

        return s

    def remove_apostrophe_m_filter(self, s, result):
        exp = r"'s$"
        match = re.search(exp, s)

        if match:
            s = s[:-2]
            result.append(s)
            result.append(match.group())

        return s

    def remove_apostrophe_nt_filter(self, s, result):
        exp = r"n't$"
        match = re.search(exp, s)

        if match:
            s = s[:-3]
            result.append(s)
            result.append('not')

        return s

    def has_apostrophe_s(self, s):
        exp = r"'s$"
        match = re.search(exp, s)

        return True if match else False

    def has_apostrophe_m(self, s):
        exp = r"'m$"
        match = re.search(exp, s)

        return True if match else False

    def has_apostrophe_nt(self, s):
        exp = r"n't$"
        match = re.search(exp, s)

        return True if match else False

    def changestr(self, s):
        s = 'else'


if __name__ == '__main__':
    source = InputManager('pepper-src.txt')
    src = source.tokenize()
    print(src)

    target = InputManager('pepper-tgt.txt')
    tgt = target.tokenize()
    print(tgt)

    def cost(x, y, type):
        if type == 'indel':
            if x == '' or y == '':
                return -1
        if type == 'match-mismatch':
            if x == y:
                return 2
            if x != y:
                return -1

    align = sq.StringTool.alignment_matrix(src, tgt, cost)

    print()
    sq.StringTool.print_matrix(align)

    r1 = ""
    r2 = ""
    r1, r2 = sq.StringTool.unpack_alignment(align, src, tgt, r1, r2)

    # print('Edit Distance: ' + str(align[-1][-1][0]))
    print('s1: ' + r1)
    print('s2: ' + r2)
    print()