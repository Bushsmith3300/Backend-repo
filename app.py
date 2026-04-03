from flask import Flask, jsonify
from flask_cors import CORS
from chem_questions import questions

app = Flask(__name__)
CORS(app)

@app.route("/questions", methods=["GET"])
def get_questions():
    try:
        if not questions:
            return jsonify({"status": "error", "message": "No questions available"}), 404

        return jsonify({
            "status": "success",
            "total": len(questions),
            "questions": questions
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


