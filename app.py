from flask import *
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    
    return render_template("index.html")


@app.route('/register')
def register():
    return render_template("register.html")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="80")