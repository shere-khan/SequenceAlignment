import re, sequence as sq, search


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

    def raw_tokens(self):
        f = open(self.file, 'r')
        c = f.read()
        f.close()

        return c


if __name__ == '__main__':
    print('University of Central Florida')
    print('CAP6640 String 2018 - Dr. Glinos')
    print()
    print('Text Similarity Analysis by Justin Barry')

    file_name_prefs = ['pepper', 'gene', 'shake']

    for fn in file_name_prefs:
        src_name = '{0}-src.txt'.format(fn)
        tgt_name = '{0}-tgt.txt'.format(fn)

        print('Source File: {0}'.format(src_name))
        print('Target File: {0}'.format(tgt_name), end='\n\n')
        print('Raw Tokens')

        source = InputManager(src_name)

        rt = source.raw_tokens()
        print('Source > {0}'.format(rt))

        # source = InputManager('gene-src.txt')
        src = source.tokenize()
        print('Target > {0}'.format(" ".join(src)))

        target = InputManager(tgt_name)
        # target = InputManager('gene-tgt.txt')
        tgt = target.tokenize()
        print(tgt)


        def cost(x, y, type):
            if type == 'ins':
                if x == '' or y == '':
                    return -1
            if type == 'del':
                if x == '' or y == '':
                    return -1
            if type == 'match-mismatch':
                if x == y:
                    return 2
                if x != y:
                    return -1


        align, max_score = sq.StringTool.local_alignment_matrix(src, tgt, cost)

        locs = search.Search.search_matrix(align, max_score)

        # align2 = sq.StringTool.local_alignment_matrix_values_only(src, tgt, cost)

        # for l in align2:
        #     for i in l:
        #         print(i, end=", ")
        #     print()

        print()
        sq.StringTool.print_matrix_pointers(align)
        print()
        sq.StringTool.print_matrix_nums(align)

        for i in locs:
            r1 = ""
            r2 = ""
            r1, r2 = sq.StringTool.unpack_alignment(align, i[0], i[1], src, tgt, r1, r2, max_score)

            print('Edit Distance: ' + str(align[-1][-1][0]))
            print('s1: ' + r1)
            print('s2: ' + r2)
            print()
