from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000", "https://bta-330.vercel.app"])

questions = [("Rutherford's experiment was based on the use of\n\n\
A. Alpha particles\nB. Neutron\nC. Cathode rays\nD. Gamma ray\n", "A"),
("The Cathode rays in JJ Thompson's experiment were later called...\n\n\
A. Protons\nB. Leptons\nC. Quarks\nD. Electrons\n", "D"),
("Who is the nucleus of the atom attributed to?\n\n\
A. JJ Thompson\nB. Neil Bohr\nC. Rutherford\nD. John Dalton\n", "C"),
("Atoms of the same element have the same mass and size. This theory was later disproved by\n\n\
A. radioactivity\nB. Isotopy\nC. Spectral Emission\nD. Diffusion\n", "B"),
("When Alpha particles are passed through a thin gold foil, most of them go\n\
straight through the foil because of\n\nA. The empty space present in the atom\n\
B. The high speed\nC. Positive charge\nD. Negative charge\n", "A"),
("According to Rutherford's atomic model, the electrons inside the atom are\n\n\
A. Stationary\nB. Centralized\nC. Moving\nD. Intersected\n", "C"),
("Rutherford's atomic model suggests that atoms are made up of which kind of particles?\n\n\
A. Protons and neutrons\nB. Electrons and neutrons\nC. Protons and electrons\n\
D. Electrons and Positrons\n", "C"),
("What is the main criticism of Thompson's atomic model?\n\n\
 A. It cannot explain the stability of the atom\n\
 B. It cannot explain the distribution of the electrons in the atom\n\
 C. It cannot explain the spectral lines of the atom\n\
 D. It cannot explain the chemical properties of the atom\n", "A"),
 ("What experiment provided evidence for Thompson's atomic model?\n\n\
 A. The gold foil experiment\nB. The cathode ray tube experiment\n\
 C. The nuclear magnetic resonance experiment\nD. The electron diffraction experiment\n", "B"),
 ("What did Thompson's atomic model propose about the distribution of charge in an atom?\n\n\
 A. The charge is concentrated in a small, dense nucleus\n\
 B. The charge is distributed evenly throughout the atom\n\
 C. The charge is concentrated in the electron orbits\n\
 D. The charge is concentrated in the electron shells\n", "B")]

@app.route('/question_answer_pair', methods=['GET'])
def get_questions():
    return jsonify(questions=questions)

