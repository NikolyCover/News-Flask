from __main__ import app
from flask import render_template

@app.route('/news')
def new():

    return render_template('new.html')
    