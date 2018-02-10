import pyperclip


class Account:
    """Will generate instances of account"""
    account_list = []
    """this is a class variable called account_list"""
    def __init__(self, login_user_name, login_password, login_website):
        """Passed in 4 arguements and create 3 instance variables below"""
        self.login_user_name = login_user_name
        self.login_password = login_password

    def save_account(self):
        """saving account object into object list"""
        Account.account_list.append(self)

    def delete_account(self):
        """will delete any account saved in the account_list"""
        Account.account_list.remove(self)

    @classmethod
    def find_by_user_name(cls, user_name):
        """
        this method will take a user_name and
        return an account that matches that user_name
        """

        for account in cls.account_list:
            if account.login_user_name == user_name:
                return account

    @classmethod
    def account_exist(cls, login_user_name):
        """
        we want to test if our account exists
        """

        for account in cls.account_list:
            if account.login_user_name == login_user_name and account.login_password == password:
                return True

        return False

    @classmethod
    def copy_account(cls, login_user_name):
        account_found = Account.find_account(login_user_name)
        pyperclip.copy(account_found.login_user_name)
