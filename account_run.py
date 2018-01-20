from account import Account


def create_account(user_name, password):
    new_account = Account(user_name, password)
    return new_account


def delete_account(account):
    """function that will delete an account"""
    account.delete_account()


def find_account(user_name):
    """finds an account user_name and returns that user_name"""
    return Account.find_by_account(user_name)


def display_accounts():
    """function that will return all saved accounts"""
    return Account.display_accounts()
    
