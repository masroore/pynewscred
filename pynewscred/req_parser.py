__author__ = 'Dr. Masroor Ehsan'
__email__ = 'masroore@gmail.com'
__copyright__ = 'Copyright 2013, Dr. Masroor Ehsan'
__license__ = 'BSD'
__version__ = '0.1.1'

from datetime import datetime

try:
    from lxml import etree
except ImportError:
    try:
        # Python 2.5
        import xml.etree.cElementTree as etree
    except ImportError:
        try:
            # Python 2.5
            import xml.etree.ElementTree as etree
        except ImportError:
            try:
                # normal cElementTree install
                import cElementTree as etree
            except ImportError:
                # normal ElementTree install
                import elementtree.ElementTree as etree

__all__ = ['parse_single_article', 'parse_story_set', 'parse_article_set']


def _find_and_set(key, rootNode, dict_obj, cb=None):
    node = rootNode.find(key)
    if node is not None:
        dict_obj[key] = cb(node.text) if cb is not None else node.text


def _parse_datetime(input):
    return datetime.strptime(input, "%Y-%m-%d %H:%M:%S")


def _parse_category_set(rootNode, tagName='category'):
    categories = []
    categoriesNode = rootNode.find('categories_set')
    for categoryNode in categoriesNode.findall(tagName):
        category = {}
        _find_and_set('name', categoryNode, category)
        _find_and_set('dashed_name', categoryNode, category)
        if len(category) > 0:
            categories.append(category)
    return categories


def parse_category_set(content):
    rootNode = etree.fromstring(content)
    return _parse_category_set(rootNode)


def parse_single_article(content):
    rootNode = etree.fromstring(content)
    return _parse_single_article(rootNode)


def _parse_single_topic(rootNode):
    topic = {}
    _find_and_set('name', rootNode, topic)
    _find_and_set('topic_group', rootNode, topic)
    _find_and_set('topic_subclassification', rootNode, topic)
    _find_and_set('score', rootNode, topic, float)
    _find_and_set('image_url', rootNode, topic)
    _find_and_set('link', rootNode, topic)
    _find_and_set('guid', rootNode, topic)
    _find_and_set('topic_classification', rootNode, topic)
    _find_and_set('description', rootNode, topic)
    return topic if len(topic) > 0 else None


def _parse_topic_set(rootNode):
    topicSetNode = rootNode.find('topic_set')
    topic_set = []
    if topicSetNode is not None:
        for node in topicSetNode.findall('topic'):
            topic = _parse_single_topic(node)
            if topic is not None:
                topic_set.append(topic)
    return topic_set if len(topic_set) > 0 else None


def _parse_thumbnail(rootNode, dict_obj):
    thumbNode = rootNode.find('thumbnail')
    if thumbNode is not None:
        thumb = {}
        _find_and_set('original_image', thumbNode, thumb)
        _find_and_set('link', thumbNode, thumb)
        if len(thumb) > 0:
            dict_obj['thumbnail'] = thumb


def _parse_single_article(rootNode):
    article = {}

    _find_and_set('description', rootNode, article)
    _find_and_set('title', rootNode, article)
    _find_and_set('created_at', rootNode, article, _parse_datetime)
    _find_and_set('published_at', rootNode, article, _parse_datetime)
    _find_and_set('score', rootNode, article, float)
    _find_and_set('link', rootNode, article)
    _find_and_set('guid', rootNode, article)

    catNode = rootNode.find('category')
    article['category'] = {
        'name': catNode.find('name').text,
        'dashed_name': catNode.find('dashed_name').text}

    authorSetNode = rootNode.find('author_set')
    if authorSetNode is not None:
        article['author_set'] = []
        for authorNode in authorSetNode.findall('author'):
            author = {
                'guid': authorNode.find('guid').text,
                'first_name': authorNode.find('first_name').text,
                'last_name': authorNode.find('last_name').text,
            }
            article['author_set'].append(author)

    topic_set = _parse_topic_set(rootNode)
    if topic_set:
        article['topic_set'] = topic_set

    srcNode = rootNode.find('source')
    source_dict = {}
    _find_and_set('website', srcNode, source_dict)
    _find_and_set('name', srcNode, source_dict)
    _find_and_set('circulation', srcNode, source_dict, int)
    _find_and_set('country', srcNode, source_dict)
    _find_and_set('company_type', srcNode, source_dict)
    _find_and_set('founded', srcNode, source_dict)
    _find_and_set('staff_authors', srcNode, source_dict, int)
    _find_and_set('frequency', srcNode, source_dict)
    _find_and_set('owner', srcNode, source_dict)
    _find_and_set('guid', srcNode, source_dict)
    _find_and_set('is_blog', srcNode, source_dict, bool)
    _find_and_set('thumbnail', srcNode, source_dict)
    _find_and_set('description', srcNode, source_dict)

    mediaNode = srcNode.find('media_type')
    media_dict = {}
    _find_and_set('name', mediaNode, media_dict)
    _find_and_set('dashed_name', mediaNode, media_dict)

    if len(media_dict) > 0:
        source_dict['media_type'] = media_dict

    if len(source_dict) > 0:
        article['source'] = source_dict

    return article


def _parse_author_set(rootNode):
    authorSetNode = rootNode.find('author_set')
    authors = []
    if authorSetNode is not None:
        for node in authorSetNode.findall('author'):
            author = {}
            _find_and_set('guid', node, author)
            _find_and_set('name', node, author)
            if len(author) > 0:
                authors.append(author)

    return authors if len(authors) > 0 else None


def _parse_story_set_article(rootNode):
    article = {}
    _find_and_set('description', rootNode, article)
    _find_and_set('title', rootNode, article)
    _find_and_set('published_at', rootNode, article, _parse_datetime)
    _find_and_set('link', rootNode, article)
    _find_and_set('guid', rootNode, article)

    categories = _parse_category_set(rootNode, tagName='categories')
    if categories is not None:
        article['categories_set'] = categories

    sourceNode = rootNode.find('source')
    if sourceNode is not None:
        source_dict = {}
        _find_and_set('name', sourceNode, source_dict)
        _find_and_set('guid', sourceNode, source_dict)
        if len(source_dict) > 0:
            article['source'] = source_dict

    author_set = _parse_author_set(rootNode)
    if author_set is not None:
        article['author_set'] = author_set

    return article


def _parse_story_node(rootNode):
    story = {}
    _find_and_set('num_articles', rootNode, story, int)
    _find_and_set('guid', rootNode, story)

    articles = []
    for articleNode in rootNode.find('article_set').findall('article'):
        article = _parse_story_set_article(articleNode)
        if article is not None:
            articles.append(article)
    if len(articles) > 0:
        story['article_set'] = articles

    return story


def parse_story_set(content):
    rootNode = etree.fromstring(content)
    story_set = []
    for storyNode in rootNode.findall('story'):
        story_set.append(_parse_story_node(storyNode))
    return story_set


def parse_article_set(content):
    rootNode = etree.fromstring(content)
    #<article_set num_found="197218">
    article_set = []
    for storyNode in rootNode.findall('article'):
        article_set.append(_parse_single_article(storyNode))
    return article_set