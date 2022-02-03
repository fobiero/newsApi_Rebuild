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

    '''
    View news page function that returns the news details page and its data
    '''
    
    return render_template('index.html',id = source_id)

@main.route('/source/<int:id>')
def source(id):

    '''
    View source page function that returns the movie details page and its data
    '''
    source = get_sources(id)
    title = f'{source.title}'
    urlToImage = source.urlToImage
    url = source.url
    
    return render_template('news.html',title = title,source= source, urlToImage = urlToImage, url = url)    


@main.route('/articles/<id>')
def article(id):

    '''
    View news page function that returns the news details page and its data
    '''
    article = get_articles(id)
    title = f'{id}'

    return render_template('news.html',title = title,article= article)
    
