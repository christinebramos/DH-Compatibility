# Objective: Determine compatibility scores for each applicant

import json
import math
import pandas as pd

# Read JSON file that contains input
with open('input.json', 'r') as f:
    input_read = json.load(f)

    # Use pandas to read JSON file
    data = pd.read_json('input.json')

    # Normalize data for readabliity
    team_data_normalized = pd.json_normalize(data.team)
    applicants_data_normalized = pd.json_normalize(data.applicants)

    # Initialize team variables
    team_total = 0
    team_intell_sum = 0   
    team_strength_sum = 0
    team_end_sum = 0
    team_spicy_sum = 0
    
    # Get total number of team members
    for tm in team_data_normalized['name']:
        team_total += 1

    # Get sum of scores for each team member attribute
    for tma in team_data_normalized['attributes.intelligence']:
        team_intell_sum += tma

    for tma in team_data_normalized['attributes.strength']:
        team_strength_sum += tma

    for tma in team_data_normalized['attributes.endurance']:
        team_end_sum += tma
        
    for tma in team_data_normalized['attributes.spicyFoodTolerance']:
        team_spicy_sum += tma
 
    # Calculate attribute score averages for team
    team_intell_avg = team_intell_sum / team_total
    team_strength_avg = team_strength_sum / team_total
    team_end_avg = team_end_sum / team_total
    team_spicy_avg = team_spicy_sum / team_total

    # Get user input for attribute weights
    print("- WELCOME TO THE DH COMPATIBILITY PREDICTOR -")
    print("Please follow the instructions below to find the most compatible applicant:")
    print("\tTo determine an applicant's compatibility with the DH team, the four attributes are reviewed:")
    print("\t\t-Intelligence")
    print("\t\t-Physical Strength")
    print("\t\t-Mental Endurance")
    print("\t\t-Spicy Food Tolerance")
    print("\tOnce prompted, plese enter the weights for each of the attributes below.")
    print("\tWeights should be entered as numerical values that when summed, equal to 100.")
    print("\t\ti.e. Intelligence: 25 \n\t\t     Physical Strength: 25 \n\t\t     Mental Endurance: 25 \n\t\t     Spicy Food Tolerance: 25")
    print("\nPlease enter the desired weights for the attributes below:")

    # User input
    intell_weight = int(input("Intelligence: "))
    strength_weight = int(input("Physical Strength: "))
    end_weight = int(input("Mental Endurance: "))
    spicy_weight = int(input("Spicy Food Tolerance: "))

    # Weight conversion
    weight_total = 100
    intell_conv = intell_weight / weight_total
    strength_conv = strength_weight / weight_total
    end_conv = end_weight / weight_total
    spicy_conv = spicy_weight / weight_total
    
    # Sum of entered attribute weights
    weight_sum = intell_conv + strength_conv + end_conv + spicy_conv

    # Input Validation
    # Ideal: Include validation for integer only inputs
    if weight_sum != 1:
        print("\nERROR: Sum of attribute weights do not equal to 100. Please select different values.")
        intell_weight = int(input("Intelligence: "))
        strength_weight = int(input("Physical Strength: "))
        end_weight = int(input("Mental Endurance: "))
        spicy_weight = int(input("Spicy Food Tolerance: "))

    # Declare applicant arrays
    applicants_compat_list = []
    applicants_names = []
    applicants_intell = []
    applicants_strength = []
    applicants_end = []
    applicants_spicy = []

    # Copy applicant names into new array
    for aa in applicants_data_normalized['name']:
        applicants_names.append(aa)
    
    # Calculate team compatibility scores for each attribute
    team_intell_compat = intell_conv * team_intell_avg
    team_strength_compat = strength_conv * team_strength_avg
    team_end_compat = end_conv * team_end_avg
    team_spicy_compat = spicy_conv * team_spicy_avg

    # Calculate applicant compatibility scores for intelligence
    for ac in range(len(applicants_data_normalized['attributes.intelligence'])):
        if applicants_data_normalized['attributes.intelligence'][ac] >= team_intell_avg:
            intell_compat = intell_conv * (applicants_data_normalized['attributes.intelligence'] / team_intell_avg)
        elif applicants_data_normalized['attributes.intelligence'][ac] <= team_intell_avg:
            intell_compat = intell_conv * (team_intell_avg / applicants_data_normalized['attributes.intelligence'])
        applicants_intell.insert(ac, intell_compat[ac])

    # Calculate applicant compatibility scores for strength
    for ac in range(len(applicants_data_normalized['attributes.strength'])):
        if applicants_data_normalized['attributes.strength'][ac] >= team_strength_avg:
            strength_compat = strength_conv * (applicants_data_normalized['attributes.strength'] / team_strength_avg)
        elif applicants_data_normalized['attributes.strength'][ac] <= team_strength_avg:
            strength_compat = strength_conv * (team_strength_avg / applicants_data_normalized['attributes.strength'])
        applicants_strength.insert(ac, strength_compat[ac])

    # Calculate applicant compatibility scores for endurance
    for ac in range(len(applicants_data_normalized['attributes.endurance'])):
        if applicants_data_normalized['attributes.endurance'][ac] >= team_end_avg:
            end_compat = end_conv * (applicants_data_normalized['attributes.endurance'] / team_end_avg)
        elif applicants_data_normalized['attributes.endurance'][ac] <= team_end_avg:
            end_compat = end_conv * (team_end_avg / applicants_data_normalized['attributes.endurance'])
        applicants_end.insert(ac, end_compat[ac])

    # Calculate applicant compatibility scores for spicy food tolerance
    for ac in range(len(applicants_data_normalized['attributes.spicyFoodTolerance'])):
        if applicants_data_normalized['attributes.spicyFoodTolerance'][ac] >= team_spicy_avg:
            spicy_compat = spicy_conv * (applicants_data_normalized['attributes.spicyFoodTolerance'] / team_spicy_avg)
        elif applicants_data_normalized['attributes.spicyFoodTolerance'][ac] <= team_spicy_avg:
            spicy_compat = spicy_conv * (team_spicy_avg / applicants_data_normalized['attributes.spicyFoodTolerance'])
        applicants_spicy.insert(ac, spicy_compat[ac])

    # Move all applicant attribute compatibility scores to a JSON file
    with open('app_compat_list.json', 'w') as af:
        applicants_compat_list = [applicants_names, applicants_intell, applicants_strength, applicants_end, applicants_spicy]
        json.dump(applicants_compat_list, af, indent=4)
    
    # Calculate overall team compatibility score for comparison with applicant
    team_overall = (team_intell_compat + team_strength_compat + team_end_compat + team_spicy_compat) / 4

    # Keep compatibility score within range [0,1]
    if team_overall > 1:
        team_overall = 1

    # Organize attribute scores to be in the same array as applicant name
    applicant1 = []
    applicant2 = []
    applicant3 = []

    applicant1 = [applicants_names[0], applicants_intell[0], applicants_strength[0], applicants_end[0], applicants_spicy[0]]
    applicant2 = [applicants_names[1], applicants_intell[1], applicants_strength[1], applicants_end[1], applicants_spicy[1]]
    applicant3 = [applicants_names[2], applicants_intell[2], applicants_strength[2], applicants_end[2], applicants_spicy[2]]

    # Calculate overall applicant compatibilities by averaging attribute scores
    applicant1_overall = (applicants_intell[0] + applicants_strength[0] + applicants_end[0] + applicants_spicy[0]) / 4
    applicant2_overall = (applicants_intell[1] + applicants_strength[1] + applicants_end[1] + applicants_spicy[1]) / 4
    applicant3_overall = (applicants_intell[2] + applicants_strength[2] + applicants_end[2] + applicants_spicy[2]) / 4

    # Keep compatibility score within range [0,1]
    if applicant1_overall > 1:
        applicant1_overall = 1
    if applicant2_overall > 1:
        applicant2_overall = 1
    if applicant3_overall > 1:
        applicant3_overall = 1

    # Create JSON file for final compatibility scores
    with open('final_compat_scores.json', 'w') as output:
        final_compat_list = {}
        
        final_compat_list['team compatibility score'] = [] 
        final_compat_list['team compatibility score'].append(team_overall)

        final_compat_list['applicant1'] = []
        final_compat_list['applicant1'].append(applicants_names[0])
        final_compat_list['applicant1'].append(applicant1_overall)

        final_compat_list['applicant2'] = []
        final_compat_list['applicant2'].append(applicants_names[1])
        final_compat_list['applicant2'].append(applicant2_overall)

        final_compat_list['applicant3'] = []
        final_compat_list['applicant3'].append(applicants_names[2])
        final_compat_list['applicant3'].append(applicant3_overall)

        json.dump(final_compat_list, output, indent=4)

    print("- Please find the compatibility scores for each applicant in the file final_compat_scores.json. Mahalo. -")

        
