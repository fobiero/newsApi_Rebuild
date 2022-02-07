import urllib
import base64
import sys
import urllib.request,json
from .models import Sources, Articles

Sources = Sources
Article = Articles

api_key= None
news_base_url = None
articles_url = None

def configure_request(app):
    global api_key, news_sources_url, articles_url  

    api_key = app.config['API_KEY']
    news_sources_url = app.config["NEWS_BASE_URL"]
    articles_url =app.config['SOURCE_API_URL']

def get_sources(category):

    get_sources_url = news_sources_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
           source_results_list = get_sources_response['sources']
           source_results = process_source_results(source_results_list)

    return source_results


def process_source_results(source_list):
    source_results = []
    for source_item in source_list:

        id = source_item.get('id')
        name = source_item.get('name')
        author= source_item.get('author')
        title = source_item.get('title')
        description = source_item.get('description')
        publishedAt= source_item.get('publishedAt')
        urlToImage = source_item.get('urlToImage')
        url= source_item.get('url')
        
        source_object = Sources(id,name,author,title,description,publishedAt,urlToImage,url)
        source_results.append(source_object)

    return source_results  


def get_articles(id):

    get_articles_url = articles_url.format(id,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
           articles_results_list = get_articles_response['articles']
           articles_results = process_source_results(articles_results_list)


    return articles_results


def process_articles_results(articles_list):

    article_results = []

    for article_item in articles_list:
        urlToImage = article_item.get('urlToImage')
        title = article_item.get('title')
        name = article_item.get('name')
        author= article_item.get('author')
        description = article_item.get('description')
        publishedAt= article_item.get('publishedAt')
        url= article_item.get('url')

        article_object = Articles(name,author,title,description,publishedAt,urlToImage,url)
        article_results.append(article_object)

    return article_results      
