from Lang.Shell.Shell import Shell


####################
#   MAIN
####################

class Main:

    def __init__(self):
        self.shell = Shell
        self.shell().run()


if __name__ == '__main__':
    Main()

