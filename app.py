from flask import Flask, jsonify
from flask_cors import CORS
from chem_questions import questions

app = Flask(__name__)
CORS(app)


@app.route("/questions", methods=["GET"])
def get_questions():
    return jsonify({
        "status": "success",
        "total": len(questions),
        "questions": questions
    })


if __name__ == '__main__':
    app.run(debug=True)