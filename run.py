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
    return User.find_user_by_user_name(user_name)


def display_aacount():
    return User.display_users()


def save_accounts(accounts):
    return accounts.save_accounts()
