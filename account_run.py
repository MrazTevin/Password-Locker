from account import Account


def create_account(user_name, password):
    new_account = Account(user_name, password)
    return new_account
