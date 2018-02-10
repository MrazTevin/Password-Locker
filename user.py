import pyperclip
import random


class User:
    """Will generate instances of user"""
    user_list = []
    """this is a class variable called account_list"""
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

    def save_user(self):
        """saves user objects into user_list"""
        User.user_list.append(self)

    def delete_user(self):
        """will delete users form user_list"""

        User.user_list.remove(self)

    @classmethod
    def user_by_user_name(cls, user_name):

        for user in cls.user_list:
            if user.login_user_name == user_name and user.login_password == password:
                return user

    @classmethod
    def display_users(cls):
        """this method will return the user_list"""
        return cls.user_list

    def generate_passwords(self, password):
        password = random.randint(1, 20)
        print(password)
