# Project:             AS2 - FV Calculator  
# Description:         Calculates the future value of a present investment             
# Depends on:                     
# Developer:           TW              
# Date:                21 September 2025


#A function that calculates and returns the future value of a present investment


def calc_futurevalue(present_value, duration, APR):
    return (present_value * (1 + APR/100) ** duration)