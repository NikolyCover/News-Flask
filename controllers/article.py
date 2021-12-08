from __main__ import app
from flask import render_template

@app.route('/article')
def article():

    return render_template('article.html')
    