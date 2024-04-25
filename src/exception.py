import sys


def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info() #exc_info fetch the message from exception class

    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = "Error occurred python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message

#here we inherite the parent class
class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        """
        :param error_message: error message in string format
        """
        super().__init__(error_message) #super called the message from parent class

        self.error_message = error_message_detail(
            error_message, error_detail=error_detail
        )

    def __str__(self): #it print the object indirectly error message
        return self.error_message
