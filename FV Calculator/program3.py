# Project:             AS2 - FV Calculator  
# Description:         Define user inputs and display the future value of a present investment             
# Depends on:          futurevalue_calculator.py           
# Developer:           TW              
# Date:                21 September 2025


import futurevalue_calculator as fvc

#Functions gather user input for PV, duration, APR
pv = int(input('Enter present value of investment: ')) #converts input to integer

dur = int(input('Enter the number of years that investment will last: ')) #converts input to integer

int_rate = float(input('Enter the annual interest rate for the investment: ')) #converts input to float

print(f'The future value of an investment of ${pv:,.2f} for a duration of {dur:,} years at an interest rate of {int_rate:,}% is ${fvc.calc_futurevalue(pv,dur,int_rate):,.2f}') #formats and displays the result returned by the calc_futurevalue function