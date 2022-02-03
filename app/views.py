from flask import render_template
from app import app
# from .request import get_news
# from .request import get_news,get_news
from flask import render_template,request,redirect,url_for

#views
# @TODO: Route to homePage 
@app.route('/')
def home():

    '''
    returns to homePage
    '''

    return render_template('home.html')