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

        # tokenize on white space
        toks = c.split()

        for t in toks:
            # run tokenization rules rules
            exp1 = r"(?<=[\S])'s(?=[\s|<\s>])"
            # exp2 = r"\w*(?='s)"
            matches = re.findall(exp1, )


        f.close()

        return toks

    def filter1(self, exp, s, l):
        matches = re.findall(exp, s)
        if matches:
            l.append(matches[0])
            l.append(str.format("'{0}", matches[1]))


    def filter2(self):
        pass

    def filter3(self):
        pass

    def filter4(self):
        pass


if __name__ == '__main__':
    im = InputManager('input_6640.txt')
    tok = im.tokenize()
    # for t in tok:
    #     print(t)

