import sys

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    error_message_detail = "Error occurred in python script name [{0}] in line number [{1}] error message: {2}".format(
    exc_tb.tb_frame.f_code.co_filename,
    exc_tb.tb_frame.f_lineno,
    str(error)
    
)
    return error_message_detail
    
class CusException(Exception):
    def __init__(self, error_message, error_details):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_details)
    
    def __str__(self):
        return self.error_message


# if __name__ == '__main__':
#     try:
#         a = 10/ 0
#     except Exception as e:
#         raise CusException(e, sys)