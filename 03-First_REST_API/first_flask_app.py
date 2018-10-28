from flask import Flask

app = Flask(__name__)

@app.route('/') # 'http://www.google.com/'
def home():
    return "Hola mundo desde Flask!"

app.run(port=5000)
