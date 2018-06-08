import sys
from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/', methods = ['POST'])
def deploy():
    data = request.get_json()
    # Check for branch and token keys
    if data.get('branch') and data.get('token'):
        print('Token and branch keys exist')
    return jsonify({'route':'deploy'})

if __name__ == '__main__':
    try:
        with open('deploy.json') as f:
            app.run(debug=True, port=8000, host='0.0.0.0')
    except:
        print('Missing deploy.json file.')
        sys.exit(1)
