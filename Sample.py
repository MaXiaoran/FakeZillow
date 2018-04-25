"""
    Testing Flask installation
"""
from werkzeug.routing import BaseConverter
from flask import Flask,render_template,request


class RegexConvert(BaseConverter):
    def __init__(self,url_map,*itms):
        super(RegexConvert,self).__init__(url_map)
        self.regex=itms[0]


app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html', title = 'Welcome')


@app.route('/services')
def services():
    return 'services'


@app.route('/login')
def login():
    return render_template('login.html', method=request.method)


if __name__ == '__main__':
    app.run(debug=True)
