from flask import Flask, request
import requests
import json
app = Flask(__name__)

@app.route("/", methods = ['POST'])
def hello():
    content = request.json
    print (content)
    if request.json['action'] in ['opened','edited', 'synchronize']:
    	urrl = request.json['pull_request']['_links']['statuses']['href']
    	payload = {'state': 'failure'}
    
    	r = requests.post(url, json=payload)
    	print(r.urrl)
    return "CI server!"

if __name__ == '__main__':
    app.run(debug = True, port=8080)