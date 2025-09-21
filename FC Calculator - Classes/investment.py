# Project:             AS2 - Investment Class Calculator
# Description:         Calculates the future value of a present investment using object oriented programming            
# Depends on:                     
# Developer:           TW              
# Date:                21 September 2025


#Creates an Investment class with attributes and methods to calculate future value
class Investment:

    #region initializer

    def __init__(self, present_value, duration, APR):
        self.present_value = present_value
        self.duration = duration
        self.APR = APR

    #endregion

    #region instance methods

    def calc_futurevalue(self):
        return (self.present_value * (1 + self.APR/100) ** self.duration)

    #endregion