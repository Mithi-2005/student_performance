import sys
from src.logger import logging
def error_message_detail(error,error_detail: sys):
    _,_,exc_tb=error_detail.exc_info() ##Gives actually exc_type (no need),exc_value (no need),exc_traceback(where it ocured)(needed)
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in file [{0}] on line [{1}] with message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message,error_detail: sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
        
    def __str__(self):
        return self.error_message

    