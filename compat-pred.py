# Christine Ramos
# Objective: Determine compatibility scores for each applicant

import json
import math

from funct import calcAvg
from funct import getTeamAtt
from funct import getApplicantAtt
from funct import calcCompatScore

# Read JSON file that contains input
with open('input.json', 'r') as f:
    input_read = json.load(f)

    for a in input_read:
        # Get team intelligence attributes + calculate average
        team_intell = getTeamAtt('team', 'intelligence')
        team_intell_avg = calcAvg(team_intell)

        # Get team strength attributes + calculate average
        team_strength = getTeamAtt('team', 'strength')
        team_strength_avg = calcAvg(team_strength)

        # Get team endurance attributes + calculate average 
        team_end = getTeamAtt('team', 'endurance')
        team_end_avg = calcAvg(team_end)

        # Get team spicyFoodTolerance attributes + calculate average
        team_spicy = getTeamAtt('team', 'spicyFoodTolerance')
        team_spicy_avg = calcAvg(team_spicy)

        # Get applicant attributes
        applicant_attributes = getApplicantAtt()
        
    
