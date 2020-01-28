from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    print("received request")
    return "Hello Docker!!"


if __name__ == '__main__':
    print("Start server")
    app.run(host='0.0.0.0', port=8080)