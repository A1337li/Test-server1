from flask import Flask, request
app = Flask(__name__)

@app.route("/", methods = ['GET','POST'])
def hello():
    content = request.json
    print (content)
    return "CI server!"

if __name__ == '__main__':
    app.run(debug = True, port=8080)