from flask import Flask, jsonify, make_response
from chem_questions2 import questions2  # <-- this is the only import you need

app = Flask(__name__)

@app.route('/questions')
def get_questions():
    response = make_response(jsonify(questions2))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate'
    response.headers = 'no-cache'
    response.headers = '0'
    return response

