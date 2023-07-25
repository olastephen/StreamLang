####################
#   PARSER
####################
from Lang.Extra.Do import Do


class Parser:

    def __init__(self):
        self.i = 0

    def parse(self, toks):

        while self.i < len(toks):
            if toks[self.i] + " " + toks[self.i + 1][0:6] == "LETOUT STRING" or \
                    toks[self.i] + " " + toks[self.i + 1][0:3] == "LETOUT NUM" or \
                    toks[self.i] + " " + toks[self.i + 1][0:4] == "LETOUT EXPR" or \
                    toks[self.i] + " " + toks[self.i + 1][0:4] == "LETOUT VAR":
                if toks[self.i + 1][0:6] == "STRING":
                    Do().letout(toks[self.i + 1])
                elif toks[self.i + 1][0:3] == "NUM":
                    Do().letout(toks[self.i + 1])
                elif toks[self.i + 1][0:4] == "EXPR":
                    Do().letout(toks[self.i + 1])
                self.i += 2
            if toks[self.i][0:3] + " " + toks[self.i + 1] + " " + toks[self.i + 2][0:6] == "VAR EQUALS STRING" or \
                    toks[self.i][0:3] + " " + toks[self.i + 1] + " " + toks[self.i + 2][0:3] == "VAR EQUALS NUM" or \
                    toks[self.i][0:3] + " " + toks[self.i + 1] + " " + toks[self.i + 2][0:4] == "VAR EQUALS EXPR" or \
                    toks[self.i][0:3] + " " + toks[self.i + 1] + " " + toks[self.i + 2][0:3] == "VAR EQUALS VAR":
                if toks[self.i + 2][0:6] == "STRING":
                    Do().assign(toks[self.i], toks[self.i + 2])
                elif toks[self.i + 2][0:3] == "NUM":
                    Do().assign(toks[self.i], toks[self.i + 2])
                elif toks[self.i + 2][0:4] == "EXPR":
                    Do().assign(toks[self.i], "NUM:" + str(Do().eval(toks[self.i + 2][5:])))
                elif toks[self.i + 2][0:4] == "VAR":
                    Do().assign(toks[self.i], Do().var(toks[self.i + 2]))
                self.i += 3
