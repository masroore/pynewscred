__author__ = 'Dr. Masroor Ehsan'
__email__ = 'masroore@gmail.com'
__copyright__ = 'Copyright 2013, Dr. Masroor Ehsan'
__license__ = 'BSD'
__version__ = '0.1.1'

try:
    import simplejson as json
except ImportError:
    try:
        import json
    except ImportError:
        try:
            from django.utils import simplejson as json
        except ImportError:
            raise ImportError('A JSON library is required to use this python library!')
from datetime import datetime, date

_datetime_handler = lambda x: x.isoformat() if isinstance(x, (date, datetime)) else None

def jsonify(input, sort_keys=True, indent=4):
    return json.dumps(input, sort_keys=sort_keys, indent=indent, default=_datetime_handler)