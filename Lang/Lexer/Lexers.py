####################
#   LEXER
####################
from Lang.Constants.Constant import Constant
from Lang.Tokenizer.Tokenizer import Tokenizer


class Lexer:

    def __init__(self, filecontents):
        self.filecontents = list(filecontents)
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

    def lex(self):
        for char in self.filecontents:
            self.tok += char
            if self.tok == " ":
                if self.state == 0:
                    self.tok = ""
                else:
                    self.tok = " "
            elif self.tok == "\n" or self.tok == self.EOF:
                if self.expr != "" and self.isExpr == 1:
                    self.tokens.append("EXPR:" + self.expr)
                    self.expr = ""
                elif self.expr != "" and self.isExpr == 0:
                    self.tokens.append("NUM:" + self.expr)
                    self.expr = ""
                elif self.var != "" and self.var_started == 1:
                    self.tokens.append("VAR:" + self.var)
                    self.var = ""
                    self.var_started = 0
                self.tok = ""
            elif self.tok == Constant().aOperator:
                if self.var != "" and self.var_started == 1:
                    self.tokens.append("VAR:" + self.var)
                    self.var = ""
                    self.var_started = 0
                self.tokens.append("EQUALS")
                self.tok = ""
                self.last_token = "equals"
            elif self.tok == "let":
                self.last_token = "let"
                self.tok = ""
            elif self.last_token == "let":
                self.var_started = 1
                self.var += self.tok
                self.tok = ""
            elif self.tok == "letout":
                self.tokens.append("LETOUT")
                self.tok = ""
            elif self.tok in self.numbers:
                self.expr += self.tok
                self.tok = ""
            elif self.tok in self.bOperator or self.tok in self.brackets:
                self.isExpr = 1
                self.expr += self.tok
                self.tok = ""
            elif self.tok == "\"":
                if self.state == 0:
                    self.state = 1
                elif self.state == 1:
                    self.tokens.append("STRING:" + self.string + "\"")
                    self.string = ""
                    self.state = 0
                    self.tok = ""
            elif self.state == 1:
                self.string += self.tok
                self.tok = ""
        #return self.tokens
        print(self.tokens)
        return ''
