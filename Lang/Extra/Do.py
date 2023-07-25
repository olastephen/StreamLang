from Lang.Constants.Constant import Constant
from Lang.Tokenizer.Tokenizer import Tokenizer


class Do:

    def __init__(self):
        self.tokenizer = Tokenizer()

    @staticmethod
    def eval(expr):
        return eval(expr)

    def letout(self, to_letout):
        if to_letout[0:6] == "STRING":
            to_letout = to_letout[8:]
            to_letout = to_letout[:-1]
        elif to_letout[0:3] == "NUM":
            to_letout = to_letout[4:]
        elif to_letout[0:4] == "EXPR":
            to_letout = self.eval(to_letout[5:])
        print(to_letout)

    def assign(self, name, value):
        self.tokenizer.symbols[name[4:]] = value

    def var(self, var):
        return self.tokenizer.symbols[var[4:]]
