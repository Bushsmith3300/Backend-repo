from flask import Flask, jsonify
from flask_cors import CORS
from chem_questions2 import questions2

app = Flask(__name__)
CORS(app)


@app.route("/questions", methods=["GET"])
def get_questions():
    return jsonify({
        "status": "success",
        "total": len(questions2),
        "questions": questions2
    })

