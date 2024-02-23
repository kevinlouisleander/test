# app.py
from flask import Flask
import os

app = Flask(__name__)

port = int(os.environ.get('PORT', 3000))

@app.route('/')
def index():
    return "Company: Wild Rydes\nDeveloper: Kevin Leander\nStudent ID: 100918906"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)
