from flask import Flask 

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello world!'

@app.route('/<name>')
def user(name):
    return 'hello %s' %name

def main():
    app.run(debug = True)

if __name__ == '__main__':
    main()