#####################
#   ERROR HANDLER
#####################
from Lang.ErrorHandler.Error import Error


##############################
#   ILLEGAL CHARACTER ERROR
##############################

class IllegalCharError(Error):
    """
    Sub class of the Error class
    """

    def __init__(self, pos_start, pos_end, details):
        """

        :param details: error details
        """
        super().__init__(pos_start, pos_end, 'Illegal Character', details)
