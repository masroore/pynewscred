__author__ = 'Dr. Masroor Ehsan'
__email__ = 'masroore@gmail.com'
__copyright__ = 'Copyright 2013, Dr. Masroor Ehsan'
__license__ = 'BSD'
__version__ = '0.1.1'

class APIError(Exception):
    def __init__(self, code, message, rest_response=None):
        super(APIError, self).__init__()
        self.errorCode = code
        self.errorMessage = message
        self.rest_response = rest_response

    def __str__(self):
        return 'PyNewsCred API error: %d: %s' % (self.errorCode,
                                                 self.errorMessage)