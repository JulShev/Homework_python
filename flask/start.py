from flask import Flask, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')


@app.route('/')
def main():
    return render_template('index.html', text = 'текст')
@app.route('/login')
def login():
    return render_template('login.html', text = 'введите имя')
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
