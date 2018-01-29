import re, sequence as sq, search, sys


class InputManager:

    def __init__(self, file):
        self.file = file

    def tokenize(self):
        # open and read file
        f = open(self.file, 'r')
        c = f.read()

        # make all strings lowercase
        c = c.lower()

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
        # exp = r'^\W'
        exp = r'^\W(?=[\W]*[\w])'
        match = re.search(exp, s)
        while match:
            result.append(match.group())
            s = s[1:]
            match = re.search(exp, s)

        return s

    def remove_special_chars_end_filter(self, s):
        # exp = r'\W$'
        exp = r'(?<=[\w])[\W]+$'
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

    @staticmethod
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

    @staticmethod
    def print_matrix_info(toks):
        print('          ', end='')
        for i in range(len(toks) + 1):
            print(str(i).center(5), end='')

        print()
        print('          ', end='')

        for i in range(len(toks) + 1):
            sub = toks[i - 1][:3]
            if i == 0:
                print('#'.center(5), end='')
            else:
                print(sub.center(5), end='')
            sys.stdout.flush()

    @staticmethod
    def print_matrix_format(M, src_toks, tgt_toks):
        InputManager.print_matrix_info(tgt_toks)
        print()

        for i, row in enumerate(M):
            print(str(i).center(5), end='')
            if i == 0:
                print('#'.center(5), end='')
            else:
                print(src_toks[i - 1][:3].center(5), end='')
            sys.stdout.flush()
            for j, cell in enumerate(row):
                print(str(cell[0]).center(5), end='')
                sys.stdout.flush()
            print()

    @staticmethod
    def print_backtrace_format(M, src_toks, tgt_toks):
        # print column headers first
        InputManager.print_matrix_info(tgt_toks)
        print()

        # print remaining table starting with row headers at
        # the beginning of each row
        for i, row in enumerate(M):
            print(str(i).center(5), end='')
            if i == 0:
                print('#'.center(5), end='')
            else:
                print(src_toks[i - 1][:3].center(5), end='')
            sys.stdout.flush()
            for j, cell in enumerate(row):
                # Don't print ptr's for margins/base cases
                # or if ptr doesn't exist (None)
                if cell[1] is None or i == 0 or j == 0:
                    print(' '.center(5), end='')

                else:
                    ptr = cell[1][2]
                    val = ''
                    if ptr == 'up':
                        val = 'UP'
                    elif ptr == 'left':
                        val = 'LT'
                    elif ptr == 'diag':
                        val = 'DI'

                    print(str(val).center(5), end='')

                sys.stdout.flush()
            print()


if __name__ == '__main__':
    print('University of Central Florida')
    print('CAP6640 String 2018 - Dr. Glinos')
    print()
    print('Text Similarity Analysis by Justin Barry')

    file_name_prefs = ['shake']
    # file_name_prefs = ['pepper', 'gene', 'shake']
    # file_name_prefs = ['pepper']
    # file_name_prefs = ['input_6640']

    for fn in file_name_prefs:
        src_name = '{0}-src.txt'.format(fn)
        tgt_name = '{0}-tgt.txt'.format(fn)

        print('Source File: {0}'.format(src_name))
        print('Target File: {0}'.format(tgt_name), end='\n\n')
        print('Raw Tokens')

        source = InputManager(src_name)
        target = InputManager(tgt_name)

        # print raw tokens
        src_raw_tokens = source.raw_tokens()
        print('\tSource > {0}'.format(src_raw_tokens), end='')
        tgt_raw_tokens = target.raw_tokens()
        print('\tTarget > {0}'.format(tgt_raw_tokens), end='\n\n')

        # Print normalized tokens with rules applied
        print('Normalized Tokens:')
        src_normalized = source.tokenize()
        print('\tSource > {0}'.format(" ".join(src_normalized)))
        tgt_normalized = target.tokenize()
        print('\tTarget > {0}'.format(" ".join(tgt_normalized)), end='\n\n')

        # Get alignment
        M, max_score = sq.StringTool.local_alignment_matrix(src_normalized, tgt_normalized, InputManager.cost)

        # print formatted edit distance table showing numbers
        print('Edit Distance Table:')
        InputManager.print_matrix_format(M, src_normalized, tgt_normalized)
        print()

        # print formatted edit distance table showing numbers
        print('Backtrace Table:')
        InputManager.print_backtrace_format(M, src_normalized, tgt_normalized)
        print()

        # -------------------------------- Print Alignment Report ------------------------------------------
        print('Maximum value in distance table: {0}'.format(max_score), end='\n\n')

        # find max alignment locations in alignment matrix
        locs = search.Search.search_matrix(M, max_score)
        print('Maxima:')
        for loc in locs:
            print('\t[ {0}, {1} ]'.format(loc[0], loc[1]))

        print('\nMaximal-similarity alignments:', end='\n\n')

        for i, l in enumerate(locs):
            r1 = ""
            r2 = ""
            r1, r2 = sq.StringTool.unpack_alignment(M, l[0], l[1], src_normalized, tgt_normalized, r1, r2,
                                                    max_score)

            print('\tAlignment {0} (length {1}):'.format(i, len(r1.split())))
            print('\t\tSource at: ' + r1)
            print('\t\tTarget at: ' + r2)
            print('\t\tEdit action:')
            print()
