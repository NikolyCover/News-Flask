#from __main__ import app
def dostuff(self):
     from __main__ import app

from flask import render_template
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='3511b9c9f1df496da3a30ca5009c0181')

@app.route('/')
def general():
    articles = newsapi.get_top_headlines(language='pt', country='br', category='general')
    articles = articles['articles']

    return render_template('index.html', articles = articles)

@app.route('/<category>')
def business(category):
    articles = newsapi.get_top_headlines(language='pt', country='br', category=category)
    articles = articles['articles']

    return render_template('index.html', articles = articles)
