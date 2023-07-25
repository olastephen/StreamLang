####################
#   LEXER
####################
from Lang.Constants.Constant import Constant
from Lang.Tokenizer.Tokenizer import Tokenizer

import  re


class Lexer:

    def __init__(self):
        self.filecontents = "let hello = \"hello world\" \n let nums = 10 + 4 - (1 * 2) \n letout 10 + 4 - (1 * 2) \n " \
                            "letout nums \n letout hello <EOF>".split()
        self.tok = ""
        self.state = 0
        self.var_started = 0
        self.var = ""
        self.string = ""
        self.tokens = Tokenizer().tokens
        self.numbers = Constant().numbers
        self.brackets = Constant().brackets
        self.last_token = ""
        self.expr = ""
        self.isExpr = 0
        self.num = ""
        self.bOperator = Constant().bOperator
        self.EOF = Constant().EOF
        self.onString = 0

    def lex(self):
        for word in self.filecontents:
            if word == "letout":
                if self.onString == 1:
                    self.string += word
                else:
                    self.tokens.append("LETOUT")
            elif word == "\"":
                if self.onString == 1:
                    self.onString = 0
                else:
                    self.onString = 1
            elif word == "let":
                if self.onString == 1:
                    self.string += word
                else:
                    self.tokens.append("LET")
            elif word == "\n":
                print("nl")

        #return self.tokens
        print(self.filecontents)
        print(self.tokens)
        return ''


Lexer().lex()
