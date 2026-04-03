from flask import Flask, jsonify, make_response
from questions_data import QUESTIONS  # <-- this is the only import you need

app = Flask(__name__)

@app.route('/questions')
def get_questions():
    response = make_response(jsonify(QUESTIONS))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate'
    response.headers = 'no-cache'
    response.headers = '0'
    return response

