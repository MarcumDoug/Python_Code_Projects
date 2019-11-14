# File: calc_function.py
# Name: Doug Marcum
# Date: 9/18/2019
# Course: DSC 510
# Assignment Number: 4.1
# Description: Program uses functions to calculate the installation cost of fiber optic cable based on volume pricing

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


def bulk_rate():
    """Return the installation cost rate depending on the number of feet of cable needed"""
    if feet_needed > 500:
        install_cost = .50
    elif feet_needed > 250:
        install_cost = .70
    elif feet_needed > 100:
        install_cost = .80
    else:
        install_cost = .87     # standard installation rate, no discount applied
    return float(install_cost)


def total_cost(feet, price):
    """Return the calculated total cost of the cable installation"""
    return print('Total Cost: $', format((feet * price), '.2f'))


# Printable Receipt Information
print('Posted below are your results')
print('Company Name:', company_name)
print('Length Of Cable For Installation:', feet_needed, 'feet')
print('Your Installation Rate Per Foot Is: $', format(bulk_rate(), '.2f'))
total_cost(feet_needed, bulk_rate())


