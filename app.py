from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/', methods = ['POST'])
def deploy():
    return jsonify({'route':'deploy'})

if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')
