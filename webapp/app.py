from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get('name', 'World')
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
    
# Neue Route
@app.route('/info', methods=['GET'])
def info():
    return jsonify({
        "status": "running",
        "version": "1.0.0",
        "description": "Flask-App fuer das Git-Merge-Training"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)