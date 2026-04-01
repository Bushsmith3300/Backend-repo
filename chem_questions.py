# data/questions.py

questions = [
    {
        "id": 1,
        "question": "The rate determining step for a reaction 2A + 3B ---> 3C is A + 2B ---> D. Therefore the reaction is of the",
        "options": [
            "A. first order",
            "B. Second order",
            "C. Third order",
            "D. Zero order"
        ],
        "answer": "C",
        "explanation": "The rate-determining step is the slowest step in a reaction mechanism and determines the overall rate law and order. Here, the slow step is A + 2B → D, which involves 1 A and 2 B, so the overall order is 1 + 2 = 3 (third order)."
    },
    {
        "id": 2,
        "question": "Chemical reactions tend to occur at higher rate at a higher temperature because",
        "options": [
            "A. masses of the reaction particles become lower at a higher temperature",
            "B. The activation energy of the reaction becomes lower at a higher temperature",
            "C. The number of effective collisions is higher at higher temperature",
            "D. The mechanism of the reaction at a higher temperature is different from that at a lower temperature"
        ],
        "answer": "C",
        "explanation": "Higher temperature increases the average kinetic energy of molecules, leading to more frequent and energetic collisions. This results in a higher fraction of collisions having energy greater than or equal to the activation energy, thus increasing the number of effective collisions."
    },
    {
        "id": 3,
        "question": "The minimum amount of energy required for a reaction to take place is known as the",
        "options": [
            "A. Kinetic energy",
            "B. Heat energy",
            "C. Activation energy",
            "D. Potential energy"
        ],
        "answer": "C",
        "explanation": "Activation energy (Ea) is the minimum energy barrier that reactant molecules must overcome to form products. It is the difference between the energy of reactants and the transition state."
    },
    {
        "id": 4,
        "question": "When 1.5 g of Calcium trioxocarbonate (IV) is added to excess dilute hydrochloric acid, carbon (IV) oxide is given out. The entire reaction takes 15 seconds. What is the rate of reaction in mole per second? [ CaCO3 = 100g/mol ]",
        "options": [
            "A. 1.0 x 10^-1 mol/s",
            "B. 1.0 x 10^-2 mol/s",
            "C. 1.0 x 10^-3 mol/s",
            "D. 1.0 x 10^-4 mol/s"
        ],
        "answer": "C",
        "explanation": "Moles of CaCO3 = 1.5 g / 100 g/mol = 0.015 mol. Since 1 mole CaCO3 produces 1 mole CO2, moles of CO2 = 0.015 mol. Rate = 0.015 mol / 15 s = 0.001 mol/s = 1.0 × 10^{-3} mol/s."
    },
    {
        "id": 5,
        "question": "Chemical reactions tend to occur at a lower rate at a lower temperature Because",
        "options": [
            "A. masses of the reacting particles become lower at a higher temperature",
            "B. The activation energy of the reaction becomes lower at higher temperature",
            "C. The number of effective collision is lower at lower temperature",
            "D. The mechanism of the reaction at a higher temperature is different from that at a lower temperature"
        ],
        "answer": "C",
        "explanation": "At lower temperature, molecules have lower kinetic energy, so fewer collisions have sufficient energy to overcome the activation energy barrier. Hence, the number of effective collisions decreases, slowing down the reaction rate."
    },
    {
        "id": 6,
        "question": "The decay of a radioactive material is first order reaction. This means that the rate of decay is proportional to",
        "options": [
            "A. Light exposure or intensity",
            "B. Pressure exerted on it",
            "C. Number of nuclei present",
            "D. Temperature of the material"
        ],
        "answer": "C",
        "explanation": "For a first-order reaction, rate = k × [reactant]. In radioactive decay, the rate is proportional to the number of radioactive nuclei present at that time."
    },
    {
        "id": 7,
        "question": "The rate of reaction is R = k[X]^2[Y]. By what factor will the rate of the reaction increase if the concentrations of X and Y are both doubled?",
        "options": [
            "A. 4 times",
            "B. 8 times",
            "C. 27 times",
            "D. 64 times"
        ],
        "answer": "B",
        "explanation": "Rate = k[X]^2[Y]. When both concentrations are doubled: new rate = k(2X)^2(2Y) = k × 4X² × 2Y = 8 × kX²Y. So the rate increases by 8 times."
    },
    {
        "id": 8,
        "question": "The activation energy of a reaction is the",
        "options": [
            "A. energy given out as the reaction proceeds",
            "B. Energy used up by the reaction",
            "C. Minimum energy that must be possessed by reactants to enable them react",
            "D. Energy absorbed as the reaction proceeds"
        ],
        "answer": "C",
        "explanation": "Activation energy is the minimum energy that colliding reactant molecules must possess for the collision to be effective and lead to product formation."
    },
    {
        "id": 9,
        "question": "The collision theory proposes that",
        "options": [
            "A. Reactants collide to bring about the destruction of molecules",
            "B. All collisions are fruitful",
            "C. Reactants must collide with a certain minimum amount of energy to form products",
            "D. The harder the collisions the faster the reaction"
        ],
        "answer": "C",
        "explanation": "According to collision theory, for a reaction to occur, particles must collide with proper orientation and with kinetic energy equal to or greater than the activation energy."
    },
    {
        "id": 10,
        "question": "A small amount of an element when added to the reaction 3H2(g) + N2(g) ↔ 2NH3(g) increases the rate of the reaction. The element is likely to be",
        "options": [
            "A. A Condenser",
            "B. A filter",
            "C. A Pollutant",
            "D. A Catalyst"
        ],
        "answer": "D",
        "explanation": "A catalyst is a substance that increases the rate of a reaction without being consumed. It provides an alternative pathway with lower activation energy."
    },
    {
        "id": 11,
        "question": "The minimum amount of energy required to start a chemical reaction is called",
        "options": [
            "A. Activation energy",
            "B. Ionization energy",
            "C. Heat of Combustion",
            "D. Chemical energy"
        ],
        "answer": "A",
        "explanation": "Activation energy is the minimum energy required to initiate a chemical reaction by breaking bonds in reactant molecules."
    },
    {
        "id": 12,
        "question": "The rate of reaction 3A + 2B ----> C + D is doubled when the concentration of A is doubled and quadrupled when the concentration of B is doubled. Calculate the overall order of the reaction",
        "options": [
            "A. 5",
            "B. 3",
            "C. 4",
            "D. 2"
        ],
        "answer": "B",
        "explanation": "When [A] is doubled, rate doubles → order w.r.t. A is 1. When [B] is doubled, rate becomes 4 times → order w.r.t. B is 2. Overall order = 1 + 2 = 3."
    },
    {
        "id": 13,
        "question": "Increase in temperature of a reaction leads to increase in the reaction rate by:",
        "options": [
            "A. Increasing the concentration of the reactions",
            "B. Lowering the activation energy of the reactants",
            "C. Increasing the number of molecules of reactants having their activation energy greater than the activation energy of the reactants.",
            "D. Providing an alternative reaction path with low activation energy"
        ],
        "answer": "C",
        "explanation": "Increasing temperature increases the fraction of molecules that have kinetic energy greater than the activation energy (according to Maxwell-Boltzmann distribution), leading to more effective collisions."
    },
    {
        "id": 14,
        "question": "Using the same volume of HCl and the same mass of CaCO3, in which of the following situations will the reaction rate be fastest?",
        "options": [
            "A. 1.0 mol/dm3 and lumps of CaCO3",
            "B. 1.0 mol/dm3 and powdered CaCO3",
            "C. 0.1 mol/dm3 and powdered CaCO3",
            "D. 0.1 mol/dm3 and lumps of CaCO3"
        ],
        "answer": "B",
        "explanation": "Powdered CaCO3 has larger surface area than lumps, increasing the frequency of collisions with HCl. Higher concentration (1.0 mol/dm³) also increases collision frequency. So powdered + higher concentration gives the fastest rate."
    },
    {
        "id": 15,
        "question": "The rate equation of a reaction is R = K[A][B]^2. By what factor will the reaction rate change if the concentrations of both A and B are doubled?",
        "options": [
            "A. 4",
            "B. 8",
            "C. 27",
            "D. 64"
        ],
        "answer": "B",
        "explanation": "Rate = k[A][B]^2. When both doubled: new rate = k(2A)(2B)^2 = k × 2A × 4B² = 8 × original rate. So the rate increases by a factor of 8."
    },
    {
        "id": 16,
        "question": "Which of the following parameters affects the rate of chemical reactions?\nI. States of reactants\nII. Temperature\nIII. Catalyst",
        "options": [
            "A. I only",
            "B. I and II only",
            "C. I, II and III",
            "D. I and III only"
        ],
        "answer": "C",
        "explanation": "All three factors affect reaction rate: physical state/surface area of reactants, temperature (affects kinetic energy), and catalysts (lower activation energy)."
    },
    {
        "id": 17,
        "question": "The rate of a second order reaction will be numerically equal to the specific rate constant when:",
        "options": [
            "A. Reaction is homogenous",
            "B. Temperature of the reaction is varied",
            "C. Concentrations of the reactants are doubled",
            "D. Concentrations of the reactants are unimolar"
        ],
        "answer": "D",
        "explanation": "For a second-order reaction, rate = k[A]^2 or k[A][B]. When concentrations are 1 mol/L (unimolar), rate = k × (1)^2 = k. So numerically, rate equals the rate constant k."
    },
    {
        "id": 18,
        "question": "Which of the following statements about reaction rates is true?",
        "options": [
            "A. The rate of reaction varies with temperature of the system",
            "B. The rate of reaction increases as the reaction proceeds",
            "C. Catalyst increase the rate of forward reactions only",
            "D. The reaction between Na2CO3 and HCl is reversible"
        ],
        "answer": "A",
        "explanation": "Reaction rate is highly dependent on temperature (Arrhenius equation: k = Ae^{-Ea/RT}). The other options are generally false."
    },
    {
        "id": 19,
        "question": "Which of the following statements is true about the rate of a chemical reaction? The rate",
        "options": [
            "A. Does not depend on the size of the containing vessel for gaseous phase reactions",
            "B. Decreases with increasing temperature",
            "C. Depends on the concentration of the reactants",
            "D. Increases with increasing activation energy"
        ],
        "answer": "C",
        "explanation": "Rate of reaction depends on the concentration of reactants (as per rate law). It increases with temperature and decreases with higher activation energy."
    },
    {
        "id": 20,
        "question": "Consider the reaction: 2A + 2B + C ---> D. The rate of the reaction is given by R = K[A]^2 [B]^2 [C]. By how many times will the rate increase, if the concentrations of all reactants are doubled?",
        "options": [
            "A. 4",
            "B. 8",
            "C. 16",
            "D. 32"
        ],
        "answer": "D",
        "explanation": "Rate = k[A]^2[B]^2[C]. When all concentrations doubled: new rate = k(2A)^2(2B)^2(2C) = k × 4A² × 4B² × 2C = 32 × original rate."
    }
]