# DH Compatibility Predictor

# Project Objective
Help DataHouse determine the most compatible applicant for the company by generating compatibility scores for each applicant.

# Chosen Approach
Keeping the "open-ended" mindset of the project in mind, the logic used has been based off of various possible user inputs for the company's preferences. Each attribute will be assigned a specific weight that can only be determined via user input.

Programming language: Python

# Run Program
This program must be compiled using python3 due to the use of the pandas (Python data analysis library).

Simply run "python3 compat-pred.py" in the command line to compile and begin the program.

The user will be prompted to enter specific weight values per attribute where the sum of all weights must equal to 100.
Once completed, the final compatibility scores for each applicant can be found in a JSON file called "final_compat_scores.json".

# Notes
The final compatibility scores for each applicant is determined by multiplying each weight value to their respective attribute scores that is divided by an averaged team attribute score.

If you have any questions or concerns regarding this project, feel free to email me at cbramos6@hawaii.edu.

Thank you!
