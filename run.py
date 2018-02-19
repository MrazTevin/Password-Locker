from user import User
import pyperclip
import random
from account import Account


def create_user(user_name, password):
    '''
    creates a new user
    '''
    new_user = User(user_name, password)
    return new_user


def save_user(user):
    '''
    will save new_users
    '''
    user.save_user()


def find_user_by_user_name(user_name):
    
    '''Function that finds user_name by number'''
    return User.find_user_by_user_name(user_name)


def display_users():
    '''will return all saved users'''
    return User.display_users()

def generate_passwords(user):
    '''will generate passwords for various accounts'''

    generate_accountPassword = user.generate_passwords()
    return generate_accountPassword

def save_accounts(accounts):
    '''function to save accounts'''
    return accounts.save_accounts()

def find_useraccounts(login_user_name):
    '''function to find user accounts'''
    return UserAccount.find_useraccount(login_user_name)

def useraccount_exists(login_user_name, login_password):
    '''function that will check if the user account exists'''
    account_exists = Useraccount.useraccount_exists(login_password,login_user_name)

    return account_exists

def create_account(username, password, website):
    '''
    function to create a new account
    '''
    new_account = UserAccount(username, password, website)
    return new_account


def save_account(account):
    '''
    will save new account
    '''
    account.save_account()

def display_account(account):
    '''
    checks if account can be displayed
    '''
    return UserAccount.copy_account(account)


def main():
    global login_name
    global login_password

    print("Welcome to password generator")
    print("Kindly wait")
    print("You name please?")
    personal_name = input()

    while True:
        print("these shortcodes will help you navigate easily: '~new'-create a new account, '~sign'-log in to any of your accounts")
        print("Input new or signIn")

        if short_code == 'new':
            print("Input username of your choice and automatically generate a password")
            print()
            name = input()
            print()
            passwords = generate_passwords()

            save_user = (create_user(user_name, password))

            print('\n')
            print("You successfully created your new account")
            print('\n')
            break
        
        elif short_code == 'signin':
            print(
            login_name = input()

            login = usercredential_exists(login_name, login_password)

            if login = True:
                print("You have successfully logged in.Enjoy!!")
                print()
                break

        else:
            print("Please use one of the two codes provide





