from __main__ import app
from flask import render_template

@app.route('/news')

def news():
    return render_template('new.html')