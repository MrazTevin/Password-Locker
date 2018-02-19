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










