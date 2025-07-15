from flask import Flask
from datetime import datetime
app = Flask(__name__)


@app.route('/')
def index():
    return 'Welcome to Python Flask World v5.0 from cicd-gke'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)


