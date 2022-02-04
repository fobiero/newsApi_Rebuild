# from urllib.request import _UrlopenRet
from ..request import get_articles, get_sources
from flask import render_template
from . import main

@main.route('/')
def index():
    general_sources = get_sources('general')
    title = 'Pata News'

    return render_template('index.html', title = title,general = general_sources)


@main.route('/source/<source_id>')
def artcicles(source_id):

    return render_template('index.html',id = source_id)

@main.route('/source/<int:id>')
def source(id):

    source = get_sources(id)
    title = f'{source.title}'
    # urlToImage = source.urlToImage
    # url = source.url
    
    return render_template('news.html',title = title,source= source)    


@main.route('/articles/<id>')
def article(id):

    '''
   returns article ID
    '''
    article = get_articles(id)
    title = f'{id}'

    return render_template('news.html',title = title,article= article)
    
@main.route('/sports')
def sports():
    '''
    Sports news
    '''

    sport_news = get_sources('sports')

    title = 'Welcome to Home of champions'
    return render_template('sports.html', title = title,sports=sport_news)

@main.route('/business')
def business():
    '''
    Business News
    '''

    business_news = get_sources('business')
    title = 'Business News'
    return render_template('business.html', title = title, business = business_news)


@main.route('/technology')
def technology():
    '''
    technology News
    '''

    technology_news = get_sources('technology')
    title = 'Technology News'
    return render_template('business.html', title = title, technology = technology_news)