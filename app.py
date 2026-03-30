from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

questions = [["The rate determining step for a reaction 2A + 3B ---> 3C is\n\
A +2B ---> D. Therefore the reaction is of the\n\nA. first order\nB. Second order\nC. Third order\n\
D. Zero order", "C"],
["Chemical reactions tend to occur at higher rate at a higher temperature because\n\n\n\
A. masses of the reaction particles become lower at a higher temperature\n\n\
B. The activation energy of the reaction becomes lower at a higher temperature\n\n\
C. The number of effective collisions is higher at higher temperature\n\n\
D. The mechanism of the reaction at a higher temperature is different \
from that at a lower temperature", "C"],
["The minimum amount of energy required for a reaction to take place is known as the\n\n\
A. Kinetic energy\nB. Heat energy\nC. Activation energy\nD. Potential energy", "C"],
["When 1.5 g of Calcium trioxocarbonate (IV) is added to excess dilute hydrochloric acid,\n\
carbon (IV) oxide is given out. The entire reaction takes 15 seconds.\n\n\
What is the rate of reaction in mole per second? [ CaCO3 = 100 ]\n\n\nA. 1.0 x 10^-1 mol/s\n\n\
B. 1.0 x 10^-2 mol/s\n\nC. 1.0 x 10^-3 mol/s\n\nD. 1.0 x 10^-4 mol/s", "C"],
["Chemical reactions tend to occur at a lower rate at a lower temperature Because\n\n\n\
A. masses of the reacting particles become lower at a higher temperature\n\n\
B. The activation energy of the reaction becomes lower at higher temperature\n\n\
C. The number of effective collision is lower at lower temperature\n\n\
D. The mechanism of the reaction at a higher temperature is different from that at a lower \
temperature", "C"],
["The decay of a radioactive material is first order reaction.\nThis means that the rate of decay \
is proportional to\n\nA. Light exposure or intensity\nB. Pressure exerted on it\n\
C. Number of nuclei present\nD. Temperature of the material", "C"],
["The rate of reaction is R = k[X]^2[Y]. By what factor will the rate of the reaction\n\
increase if the concentrations of X and Y are both doubled?\n\nA. 4 times\nB. 8 times\nC. 27 times\n\
D. 64 times", "B"],
["The activation energy of a reaction is the\n\n\nA. energy given out as the reaction proceeds\n\n\
B. Energy used up by the reaction\n\nC. Minimum energy that must be possessed by reactants to \
enable them react\n\nD. Energy absorbed as the reaction proceeds", "C"],
["The collision theory proposes that\n\n\nA. Reactants collide to bring about the destruction \
of molecules\n\nB. All collisions are fruitful\n\nC. Reactants must collide with a certain minimum \
amount of energy to form products\n\nD. The harder the collisions the faster the reaction", "C"],
["A small amount of an element when added to the reaction 3H2(g) + N2(g)  ↔  2NH3(g)\nincreases \
the rate of the reaction element is likely to be\n\nA. A Condenser\nB. A filter\n\
C. A Pollutant\nD. A Catalyst", "D"],
["The minimum amount of energy required to start a chemical reaction is called\n\nA. Activation energy\n\
B. Ionization energy\nC. Heat of Combustion\nD. Chemical energy", "A"],
["The rate of reaction 3A + 2B ----> C + D is doubled when the concentration of A\n\
is doubled and quadrupled when the concentration of B is doubled.\nCalculate the overall \
order of the reaction\n\nA. 5\nB. 3\nC. 4\nD. 2", "B"],
["Increase in temperature of a reaction leads to increase in the reaction rate by\n\n\n\
A. Increasing the concentration of the reactions\n\nB. Lowering the activation energy of the reactants\n\n\
C. Increasing the number of molecules of reactants having their activation energy greater than\n\n\
n\the activation energy of the reactants.\n\nD. Providing an alternative reaction path with low activation energy", "C"],
["Using the same volume of HCl and the same mass of CaCO3, in which of the following\n\n\
situations will the reaction rate be fastest?\n\n\nA. 1.0 mol/dm3 and lumps of CaCO3\n\n\
B. 1.0 mol/dm3 and powdered CaCO3\n\n\
C. 0.1 mol/dm3 and powdered CaCO3\n\nD. 0.1 mol/dm3 and lumps of CaCO3", "B"],
["The rate equation of a reaction is R = K[A][B]^2. By what factor will the reaction rate\n\
change if the concentrations of both A and B are doubled?\n\nA. 4\nB. 8\nC. 27\nD. 64", "B"],
["Which of the following parameters affects the rate of chemical reactions?\n\n\
I. States of reactants\nII. Temperature\nIII. Catalyst\n\nA. I only\n\
B. I and II only\nC. I, II and III\nD. I and III only", "C"],
["The rate of a second order reaction will be numerically equal to the specific rate constant when\n\n\
A. Reaction is homogenous\n\nB. Temperature of the reaction is varied\n\nC. Concentrations of \
the reactants are doubled\n\nD. Concentrations of the reactants are unimolar", "D"],
["Which of the following statements about reaction rates is true?\n\n\n\
A.The rate of reaction varies with temperature of the system\n\n\
B.The rate of reaction increases as the reaction proceeds\n\n\
C.Catalyst increase the rate of forward reactions only\n\n\
D.The reaction between Na2CO3 and HCl is reversible", "A"],
["Which of the following statements is true about the rate of a chemical reaction?\n\n\n\
The rate\n\n\
A.Does not depend on the size of the containing vessel for gaseous phase reactions\n\n\
B.Decreases with increasing temperature\n\nC.Depends on the concentration of the reactants\n\n\
D.Increases with increasing activation energy", "C"],
["Consider the reaction: 2A + 2B + C - ---> D.The rate of the reaction is given by \
R = K[A]^2 [B]^2 [C].\nBy how many times will the rate increase, if the concentrations \
of all reactants are doubled?\n\nA.4\nB.8\nC.16\nD.32", "D"],
["The reaction, 2NO(g) + O2(g) ----> 2NO2(g) was found to be first order with respect to \
each of the reactants.\nThe rate law should therefore be written as \n\nA.Rate = K[NO] ^ 2[O2]\n\n \
B.Rate = K[NO][O2]\n\nC.Rate = K[NO2] ^ 2[O2] ^ 2\n\nD.Rate = K[NO][O2] ^ 2", "B"]]

@app.route("/question_answer_pair", methods=["GET"])
 
def get_questions():
    return jsonify(questions=questions)

