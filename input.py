import re, regex


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

        # self.filter(c, result)

        # tokenize on white space
        toks = c.split()

        # run rules on each token
        for t in toks:
            t = self.remove_special_chars_begin_filter(t, result)
            res = self.remove_special_chars_end_filter(t)
            word = res.pop(-1)
            if self.has_apostrophe_s(word):
                t = self.remove_apostrophe_s_filter(word, result)
            elif self.has_apostrophe_m(word):
                t = self.remove_apostrophe_m_filter(word, result)
            elif self.has_apostrophe_nt(word):
                t = self.remove_apostrophe_nt_filter(word, result)
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
            result.append(match.group())
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

    def filter3(self, s, result):
        exp1 = r"\w*(?=['s])"
        match1 = re.search(exp1, s)
        if match1:
            exp2 = r"(?<=[\S])'s"
            match2 = re.search(exp2, s)
            result.append(match1.group())
            if match2:
                result.append(match2.group())

        else:
            result.append()

    def filter4(self):
        pass

    def changestr(self, s):
        s = 'else'


if __name__ == '__main__':
    # print("something")
    im = InputManager('input_6640.txt')
    result = im.tokenize()
    print(result)
