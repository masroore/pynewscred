__author__ = 'Dr. Masroor Ehsan'
__email__ = 'masroore@gmail.com'
__copyright__ = 'Copyright 2013, Dr. Masroor Ehsan'
__license__ = 'BSD'
__version__ = '0.1.1'

from req_mixins import _RequestProcessorMixin1, _RequestProcessorMixin2, _RequestProcessorMixin3
from req_builder import _FluentRequestProcessorBase, _ArticleRequestProcessorBase

__all__ = ['ArticleRequest',
           'ArticleImagesRequest',
           'ArticleTopicsRequest',
           'RelatedArticlesRequest',
           'SearchArticlesRequest',
           'SearchStoriesRequest']

class ArticleRequest(_ArticleRequestProcessorBase):
    def __init__(self, access_key, article_guid):
        super(ArticleRequest, self).__init__(access_key, article_guid)
        self._uri_path = 'article/%s'
        self._parser = 'single_article'

    def get_topics(self, value):
        """Return topic associations with each article.
        For better performance, we recommend setting this to false unless topics are explicitly being used."""
        self._uri_params['get_topics'] = 'True' if bool(value) else 'False'
        return self


class ArticleImagesRequest(_ArticleRequestProcessorBase):
    def __init__(self, access_key, article_guid):
        super(ArticleImagesRequest, self).__init__(access_key, article_guid)
        self._uri_path = 'article/%s/images'

    def safe_search(self, value):
        """Returns only images marked as 'safe' when set to true."""
        self._uri_params['safe_search'] = 'True' if bool(value) else 'False'
        return self

    def approved(self, value):
        """When set to true, returns only images manually marked as relevant by our content editors.
        Reduces search set size but improves relevancy."""
        self._uri_params['approved'] = 'True' if bool(value) else 'False'
        return self


class CategoriesRequest(_FluentRequestProcessorBase):
    def __init__(self, access_key):
        super(CategoriesRequest, self).__init__(access_key)
        self._uri_path = 'categories'
        self._parser = 'category_set'

    def query(self, value):
        """The query string to find categories matching."""
        self._uri_params['query'] = value
        return self

    def autosuggest(self, value):
        """If true, partial matches will be returned, i.e. the query 'pol' will match the category 'politics'.
        This is intended for use in autosuggest dropdowns."""
        self._uri_params['autosuggest'] = 'True' if bool(value) else 'False'
        return self


class CategoryArticlesRequest(_FluentRequestProcessorBase, _RequestProcessorMixin1, _RequestProcessorMixin2):
    def __init__(self, access_key, category_dashed_name):
        super(CategoryArticlesRequest, self).__init__(access_key)
        self._dashed_name = category_dashed_name
        self._uri_path = 'category/{0}/articles'.format(self._dashed_name)
        self._parser = 'article_set'

        # remove redundant methods from _UriBuilderMixin1
        del self.topics
        del self.topic_filter_mode
        del self.topic_filter_name


class ArticleTopicsRequest(_ArticleRequestProcessorBase, _RequestProcessorMixin1):
    def __init__(self, access_key, article_guid):
        super(ArticleTopicsRequest, self).__init__(access_key, article_guid)
        self._uri_path = 'article/%s/topics'

    def topic_subclassifications(self, value):
        """Limit items to the topic sub-classifications.
        Value is a space delimited list of topic sub-classifications"""
        self._uri_params['topic_subclassifications'] = value
        return self

    def topic_classifications(self, value):
        """Limit items to the topic classifications.
        Value is a space delimited list of topic classifications"""
        self._uri_params['topic_classifications'] = value
        return self


class RelatedArticlesRequest(_ArticleRequestProcessorBase, _RequestProcessorMixin1, _RequestProcessorMixin2):
    def __init__(self, access_key, article_guid):
        super(RelatedArticlesRequest, self).__init__(access_key, article_guid)
        self._uri_path = 'article/%s/articles'

    def categories(self, value):
        """Limit items to the categories specified. Value is a space delimited list of dashed category names.
        See Category module for more information"""
        self._uri_params['categories'] = value
        return self


class SearchArticlesRequest(_FluentRequestProcessorBase, _RequestProcessorMixin1, _RequestProcessorMixin2, _RequestProcessorMixin3):
    def __init__(self, access_key):
        super(SearchArticlesRequest, self).__init__(access_key)
        self._parser = 'article_set'

    def _get_uri_path(self):
        return 'articles'


class SearchStoriesRequest(_FluentRequestProcessorBase, _RequestProcessorMixin1, _RequestProcessorMixin2, _RequestProcessorMixin3):
    def __init__(self, access_key):
        super(SearchStoriesRequest, self).__init__(access_key)
        self._parser = 'story_set'

    def _get_uri_path(self):
        return 'stories'

    def cluster_size(self, value):
        """Number of articles returned for each story"""
        self._uri_params['cluster_size'] = int(value)
        return self