from flask import Flask, render_template

app = Flask(__name__)

from controllers import news

if __name__ == '__main__':
    app.run(debug=True)