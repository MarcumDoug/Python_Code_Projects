# File: temps.py
# Name: Doug Marcum
# Date: 9/28/2019
# Course: DSC 510
# Assignment Number: 6.1
# Description: Allows a user to input a series of temperatures and returns the largest/smallest of the series

print('''This program accepts temperature input(s) and returns the
highest, lowest, and total number of temperatures entered.\n''')
temperatures = []
temps = 0
# a while loop that allows for multiple entries and includes a kill/exit(sentinel value)
while temps != 'x':
    temps = input('Please enter a temperature or type X to stop: ').strip().lower()
    # to verify and/or convert input to float or exit series input
    while True:
        if temps == 'x':
            break
        try:
            float(temps)
            temps = float(temps)
            break
        except ValueError:
            temps = input('\nYou did not enter a temperature.\n'
                          'Please enter a temperature to continue or X to stop: ').strip().lower()
    if temps == 'x':
        break
    temperatures.append(temps)
if not temperatures:
    print('You exited and did not input a temperature to determine a high or low.')
else:
    print('\nYou entered', len(temperatures), 'accepted temperature(s):', temperatures)
    print('The highest temperature is', max(temperatures), 'degrees.')
    print('The lowest temperature is', min(temperatures), 'degrees.')
