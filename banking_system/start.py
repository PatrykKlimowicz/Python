import random
import sys
import sqlite3


class Card:
    def __init__(self):
        self.data = self.__create_card()

    def __create_card(self):
        digits = "0123456789"
        card_number = "400000"
        pin = str()

        for _ in range(9):
            card_number += random.choice(digits)

        for _ in range(4):
            pin += random.choice(digits)

        card_number += self.count_card_checksum(card_number)
        return {card_number: pin}

    def count_card_checksum(self, card_number: str()):
        if len(card_number) == 16:
            temp_number = card_number[0:-1]
        else:
            temp_number = card_number

        # use the Luhn algorithm to calculate last digit checksum
        card_checksum = 0
        for i, digit in enumerate(temp_number, 1):
            digit = int(digit)
            if i % 2:
                if digit * 2 > 9:
                    card_checksum += digit * 2 - 9
                else:
                    card_checksum += digit * 2
            else:
                card_checksum += digit

        if not card_checksum % 10:
            return "0"
        else:
            return str((card_checksum + 9) // 10 * 10 - card_checksum)


class DataBase:
    def __init__(self):
        self.connection = sqlite3.connect("card.s3db")
        self.cursor = self.connection.cursor()

    def table_exist(self):
        self.cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='card';")
        return self.cursor.fetchone()

    def table_create(self):
        if not self.table_exist():
            self.cursor.execute(
                "CREATE TABLE card (id INTEGER, number TEXT, pin TEXT, balance INTEGER DEFAULT 0);")

    def add_card(self, card_number: str(), card_pin: str()):
        self.cursor.execute(
            f"INSERT INTO card (number, pin) VALUES ('{card_number}', '{card_pin}')")
        self.connection.commit()

    def get_card_number(self, pin: str()):
        self.cursor.execute(f"SELECT number FROM card WHERE pin='{pin}';")
        self.connection.commit()
        res = str(self.cursor.fetchone()).strip("'()',")

        return res

    def is_in_table(self, card_number: str()):
        self.cursor.execute(
            f"SELECT pin FROM card WHERE number='{card_number}'")
        self.connection.commit()

        if self.cursor.fetchone() is None:
            return False
        return True

    def get_balance(self, card_number: str(), card_pin: str()):
        self.cursor.execute(
            f"SELECT balance FROM card WHERE number='{card_number}' AND pin='{card_pin}';")
        self.connection.commit()
        res = int(str(self.cursor.fetchone()).strip("(,)"))

        return res

    def transfer_money(self, card_number: str(), amount: str()):
        self.cursor.execute(
            f"UPDATE card SET balance=balance+{amount} WHERE number='{card_number}'")
        self.connection.commit()

    def update_balance(self, card_number: str(), card_pin: str(), new_balance: int()):
        self.cursor.execute(
            f"UPDATE card SET balance={new_balance} WHERE number='{card_number}' AND pin='{card_pin}'")
        self.connection.commit()

    def delete_card(self, card_number: str()):
        self.cursor.execute(f"DELETE FROM card WHERE number='{card_number}'")
        self.connection.commit()


class Bank:
    def __init__(self):
        self.db = DataBase()
        self.db.table_create()
        self.__curr_card_number = None
        self.__curr_card_pin = None
        self.__curr_card = None

    def create_account(self):
        self.__curr_card = Card()

        card_data = self.__curr_card.data
        ((c_number, c_pin), ) = tuple(card_data.items())
        print("\nYour card has been created")
        print("Your card number:", c_number, sep='\n')
        print("Your card PIN:", c_pin, sep='\n')

        self.db.add_card(c_number, c_pin)

    def __card_is_valid(self, card_num: str()):
        if not len(card_num):
            print("\nWrong card number or PIN!\n")
            return False

        if self.__curr_card_number == card_num:
            print("\nYou have successfully logged in!")
            return True
        else:
            print("\nWrong card number or PIN!\n")
            return False

    def log_in(self):
        self.__curr_card_number = input("Enter your card number:\n")
        self.__curr_card_pin = input("Enter your PIN:\n")

        # get card number with specific pin from db
        card_num = self.db.get_card_number(self.__curr_card_pin)
        return self.__card_is_valid(card_num)

    def get_balance(self):
        return self.db.get_balance(self.__curr_card_number, self.__curr_card_pin)

    def add_income(self):
        balance = self.get_balance()
        income = int(input("Enter income:\n"))
        new_balance = balance + income
        self.db.update_balance(self.__curr_card_number,
                               self.__curr_card_pin, new_balance)
        print("Income was added!\n")

    def do_transfer(self):
        current_balance = self.get_balance()
        print("Transfer")
        recipient_card_number = input("Enter card number:\n")

        if self.__curr_card_number == recipient_card_number:
            print("You can't transfer money to the same account!")
            return

        if recipient_card_number[-1] != self.__curr_card.count_card_checksum(recipient_card_number):
            print("Probably you made mistake in the card number. Please try again!\n")
            return

        if self.db.is_in_table(recipient_card_number):
            amount = int(input("Enter how much money you want to transfer:\n"))

            if current_balance < amount:
                print("Not enough money!\n")
            else:
                print("Success!\n")
                new_balance = current_balance - amount
                self.db.update_balance(
                    self.__curr_card_number, self.__curr_card_pin, new_balance)
                self.db.transfer_money(recipient_card_number, amount)
        else:
            print("Such a card does not exist.\n")

    def close_account(self):
        self.db.delete_card(self.__curr_card_number)


if __name__ == "__main__":
    def print_main_menu():
        print("\n1. Create an account\n2. Log into account\n0. Exit")

    def print_option_menu():
        print("\n1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit")

    bank = Bank()
    while True:
        print_main_menu()
        option = int(input())

        if option == 1:
            bank.create_account()
        elif option == 2:
            if bank.log_in():
                while True:
                    print_option_menu()
                    sub_option = int(input())

                    if sub_option == 1:
                        acc_balance = bank.get_balance()
                        print(f"Balance: {acc_balance}")
                    elif sub_option == 2:
                        bank.add_income()
                    elif sub_option == 3:
                        bank.do_transfer()
                    elif sub_option == 4:
                        bank.close_account()
                        print("The account has been closed!\n")
                        break
                    elif sub_option == 5:
                        break
                    elif sub_option == 0:
                        print("Bye!")
                        sys.exit()
        else:
            print("Bye!")
            sys.exit()
