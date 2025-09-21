# Project:             AS2 - Cost of building a deck
# Description:         Calculates the cost of building a deck based on square footage, lumber costs, and gallon of  stain costs using object oriented programming          
# Depends on:          deck.py           
# Developer:           TW              
# Date:                21 September 2025

import deck as d #imports the deck module

#Functions gather user input for square footage, lumber cost per square foot and stain cost per gallon

sq_ft = int(input('Enter the square footage of the deck: ')) #converts input to integer

lumber_cost_sq_ft = float(input('Enter the cost of lumber per square foot: ')) #converts input to float

stain_cost_per_gallon = float(input('Enter the cost of stain per gallon: ')) #converts input to float

deck_1 = d.Deck(sq_ft, lumber_cost_sq_ft, stain_cost_per_gallon) #creates an instance of the Deck class using the previously defined user inputs

print(f'The cost of building a {sq_ft:,} square foot deck with lumber costing ${lumber_cost_sq_ft:,.2f} per square foot and stain costing ${stain_cost_per_gallon:,.2f} per gallon is ${deck_1.building_cost():,.2f}') #formats and displays the result returned by the building_cost method