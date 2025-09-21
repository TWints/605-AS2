# Project:             AS2 - Investment Class Calculator
# Description:         Calculates the future value of a present investment using object oriented programming            
# Depends on:          investment.py           
# Developer:           TW              
# Date:                21 September 2025


import investment as inv #imports the investment module

#Functions gather user input for PV, duration, APR
pv = int(input('Enter present value of investment: ')) #converts input to integer

dur = int(input('Enter the number of years that investment will last: ')) #converts input to integer

int_rate = float(input('Enter the annual interest rate for the investment: ')) #converts input to float

inv_1 = inv.Investment(pv, dur, int_rate) #creates an instance of the Investment class using the previously defined user inputs

print(f'The future value of an investment of ${pv:,.2f} for a duration of {dur:,} years at an interest rate of {int_rate:,}% is ${inv_1.calc_futurevalue():,.2f}') #formats and displays the result returned by the calc_futurevalue method