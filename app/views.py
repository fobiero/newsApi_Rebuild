# from flask import render_template
from app import app
# from .request import get_news
# from .request import get_news,get_news
from flask import render_template,request,redirect,url_for

#views
# @TODO: Route to homePage 
@app.route('/')
def index():
    '''
    returns to homePage
    '''

    return render_template('index.html')

# @TODO: Politics Route 
@app.route('/politics/<int:id>')
def politics():
    '''
    returns to homePage
    '''

    return render_template('politics.html', id=id)

# @TODO: technology Route 
@app.route('/technology')
def technology():
    '''
    returns to homePage
    '''

    return render_template('technology.html')

# @TODO: Sports Route 
@app.route('/sports')
def sports():
    '''
    returns to homePage
    '''

    return render_template('sports.html')