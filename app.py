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
    # Check for branch and token keys
    if data.get('repository') and data.get('branch') and data.get('token'):
        # Check if repository name from request exists in deploy.json
        if app.deploy_json.payload.get(data.get('repository')):
            print('repository exists')
            # Check if branch exists inside of repository
            if app.deploy_json.payload[data.get('repository')].get(data.get('branch')):
                print('branch exists inside of repo')
                # Iterate through build tokens
                for token in app.deploy_json.payload[data.get('repository')][data.get('branch')]:
                    if data.get('token') == token['token']:
                        print('tokens match')
                        return jsonify({'repository': data['repository'], 'branch': data['branch'], 'name': token['name'], 'description': token['description']})
        else:
            return jsonify({'error': 'Invalid repository'})
    else:
        # return jsonify({'error': 'Missing keys', 'missing': ['repository' if not data.get('repository') else None, 'branch' if not data.get('branch') else None, 'token' if not data.get('token') else None]})
        return jsonify({'error': 'Missing keys', 'missing': [token for token in ['repository', 'branch', 'token'] if not data.get(token)]})
    return jsonify({'route':'deploy'})

if __name__ == '__main__':
    app.run(port='8000', host='0.0.0.0')
