import sys

def error_message_detail(error, error_detail: sys):
    file_name, line_number, _ = error_detail.exc_info()[2].tb_frame.f_code.co_filename, error_detail.exc_info()[2].tb_lineno, str(error)
    return f"Error occurred in Python script name [{file_name}] line number [{line_number}] error message [{error}]"

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
    
    def __str__(self):
        return self.error_message




