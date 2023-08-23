# Custom exception handling for python documentation
# https://docs.python.org/3/library/sys.html  --> sys.exc_info()
# Exception handling - https://docs.python.org/3/tutorial/errors.html

import sys
from src.logger import logging

def error_message_detail(error, error_detail:sys):   # We can get error detail from sys module
    _,_,exc_tb = error_detail.exc_info()  # This returns 3 variables, we need the 3rd one - error traceback
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in Python script name [{0}], line number [{1}], error_message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):    # Inherits parent Exception class
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)  # Inherits from super class Exception
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):     # When we print it, we get the error message
        return self.error_message

#if __name__=="__main__":
#    try:
#        a=1/0
#    except Exception as e:
#        logging.info("Divide by Zero")
#        raise CustomException(e,sys)