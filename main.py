from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('main.html')

@app.route('/registration')
def register():
    return render_template('registration.html')


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/post')
def post():
    return render_template('post.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')