# File: simple_math_average_calc.py
# Name: Doug Marcum
# Date: 9/24/2019
# Course: DSC 510
# Assignment Number: 5.1
# Description: A calculator that takes input and direction from user to perform arithmetic (+,-,*,/) of 2 numbers or
# calculate the total and average of a list of numbers.


def main_option():
    """The backbone of the program. Allows for specific function and operator selection"""
    choice = str(input('''
Please select which calculation you wish to perform:
1) Simple Arithmetic: SA
2) Average of a List of Numbers: AVG
3) Exit Program: EXIT
Please enter SA or AVG or EXIT: ''')).upper().strip()  # upper() and strip() used to standardize responses throughout
    # while loop to allow for function selection or exit from the program
    while not (choice == 'SA' or choice == 'AVG' or choice == 'EXIT'):
        choice = input('You did not enter a valid selection.\n'
                       'Please enter SA, AVG, or EXIT to continue: ').upper().strip()
    if choice == 'SA':
        operator = input('\nFor addition please enter +\n'
                         'For subtraction please enter -\n'
                         'For multiplication please enter *\n'
                         'For division please enter /\n'
                         'Please enter + - * or / to continue: ').strip()
        while not (operator == '+' or operator == '-' or operator == '*' or operator == '/'):
            operator = input('You did not enter a valid operator.\n'
                             '\nPlease enter an accepted operator to continue: ').strip()
        if operator == '+' or operator == '-' or operator == '*' or operator == '/':
            perform_calculation(operator)
    if choice == 'AVG':
        calculate_average()
    if choice == 'EXIT':
        print("Thank you for using the calculator")


def perform_calculation(operator):
    """Function performs basic arithmetic on two numbers based on the operator parameter"""
    while True:
        try:
            first_number = float(input('\nPlease provide your first number: '))
            second_number = float(input('Please provide your second number: '))
            break
        except ValueError:
            print('You did not enter a number. Please try again.')
    if operator == '+':
        print(first_number, operator, second_number, '=', (first_number + second_number))
    elif operator == '-':
        print(first_number, operator, second_number, '=', (first_number - second_number))
    elif operator == '*':
        print(first_number, operator, second_number, '=', (first_number * second_number))
    elif operator == '/' and second_number != 0:
        print(first_number, operator, second_number, '=', (first_number / second_number))
    elif operator == '/' and second_number == 0:
        print('We are sorry, but numbers cannot be divided by zero.\n'
              'Maybe you made a typo and would like to try that one again?')
    try_again()


def calculate_average():
    """Function allows user to input a series of numbers to calculate the average"""
    while True:
        try:
            num_of_iterations = int(input('\nPlease enter how many numbers you would like to evaluate: '))
            break
        except ValueError:
            print('You did not enter a number. Please try again.')
    while True:
        try:
            # takes the input, strips the whitespaces, splits into list of strings, and converts strings into integers
            nums_list = list(map(int, input('Enter the set of numbers like so....\n'
                                            'Example: 1 2 3 4 5 6\n'
                                            'Example: 12 56 78 90 1000 (number followed by a space)\n'
                                            'Please enter the set of numbers for calculation: ').strip().split()))
            break
        except ValueError:
            print('Your set includes something that is not a number. Please try again.\n')
    while True:
        # makes certain the length of the list is the same as the the number of items entered
        if len(nums_list) == num_of_iterations:
            break
        else:
            print('Something does not add up. Please enter your requests again.\n')
            # error detection and correction set of rules
            while True:
                try:
                    num_of_iterations = int(input('Please enter how many numbers you would like to evaluate: '))
                    break
                except ValueError:
                    print('You did not enter a number. Please try again.\n')
            while True:
                try:
                    nums_list = list(map(int, input('Enter the set of numbers for calculation: ').strip().split()))
                    break
                except ValueError:
                    print('Your set includes something that is not a number. Please try again.\n')
    # for loop is used to determine the sum/total is the list of input numbers
    total = 0
    for num in nums_list:
        total = total + num
    average = float(total / num_of_iterations)
    print('For number set', nums_list, 'your calculated average is:', average)
    try_again()


def try_again():
    """This function allows the user to remain in the program or exit upon completion of needs"""
    what_is_next = str(input('\nWould you like to solve another problem, YES or NO: ')).upper().strip()
    while not (what_is_next == 'YES' or what_is_next == 'NO'):
        what_is_next = input('Great answer, just not what is need to move forward.\n'
                             'Please enter YES or NO to continue: ').upper().strip()
    if what_is_next == 'YES':
        main_option()
    if what_is_next == 'NO':
        print('Thank you for using the calculator')


print('Hello and Welcome to Your Calculator!')
main_option()
