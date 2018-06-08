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
    if data.get('branch') and data.get('token'):
        print('Token and branch keys exist')
    return jsonify({'route':'deploy'})

if __name__ == '__main__':
    app.run(port='8000', host='0.0.0.0')
