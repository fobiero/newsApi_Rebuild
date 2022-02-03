from app.request import get_news
from flask import render_template
from app import app

# Views
@app.route('/')
def index():
    # Getting technology news on pageLoad

    news_results = get_news('popular')
    print(news_results)
    title = 'Pata News ya Usasa'
    return render_template('index.html', title = title, popular = news_results)

