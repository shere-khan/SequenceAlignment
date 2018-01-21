import re


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

        self.filter(c, result)

        # tokenize on white space
        # toks = c.split()

        # run tokenization rules rules
        # for t in toks:
        #     t = self.filter1(t, result)
            # t = self.filter2(t, result)
            # t = self.filter3(t, result)
            # t = self.filter4(t, result)
            # t = self.filter5(t, result)
            # t = self.filter6(t, result)

        # f.close()

        return result

    def filter(self, c, result):
        # exp = r"[^\w\s</'](?=\w|\W)"
        exp = r"(?!<[\w])[^\w\s'](?=\w|\W)"
        match = re.findall(exp, c)
        # if match:
        #     rep = match.group() + " "
        #     s = re.sub(exp, rep, s)


    def filter1(self, s, result):
        exp = r'^\W'
        match = re.search(exp, s)
        while match:
            # result.append(match)
            # s = s[2:]
            rep = match.group() + " "
            s = re.sub(exp, rep, s)

        return s

    def filter2(self, s, result):
        exp = r'\W$'
        match = re.search(exp, s)
        while match:
            result.append(match)
            s = s[:-1]
            match = re.search(exp, s)

        return s

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
    im = InputManager('input_6640.txt')
    result = im.tokenize()
    print(result)
