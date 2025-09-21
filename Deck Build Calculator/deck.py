# Project:             AS2 - Cost of building a deck
# Description:         Calculates the cost of building a deck based on square footage, lumber costs, and gallon of  stain costs using object oriented programming          
# Depends on:                     
# Developer:           TW              
# Date:                21 September 2025


#Creates a Deck class with attributes and methods to calculate total cost
class Deck:

    #region initializer
    # Initializes the Deck object with square footage, lumber cost per square foot, stain cost per gallon, stain coverage per gallon, and labor cost

    def __init__(self, sq_ft, lumber_cost_sq_ft, stain_cost_per_gallon):
        self.sq_ft = sq_ft
        self.lumber_cost_sq_ft = lumber_cost_sq_ft
        self.stain_cost_per_gallon = stain_cost_per_gallon
        self.stain_coverage_per_gallon = 297
        self.labor_cost = 31.25

    #endregion

    #region instance methods
    # Calculates the total cost based on square footage, lumber cost per square foot, stain cost per gallon, stain coverage per gallon, and labor cost

    def building_cost(self):
        return (self.sq_ft * self.lumber_cost_sq_ft) + (self.stain_cost_per_gallon * (self.sq_ft / self.stain_coverage_per_gallon)) + (self.labor_cost * self.sq_ft)

    #endregion