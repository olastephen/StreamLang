####################
#   SHELL
####################
from Lang.File.File import File
from Lang.Lexer.Lexers import Lexer
from Lang.Parser.Parser import Parser


class Shell:  # Gets texts from a stream file

    def __init__(self):
        self.data = None
        self.toks = None

    def run(self):  # This method gets a stream file from the the console
        self.data = File().open_file(input("Stream > "))
        self.toks = Lexer(self.data).lex()
        Parser().parse(self.toks)
