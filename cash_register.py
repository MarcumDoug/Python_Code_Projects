# File: cash_register.py
# Name: Doug Marcum
# Date: 11/05/2019
# Course: DSC 510
# Assignment Number: 11.1
# Description: A simple cash register that allows the user to add the price of items to
#              the cart and prints the total item count / total price in US currency.

import locale
print("Welcome to the Personal Cash Register Program. Let's get started.")  # Welcome Message to User


class CashRegister:
    def __init__(self):
        self.total_price = 0
        self.item_count = 0

    def add_item(self, price):
        self.total_price = self.total_price + price
        self.item_count += 1

    def get_total(self):
        locale.setlocale(locale.LC_ALL, 'en_US.utf-8')
        return locale.currency(self.total_price, symbol=True)

    def get_count(self):
        return self.item_count

    def clear(self):
        self.total_price = 0
        self.item_count = 0
        print('\nGreat! Your previous cart has been deleted.'
              f'\nThere are currently {self.get_count()} items totalling {self.get_total()} in your new cart.')
        main()


def main():
    """The main function asking for the user input of prices, creating a loop for additional user input, and
     making the calls to the CashRegister class"""
    register = CashRegister()
    price = []
    while price != 'total':
        price = input("Please enter a price to be included or enter 'total' "
                      "to calculate your cart: ").strip().strip('$').lower()
        while True:
            if price == 'total':
                break
            # try and except block to catch input errors
            try:
                price = float(price)
                break
            except ValueError:
                price = input('\nYour last entry was not a valid selection.\n'
                              "Please enter a price or 'total' to continue: ").strip().strip('$').lower()
        if price == 'total':
            print(f'\nThere are {register.get_count()} items in your cart totalling {register.get_total()}.')
            option = str(input('Would you like to start a new cart, Yes or No? ')).lower().strip()
            # while loop to allow for a yes selection or to exit the program (and to catch input errors)
            while not (option == 'yes' or option == 'no'):
                option = str(input('\nYour last entry was not a valid selection.\n'
                                   'Please enter Yes or No to continue: ')).lower().strip()
            if option == 'yes':
                register.clear()
            if option == 'no':
                print('Thank you for using the Personal Cash Register Program.')  # Exit Message To User
            break
        register.add_item(price)


main()
