from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/setcookie', methods = ['POST'])
def setcookie1():
    if request.method == 'POST':
        user = request.form['nm']

        resp = make_response(render_template('readcookie.html'))
        resp.set_cookie('userID', user)

        return resp

@app.route('/getcookie', methods = ['GET'])
def getcookie():
    name = request.cookies.get('userID')
    return '<h1>Welcome ' + name + '</h1>'
