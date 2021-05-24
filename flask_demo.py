from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index_page():
    data = ['hello', 'world']
    return render_template('home.html', data=data)


if __name__ == '__main__':
    app.run(port=8488)
