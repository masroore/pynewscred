__author__ = 'Dr. Masroor Ehsan'
__email__ = 'masroore@gmail.com'
__copyright__ = 'Copyright 2013, Dr. Masroor Ehsan'
__license__ = 'BSD'
__version__ = '0.1.1'

from abc import ABCMeta, abstractmethod
from urllib import urlencode
from req_parser import parse_single_article, parse_article_set, parse_story_set, parse_category_set
from rest import RestClient
from exceptions import APIError
import platform
from .import VERSION

USER_AGENT = "PyNewsCred/%s (%s %s)" % (VERSION, platform.system(), platform.release())

class _FluentRequestProcessorBase():
    __metaclass__ = ABCMeta
    _FQDN = 'api.newscred.com'
    _parser_map = {
        'single_article': parse_single_article,
        'article_set': parse_article_set,
        'story_set': parse_story_set,
        'category_set': parse_category_set
    }

    def __init__(self, access_key):
        self._access_key = access_key
        self._uri_params = {}
        self._parser = None
        self.rest_response = None

    @abstractmethod
    def _get_uri_path(self):
        pass

    def build_url(self):
        base_uri = '/{0}?access_key={1}'.format(self._get_uri_path(), self._access_key)
        params = urlencode(self._uri_params) if self._uri_params else None
        return '{0}&{1}'.format(base_uri, params) if params else base_uri

    def build_full_url(self):
        base_uri = 'http://{0}/{1}?access_key={2}'.format(self._FQDN, self._get_uri_path(), self._access_key)
        params = urlencode(self._uri_params) if self._uri_params else None
        return '{0}&{1}'.format(base_uri, params) if params else base_uri

    def _parse_response(self):
        if self._parser and self._parser_map.has_key(self._parser):
            return self._parser_map[self._parser](self.rest_response.body)
        return None

    def perform(self):
        uri = self.build_url()
        headers = {
            'Connection': 'close',
            'Cache-Control': 'max-age=0',
            'User-Agent': USER_AGENT,
            'Accept': 'application/xml',
            'Accept-Encoding': 'gzip,deflate',
            'Accept-Charset': 'UTF-8,*;q=0.5'
        }

        rest_client = RestClient(self._FQDN)
        self.rest_response = rest_client.get(uri, headers=headers)

        if self.rest_response.status != 200:
            raise APIError(
                self.rest_response.status,
                self.rest_response.reason,
                self.rest_response)

        if self.rest_response.body == None or len(self.rest_response.body) == 0:
            raise APIError(
                -1,
                'Unexpected response from the server.',
                self.rest_response)

        return self._parse_response()


class _ArticleRequestProcessorBase(_FluentRequestProcessorBase):
    _uri_path = None

    def __init__(self, access_key, article_guid):
        super(_ArticleRequestProcessorBase, self).__init__(access_key)
        self._article_guid = article_guid

    def _get_uri_path(self):
        return self._uri_path % self._article_guid