from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1><b>Hello,  This is Lindsay Wangari</b></h1>"

if __name__ == '__main__':
    app.run(debug=True)
