from flask import Flask, request
import json

from helpers import unconditional_generation, inference_generation

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return "<h1>TEXT GENERATION</h1>"

@app.route('/inference', methods=['POST'])
def model_inference_generation():
    return inference_generation(request.json['input'])

@app.route('/uncondicional', methods=['GET'])
def model_unconditional_generation():
    return unconditional_generation()

if __name__ == '__main__':
    app.run(port='5000',debug=True)