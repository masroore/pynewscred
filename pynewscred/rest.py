__author__ = 'Dr. Masroor Ehsan'
__email__ = 'masroore@gmail.com'
__copyright__ = 'Copyright 2013, Dr. Masroor Ehsan'
__license__ = 'BSD'
__version__ = '0.1.1'

import httplib
import urllib
from cStringIO import StringIO
import gzip, zlib

class RestClient(object):
    def __init__(self, host, port=80):
        self.host = host
        self.port = port

    def _request(self, method, url, post_params=None, headers=None):
        params = post_params or {}
        headers = headers or {}

        if params:
            body = urllib.urlencode(params)
        else:
            body = None

        if body:
            headers['Content-type'] = 'application/x-www-form-urlencoded'

        conn = httplib.HTTPConnection(self.host, self.port)
        conn.request(method, url, body, headers)
        resp = RestResponse(conn.getresponse())
        conn.close()

        return resp

    def get(self, url, headers=None):
        return self._request('GET', url, headers=headers)

    def post(self, url, params, headers=None):
        return self._request('POST', url, post_params=params, headers=headers)


class RestResponse(object):
    def __init__(self, http_resp):
        self.http_response = http_resp
        self.status = int(http_resp.status)
        self.reason = http_resp.reason
        self.headers = dict(http_resp.getheaders())

        encoding = self.headers.get('content-encoding', '')
        content = http_resp.read()
        if encoding in ('gzip', 'deflate'):
            if encoding == 'deflate':
                data = StringIO(zlib.decompress(content))
            else:
                data = gzip.GzipFile('', 'rb', 9, StringIO(content))
            self.body = data.read()
        else:
            self.body = content