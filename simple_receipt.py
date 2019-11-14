# File: simple_receipt.py
# Name: Doug Marcum
# Date: 9/5/2019
# Course: DSC 510
# Assignment Number: 2.1
# Description: Program calculates the installation cost of fiber optic cable and provides a receipt

company_name = input('Hello Human!\nPlease provide the company name you are assisting:')
# To make certain a company name is entered for the receipt, an if/else loop is utilized
while True:
    if len(company_name) > 0:
        break
    else:
        company_name = input('You did not enter a company name. Please enter a company name to continue:')
# To make certain a number is entered for calculation, a try/except block is utilized
while True:
    try:
        feet_needed = float(input('Please provide the number of feet of cable needed to complete the installation:'))
        break
    except ValueError:
        print('You did not enter a number.')
install_cost = .87    # a constant value for installation cost per foot
# total_cost is the calculation of the install cost times feet of cable
total_cost = feet_needed * install_cost
print('Posted below is your receipt')
print('Company Name:', company_name)
print('Length Of Cable For Installation:', feet_needed, 'feet')
print('Installation Cost Per Foot: $', install_cost)
print('Total Cost: $', total_cost)
