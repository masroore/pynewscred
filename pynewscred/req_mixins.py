__author__ = 'Dr. Masroor Ehsan'
__email__ = 'masroore@gmail.com'
__copyright__ = 'Copyright 2013, Dr. Masroor Ehsan'
__license__ = 'BSD'
__version__ = '0.1.1'

from datetime import datetime

class _RequestProcessorMixin1(object):
    def from_date(self, value, with_time=False):
        """Beginning of date range for which items are searched. Format: yyyy-mm-dd [hh:mm:ss]"""
        self._uri_params['from_date'] = datetime.strftime(value, '%Y-%m-%d %H:%M:%S' if with_time else '%Y-%m-%d')
        return self

    def to_date(self, value, with_time=False):
        """End of date range for which items are searched. Format: yyyy-mm-dd [hh:mm:ss]"""
        self._uri_params['to_date'] = datetime.strftime(value, '%Y-%m-%d %H:%M:%S' if with_time else '%Y-%m-%d')
        return self

    def pagesize(self, value):
        """Number of items to return."""
        self._uri_params['pagesize'] = int(value)
        return self

    def offset(self, value):
        """Number of items to skip before beginning the result set.
        For example, a pagesize of 10 and an offset of 10 will return items 11-20."""
        self._uri_params['offset'] = int(value)
        return self

    def topics(self, value):
        """Value is a space delimited list of topic guids. Articles returned must contain at least one of the topics provided."""
        self._uri_params['topics'] = value
        return self

    def topic_filter_mode(self, value):
        """enables topic_filter_name and indicates filtering type. allowed values are whitelist or blacklist"""
        self._uri_params['topic_filter_mode'] = value
        return self

    def topic_filter_name(self, value):
        """Limit items to a predefined list of topics.
        Value is the name of the predefined topic filter list (applicable only when topic filtering is enabled via topic_filter_mode)"""
        self._uri_params['topic_filter_name'] = value
        return self


class _RequestProcessorMixin2(object):
    def fulltext(self, value):
        """Search exclusively for fully licensed, full text content.
        Not available without a contract. Valid values are "True" or "False"."""
        self._uri_params['fulltext'] = 'True' if bool(value) else 'False'
        return self

    def has_images(self, value):
        """Return only articles that have associated images (accessible via article/GUID/images).
        Valid values are "True" or "False"."""
        self._uri_params['has_images'] = 'True' if bool(value) else 'False'
        return self

    def get_topics(self, value):
        """Set to true to include associated topics inline with each article.
        For faster response times, we recommend setting this to false unless topics are explicitly being used"""
        self._uri_params['get_topics'] = 'True' if bool(value) else 'False'
        return self

    def sort(self, value):
        """Sort order for returned items. Valid values are date and relevance."""
        self._uri_params['sort'] = value
        return self

    def media_types(self, value):
        """Limit the media type of the returned items. Value is a space delimited list of media types.
        See Source module for a list of valid media types."""
        self._uri_params['media_types'] = value
        return self

    def source_countries(self, value):
        """Search against only sources from the specified countries.
        Value is a space delimited list of 2 character ISO 3166-1 country codes."""
        self._uri_params['source_countries'] = value
        return self

    def sources(self, value):
        """Limit items to the sources specified.
        Value is a space delimited list of source guids."""
        self._uri_params['sources'] = value
        return self

    def source_filter_mode(self, value):
        """Enables source_filter_name and indicates filtering type.
        Allowed values are whitelist or blacklist"""
        self._uri_params['source_filter_mode'] = value
        return self

    def source_filter_name(self, value):
        """Limit items to a predefined list of sources.
        Value is the name of the predefined source filter list (applicable only when source filtering is enabled via source_filter_mode)"""
        self._uri_params['source_filter_name'] = value
        return self

    def languages(self, value):
        """Limit items to those in the specified language. Value is a 2 letter ISO language code."""
        self._uri_params['languages'] = value
        return self

    def article_filter_mode(self, value):
        """Enables article_filter_name and indicates filtering type. Allowed values are whitelist or blacklist"""
        self._uri_params['article_filter_mode'] = value
        return self

    def article_filter_name(self, value):
        """Limit items to a predefined list of articles.
        Value is the name of the predefined article filter list (applicable only when article filtering is enabled via article_filter_mode)"""
        self._uri_params['article_filter_name'] = value
        return self


class _RequestProcessorMixin3(object):
    def query(self, value):
        """Specifies the set of words and phrases to search for.
        Query string syntax supports searching for phrases, required terms (whitelisted), and forbidden terms (blacklisted).
        For example to search for articles that MUST contain the phrase "Barack Obama", CANNOT include the word "china",
        and contain any one of the words "USA" and "president", issue the following query:
        query=+"barack obama" -china USA president
        The non white/blacklisted terms will be handled according to the values of the mm and boolean_operator parameters as described below.
        Leaving this parameter blank will result in matching all articles in the system.        """
        self._uri_params['query'] = value
        return self

    def query_fields(self, value):
        """Specifies which field to search when searching for articles.
        Allowed values 'title' and 'description'
        """
        self._uri_params['query_fields'] = value
        return self

    def boolean_operator(self, value):
        """Indicates the boolean operation to use on search keywords that do not have explicit whitelist (+) or blacklist (-) operators on them.
        The value can either be and or or."""
        self._uri_params['boolean_operator'] = value
        return self

    def mm(self, value):
        """"Minimum Match": specifies how many of the non whitelist/blacklist keywords must match for an article to be included in the results.
        Can be an integer (e.g., "1") or a percentage (e.g., "50%"). The default value requires that all words match."""
        self._uri_params['mm'] = value
        return self

    def categories(self, value):
        """Limit items to the categories specified. Value is a space delimited list of dashed category names.
        See Category module for more information."""
        self._uri_params['categories'] = value
        return self

    def modified_since(self, value, with_time=False):
        """Get only articles that have been modified since the supplied date.
        A modification can be the initial creation and/or an update to the article.
        Format: yyyy-mm-dd [hh:mm:ss]"""
        self._uri_params['modified_since'] = datetime.strftime(value, '%Y-%m-%d %H:%M:%S' if with_time else '%Y-%m-%d')
        return self

    def exact(self, value):
        """If this parameter is not specified, then stemming is applied, so that for example the query term "ship"
        matches articles containing "shipping", and vice versa. Specifying exact=true turns stemming off."""
        self._uri_params['exact'] = value
        return self

    def min_length(self, value):
        """Returns only articles with at least this many words. For example, min_length=100"""
        self._uri_params['min_length'] = int(value)
        return self

    def max_length(self, value):
        """Returns only articles with at most this many words. For example, max_length=200"""
        self._uri_params['max_length'] = int(value)