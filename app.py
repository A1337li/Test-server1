from flask import Flask, request
import requests
import json

app = Flask(__name__)


@app.route("/", methods=['GET','POST'])
def hello():
    content = request.json
    print(content)
    return "CI server!"

@app.route("/pr", methods=['GET','POST'])
def send():
    if request.json['action'] in ['opened', 'edited', 'synchronize']:

        urrl = request.json['pull_request']['_links']['statuses']['href']
        payload = {'state': 'failure'}
        r = requests.post(urrl, json=payload)
        print(r.url)
        return 'works'
    else:
        content2 = request.json
        print (content2)
    return 'hello'

if __name__ == '__main__':
    app.run(debug=True, port=8080)