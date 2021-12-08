from __main__ import app
from flask import render_template
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='3511b9c9f1df496da3a30ca5009c0181')

news = newsapi.get_top_headlines(language='pt', country='br', category='entertainment')
news = news['articles']

@app.route('/')
def index():

    return render_template('index.html', news = news)