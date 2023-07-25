#####################
#   ERROR
#####################

class Error:

    def __init__(self, pos_start, pos_end, error_name, details):
        """
        :param pos_start:
        :param pos_end:
        :param error_name: the name of the error made
        :param details: the details of the error
        """
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.error_name = error_name
        self.details = details

    def as_string(self):
        result = f'{self.error_name}: {self.details} \n'
        result += f'\tFile {self.pos_start.fn}, line {self.pos_start.ln + 1}'
        return result
