class Account:
    """Will generate instances of account"""
    account_list = []
    """this is a class variable called account_list"""
    def __init__(self, user_name, password):
        """Passed in 4 arguements and create 3 instance variables below"""
        self.user_name = user_name
        self.password = password

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
            if account.user_name == user_name:
                return account
