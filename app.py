import sys
from classes import Deploy
from flask import Flask, jsonify, request

def create_app(file, debug=True):
    app = Flask(__name__)
    app.debug = debug
    app.deploy_json = Deploy(file)
    return app

with open('deploy.json') as f:
    app=create_app(f)

@app.route('/', methods = ['POST'])
def index():
    data = request.get_json()
    print(app.deploy_json.payload)
    # Check for branch and token keys
    if data.get('repository') and data.get('branch') and data.get('token'):
        # Check of respository exists in deploy.json
        print('Repository, token and branch keys exist')
        if app.deploy_json.payload.get(data.get('repository')):
            print('repository exists')
    return jsonify({'route':'deploy'})

if __name__ == '__main__':
    app.run(port='8000', host='0.0.0.0')
