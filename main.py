from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
# @app.route('/index')
def index():
    return render_template('registration.html')

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')