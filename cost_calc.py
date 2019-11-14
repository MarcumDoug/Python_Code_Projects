# File: cost_calc.py
# Name: Doug Marcum
# Date: 9/10/2019
# Course: DSC 510
# Assignment Number: 3.1
# Description: Program calculates the installation cost of fiber optic cable based on volume pricing

company_name = str(input('Hello and Welcome to the Volume Cost Calculator!\n'
                         'Please provide the company name you are assisting: '))
# To make certain a company name is entered for the receipt, an if/else loop is utilized
while True:
    if len(company_name) > 0:
        break
    else:
        company_name = input('You did not enter a company name.\n'
                             'Please enter a company name to continue: ')
# To make certain a number is entered for calculation, a try/except block is utilized
while True:
    try:
        feet_needed = float(input('Please provide the number of feet of cable needed to complete the installation: '))
        break
    except ValueError:
        print('You did not enter a number.')

standard_cost = .87  # standard cost of installation per foot
install_cost = ()    # installation cost per foot
# variable volume cost structure for bulk purchases if statement
if feet_needed > 500:
    install_cost = .50
elif feet_needed > 250:
    install_cost = .70
elif feet_needed > 100:
    install_cost = .80
else:
    install_cost = standard_cost

# total_cost is the calculation of the install cost times feet of cable
total_cost = round((feet_needed * install_cost), 2)

# Printable Receipt Information
print('Posted below are your results')
print('Company Name:', company_name)
print('Length Of Cable For Installation:', feet_needed, 'feet')
print('Installation Cost Per Foot: $', (format(install_cost, '.2f')))
if feet_needed > 100:
    print('A volume purchasing discount of $', (standard_cost - install_cost), 'per foot was applied')
else:
    print('The standard installation cost was applied')
print('Total Cost: $', (format(total_cost, '.2f')))
