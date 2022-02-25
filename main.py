from flask import Flask

app = Flask(__name__)

@app.route('/', methods = ['get', 'post'])
def harish():
    return "Hi, Mr. Harish do more and more hard and smart work"


if __name__ == "__main__":

    app.run()
